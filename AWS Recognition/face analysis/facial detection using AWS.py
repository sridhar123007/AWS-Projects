import cv2, time
#import the boto3  library to connect to the AWS service
import boto3
import logging
from botocore.exceptions import ClientError

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA5LVWLJRMO6N5HREA'
secret_access_key = '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'

#Region
region='us-east-2'

#client representing AWS Rekognition service
s3 = boto3.client('s3', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', region, aws_access_key_id= access_key_id,
                      aws_secret_access_key=secret_access_key )

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    
img=cv2.imread("D:\\pic.jpg", 1)


#upload the image to s3 bucket
uploaded = upload_to_aws('D:\\pic.jpg', 'imanc', 'img.jpg')

       





