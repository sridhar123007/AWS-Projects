import boto3
import json
region='us-east-2'
ACCESS_ID='AKIA4P2Q725XUMKBPBLA'
ACCESS_KEY='CjACD4GnCcY7FxbrdBpeSlnFFQKw7O3B+E4EdCW+'

def detect_faces(photo):

    client=boto3.client('rekognition',region,aws_access_key_id=ACCESS_ID,aws_secret_access_key= ACCESS_KEY)

    with open(photo, 'rb') as image:
        response = client.detect_faces(Image={'Bytes':image.read()},Attributes=['ALL'])
    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        print('The detected face is between')
        print('looks like a face: '+ str(faceDetail['Confidence']))
        print('AgeRange:  ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        print('Eyeglasses: ' + str(faceDetail['Eyeglasses']['Confidence']))
        print('Beard: '+ str(faceDetail['Beard']['Confidence']))
        print('appears to be male: '+ str(faceDetail['Gender']['Confidence']))
        print('EyesOpen: '+ str(faceDetail['EyesOpen']['Confidence']))
        print('MouthOpen: ' + str(faceDetail['MouthOpen']['Confidence']))
        print('Mustache: '+ str(faceDetail['Mustache']['Confidence']))
        print('Smile: '+ str(faceDetail['Smile']['Confidence']))
        print('Sunglasses: '+ str(faceDetail['Sunglasses']['Confidence']))
        #print('Here are the other attributes:')
        #print(json.dumps(faceDetail, indent=4, sort_keys=True))
    return len(response['FaceDetails'])
def main():
    photo='C:\Users\VSES006\Desktop\Sridhar\i.jpg'
    face_count=detect_faces(photo)
    print("Faces detected: " + str(face_count))


main()
