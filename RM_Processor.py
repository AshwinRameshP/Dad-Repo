import json
import boto3
import io
from io import BytesIO
import pandas as pd

s3_client = boto3.client('s3')

def filter_PartNO(dataFrame):
    updated_dataFrame = dataFrame
    updated_dataFrame['Part No.'] = updated_dataFrame['Part No.'].str.split(r'\*|\s',expand=False).str[0]
    return updated_dataFrame

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
        updated_df = filter_PartNO(df)
    
        print("preprocessing done")
        #QuantityCheck(updated_df)
        
        # Save the updated dataframe to a new Excel file in memory
        output = BytesIO()

        updated_df.to_excel(output,index=False)
        print("updated df to excel done")
        # Upload the new Excel file to the destination S3 bucket
        destination_bucket_name = 'rm-output'
        destination_file_name = 'updated_' + s3_File_Name
        s3_client.put_object(Bucket=destination_bucket_name, Key=destination_file_name, Body=output.getvalue())
        print("upload to s3 destination done")
        return {
        'statusCode': 200,
        'body': json.dumps('Success!')
        }
    except Exception as err:
        print(err)
    return {
        'statusCode': 500,
        'body': json.dumps('failed processing!')
    }