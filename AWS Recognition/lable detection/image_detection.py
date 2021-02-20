import boto3
import json
region='us-east-2'
ACCESS_ID='AKIA4P2Q725XUMKBPBLA'
ACCESS_KEY='CjACD4GnCcY7FxbrdBpeSlnFFQKw7O3B+E4EdCW+'
def detect_labels_local_file(photo):


    client=boto3.client('rekognition',region,aws_access_key_id=ACCESS_ID,
aws_secret_access_key= ACCESS_KEY)
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        #print (label['Name'] + ' : ' + str(label['Confidence']))
        print(json.dumps(label, indent=4, sort_keys=True))
    return len(response['Labels'])

def main():
    photo='C:\Users\VSES006\Desktop\Sridhar\Amerikamura_(Busy).jpg'

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))


main()
