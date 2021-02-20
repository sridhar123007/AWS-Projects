import boto3

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA4P2Q725XUMKBPBLA'
secret_access_key = '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'

#Region
region='us-east-2' 

bucket='imagebucket1234567'
photo='text.jpg'

def detect_text(photo, bucket):
    client = boto3.client('rekognition',
                          region,
                          aws_access_key_id = access_key_id,
                          aws_secret_access_key = secret_access_key)
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    polly_client = boto3.client('polly',
                            region,
                            aws_access_key_id = access_key_id,
                            aws_secret_access_key = secret_access_key)

    
                        
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    print (textDetections)
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            response = polly_client.synthesize_speech(VoiceId='Joanna',
                                              OutputFormat='mp3',
                                              Text = text['DetectedText'])#'This is a sample text to be synthesized.')
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()
            file = open('speech.mp3', 'wb')
            file.write(response['AudioStream'].read())
            file.close()
    return len(textDetections)

def main():
    bucket='imagebucket1234567'
    photo='text.jpg'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count))

main()

"""polly_client = boto3.client('polly',
                            region,
                            aws_access_key_id = access_key_id,
                            aws_secret_access_key = secret_access_key)

response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = 'This is a sample text to be synthesized.')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
print response"""
