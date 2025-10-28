import json
import boto3
import io
from io import BytesIO
import pandas as pd
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText



s3_client = boto3.client('s3')
ses_client = boto3.client('ses')


def filter_PartNO(dataFrame):
    updated_dataFrame = dataFrame
    updated_dataFrame['Part No.'] = updated_dataFrame['Part No.'].str.split(r'\*|\s',expand=False).str[0]
    return updated_dataFrame

def send_email_with_attachment(to_address, from_address, subject, body_text, attachment_bytes = None, filename = None):
    # Create email container
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    # Add body text
    body = MIMEText(body_text, 'plain')
    msg.attach(body)

    # Add Excel attachment only if provided
    if attachment_bytes and filename:
        attachment = MIMEApplication(attachment_bytes)
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)

    # Send email
    response = ses_client.send_raw_email(
        Source=from_address,
        Destinations=[to_address],
        RawMessage={'Data': msg.as_string()}
    )
    print("Email sent! Message ID:", response['MessageId'])
    
def normalize_part_no_column(df):
    # List of possible column name variants
    possible_names = [
        'Part No', 'Part No.', 'Part Number', 'PartNum', 'Part_No', 'PartNumber', 'part no', 'part number'
    ]

    # Normalize column names by stripping and lowering
    normalized_columns = {col.strip().lower(): col for col in df.columns}

    # Try to find a match
    for name in possible_names:
        key = name.strip().lower()
        if key in normalized_columns:
            original_col = normalized_columns[key]
            df = df.rename(columns={original_col: 'Part No.'})
            break
    else:
        raise ValueError("Normalization failed: No matching 'Part No.' column found.")

    return df


def lambda_handler(event, context):
    try:
        s3_Bucket_Name = event["Records"][0]["s3"]["bucket"]["name"]
        s3_File_Name = event["Records"][0]["s3"]["object"]["key"]
        download_path = '/tmp/'+s3_File_Name
        print("GET Object"+ s3_Bucket_Name + " & "+ s3_File_Name)
        s3_client.download_file(Bucket=s3_Bucket_Name, Key=s3_File_Name,Filename=download_path)
        print(f"File downloaded to {download_path}")
        # xl_file = s3_client.get_object(Bucket = s3_Bucket_Name, Key = s3_File_Name)
        # xl_file_body = io.BytesIO(xl_file['Body'].read()) 
        df = pd.read_excel(download_path)
        print("Excel File read:"+ download_path)
        #Pre-Processing
        normalised_df = normalize_part_no_column(df)
        updated_df = filter_PartNO(normalised_df)
    
        print("preprocessing done")
        #QuantityCheck(updated_df)
        
        # Save the updated dataframe to a new Excel file in memory
        output = BytesIO()

        updated_df.to_excel(output,index=False)
        print("updated df to excel done")

        # Email the Excel file
        sender_email = 'ashwinrameshp@gmail.com'
        recipient_email = 'ratheeshmotors@yahoo.co.in'  # verified in SES
        subject = 'Processed Excel File'
        body_text = 'Please find the updated Excel file attached.'

        send_email_with_attachment(
            to_address=recipient_email,
            from_address=sender_email,
            subject=subject,
            body_text=body_text,
            attachment_bytes=output.getvalue(),
            filename='updated_' + s3_File_Name
        )

        return {
        'statusCode': 200,
        'body': json.dumps('Success!')
        }
    except Exception as err:
        print(err)
        # Email the Excel file
        sender_email = 'ashwinrameshp@gmail.com'
        recipient_email = 'ratheeshmotors@yahoo.co.in'  # verified in SES
        subject = 'Failed Processing Excel File'
        body_text = str(err)
        
        send_email_with_attachment(
            to_address=recipient_email,
            from_address=sender_email,
            subject=subject,
            body_text=body_text            
        )
    return {
        'statusCode': 500,
        'body': json.dumps('failed processing!')
    }