#import the boto3  library to connect to the AWS service
import boto3

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA4P2Q725XUMKBPBLA'
secret_access_key = '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'

#Region
region='us-east-2' 

#client representing AWS Rekognition service
client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)
                     
#image of the bucket
photo = 'k.jpg'
response = client.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': 'imagebucket1234567',
            'Name': photo,
        }
    }
)

print(response)
