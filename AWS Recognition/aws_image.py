import boto3
region='us-east-2'
access_key_id = "AKIA4P2Q725XUMKBPBLA"
secret_access_key = "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"

photo = 'C:/Users/VSES006/Desktop/Sridhar/Amerikamura_(Busy).jpg'
    
client = boto3.client('rekognition',region,aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)
with open(photo,'rb') as source_image:
    #source_bytes = source_image.read()
    response = client.detect_labels(Image={'Bytes':source_image.read()},
                                MaxLables=10)
    print response

