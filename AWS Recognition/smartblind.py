#import the boto3  library to connect to the AWS service
import boto3
from pygame import mixer
import os

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA5LVWLJRMO6N5HREA'
secret_access_key = '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'

#Region
region='us-east-2'

#client representing AWS Rekognition service
client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)
polly = boto3.client('polly', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)                     

#image of the bucket
photo = 'traf.jpg'
response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'imanc',
            'Name': photo
            }},
    MaxLabels=5,
    MinConfidence=95
    )
                                

print(response)

print("Hello I am Seeing "+response["Labels"][0]["Name"])

#print("It may be "+response["Labels"][2]["Name"])

spoken_text = polly.synthesize_speech(Text="Hello I am Seeing "+response["Labels"][0]["Name"],
                                      OutputFormat='mp3',
                                      VoiceId='Emma')

with open('output.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()

mixer.init()#initilizing mixer
mixer.music.load('output.mp3')#load our output
mixer.music.play()#play the loaded output

#once speaking is done delete the file
while mixer.music.get_busy() == True:
    pass

mixer.quit()
os.remove('output.mp3')
