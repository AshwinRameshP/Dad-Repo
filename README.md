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
### To download the processed file
Open URL - http://rm-output.s3-website.ap-south-1.amazonaws.com
Enter Credentials
AWS Region : ap-south-1
Bucket Name : rm-output
Scroll down to Files in S3 > List Files >click "updated{File name}.xlsx" > file will be auto downloaded in new tab

## File Structure over view
### RM_OrderProcessor_UI
Contains all UI  code for application
#### RM Downloader UI
Contains UI files for the download from s3 bucket . Simple html web file
url: http://rm-output.s3-website.ap-south-1.amazonaws.com
#### RM_WebAPP
Angular Project for RM_WebApp
url : http://rm-ui-for-s3.s3-website.ap-south-1.amazonaws.com
### RM_Processor Lambda
RM_Processor.py contains the code for lambda s3-trigger-lambda
