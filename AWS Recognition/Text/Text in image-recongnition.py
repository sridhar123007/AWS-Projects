import boto3

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA4P2Q725XUMKBPBLA'
secret_access_key = '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'

#Region
region='us-east-2' 

bucket='imagebucket1234567'
photo='text.jpg'

client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

  
response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

                        
textDetections=response['TextDetections']
print response
print(response["TextDetections"][0]["DetectedText"])
    
"""print 'Matching faces'
for text in textDetections:
    print 'Detected text:' + text['DetectedText']
    print 'Confidence: ' + "{:.2f}".format(text['Confidence']) + "%"
    print 'Id: {}'.format(text['Id'])
    if 'ParentId' in text:
        print 'Parent Id: {}'.format(text['ParentId'])
    print 'Type:' + text['Type']
    print"""
