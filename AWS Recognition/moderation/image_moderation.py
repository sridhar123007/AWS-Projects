import boto3
import json
region='us-east-2'
ACCESS_ID='AKIA4P2Q725XUMKBPBLA'
ACCESS_KEY='CjACD4GnCcY7FxbrdBpeSlnFFQKw7O3B+E4EdCW+'

def moderate_image(photo):

    client=boto3.client('rekognition',region,aws_access_key_id=ACCESS_ID,aws_secret_access_key= ACCESS_KEY)

    with open(photo, 'rb') as image:
        response = client.detect_moderation_labels(Image={'Bytes':image.read()})

    print('Detected labels for ' + photo)    
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
        #print('Here are the other attributes:')
        #print(json.dumps(label, indent=4, sort_keys=True))
    return len(response['ModerationLabels'])

def main():
    photo='C:\Users\VSES006\Desktop\Sridhar\j.jpg'
    label_count=moderate_image(photo)
    print("Labels detected: " + str(label_count))

main()
 
 
