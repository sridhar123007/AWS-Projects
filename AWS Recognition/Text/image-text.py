import boto3
import json
#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA4P2Q725XUMKBPBLA'
secret_access_key = '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'

#Region
region='us-east-2' 

bucket='imagebucket1234567'
photo='text.jpg'

def detect_text(photo, bucket):
    client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    print (textDetections)
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()
            print(json.dumps(textDetections, indent=4, sort_keys=True))
    return len(textDetections)

def main():
    bucket='imagebucket1234567'
    photo='text.jpg'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count))

main()
