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
photo = 'C:\Users\VSES006\Desktop\Sridhar\k.jpg'
photo1='sk.jpg'
with open(photo, 'rb') as image:
    #response = client.detect_labels(Image={'Bytes': image.read()})
    response = client.compare_faces(
        SourceImage={
            'Bytes': image.read()
          # 'S3Object': {
              #  'Bucket': 'imagebucket1234567',
              #  'Name': photo}
                },
        TargetImage={
            'S3Object': {
                'Bucket': 'imagebucket1234567',
                'Name': photo1
            }
        },
      
        )
for key, value in response.items():
    if key in ('FaceMatches', 'UnMatchedFaces'):
        print(key)
        for att in value:
            print(att)
#print(response)
