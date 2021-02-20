import boto3
from botocore.exceptions import NoCredentialsError

import cv2

"""videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()"""

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA4P2Q725XUMKBPBLA'
secret_access_key = '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'

#Region
region='us-east-2' 

#local_file = 'text.jpg'
#bucket_name ='imagebucket1234567'

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


uploaded = upload_to_aws('C:\Users\VSES006\Desktop\Sridhar\car1.jpg', 'imagebucket1234567', 'NewPicture.jpg')

photo = 'NewPicture2.jpg'
photo1 ='NewPicture.jpg'

client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

with open(photo, 'rb') as image:
    #response = client.detect_labels(Image={'Bytes': image.read()})
    response = client.compare_faces(
        SourceImage={
                 'S3Object': {
                'Bucket': 'imagebucket1234567',
                'Name': photo
            }
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
            if(key=='Similarity'):
                print("face matches")
print response
