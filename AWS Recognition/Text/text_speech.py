import boto3

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA4P2Q725XUMKBPBLA'
secret_access_key = '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'

#Region
region='us-east-2' 

bucket='imagebucket1234567'
photo='text.jpg'

client = boto3.client('polly', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

  
response = client.synthesize_speech(
    OutputFormat='mp3',
    SampleRate='8000',
    Text='All Gaul is divided into three parts',
    TextType='text',
    VoiceId='Joanna',
)

print response

