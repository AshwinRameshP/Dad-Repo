# Dad-Repo
This repo is a Personal Repo used to help out my dad save some of his time with my coding skills.
#Dependencies
pip install -y requirements.txt

#RM OrderProcessor 
Built for RM   - by Ashwin
##Objective 
To Upload an excel file with 3 columns ( PartNo, Name, Quantity). 
To Process - ie., truncate the PartNo followed by first ' ' (space) .
Output the file back as an excel with updated file name.
## How to use?
### Upload File
Open URL- http://rm-ui-for-s3.s3-website.ap-south-1.amazonaws.com
Click "Choose file" > {select excel file from local file location} > Click "Upload"> Progress to be 100%
### Check Email for File
Open reciever email ratheeshmotors
Check mail from Ashwin
Open> download attachement

## File Structure over view
### RM_OrderProcessor_UI
Contains all UI  code for application
#### RM_WebAPP
Angular Project for RM_WebApp
url : http://rm-ui-for-s3.s3-website.ap-south-1.amazonaws.com

#### RM_Processor Lambda
RM_Processor.py contains the code for lambda s3-trigger-lambda
