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
polly_client = boto3.client('polly',
                            region,
                            aws_access_key_id = access_key_id,
                            aws_secret_access_key = secret_access_key)

response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = response["TextDetections"][0]["DetectedText"])

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
