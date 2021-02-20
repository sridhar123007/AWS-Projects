#import the boto3  library to connect to the AWS service
import boto3
from pygame import mixer
import os


#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA4P2Q725XUMKBPBLA'
secret_access_key = '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'

#Region
region='us-east-2' 

bucket='imagebucket1234567'
photo='5 bmw car wallpaper.jpg'

client = boto3.client('rekognition',
                      region,
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)
polly_client = boto3.client('polly',
                            region,
                            aws_access_key_id = access_key_id,
                            aws_secret_access_key = secret_access_key)
  
response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

                        
#textDetections=response['TextDetections']
print response
print(response["TextDetections"][0]["DetectedText"])


speech = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = response["TextDetections"][0]["DetectedText"])

with open('output.mp3', 'wb') as f:
    f.write(speech['AudioStream'].read())
    f.close()

mixer.init()#initilizing mixer
mixer.music.load('output.mp3')#load our output
mixer.music.play()#play the loaded output

#once speaking is done delete the file
while mixer.music.get_busy() == True:
    pass

mixer.quit()
os.remove('output.mp3')
