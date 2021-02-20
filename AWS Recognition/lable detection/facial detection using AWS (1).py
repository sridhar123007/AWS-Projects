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

#client representing AWS Rekognition and s3 service
s3 = boto3.client('s3', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)
client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

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
uploaded = upload_to_aws('C:\Users\VSES006\Desktop\Sridhar\Amerikamura_(Busy).jpg', 'imanc', 'img.jpg')

#image of the bucket
photo = 'img.jpg'
photo1='beyonce.jpg'

response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'imanc',
            'Name': photo
            }},
    TargetImage={
        'S3Object': {
            'Bucket': 'imanc',
            'Name': photo1
        }
    },
      
    )
for key, value in response.items():
    if key in ('FaceMatches', 'UnMatchedFaces'):
        print(key)
        for att in value:
            print(att)
            print("------------------------------------------------")
print(response['FaceMatches'])
print(response['UnmatchedFaces'])




       





