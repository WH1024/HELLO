import cv2
import init
videoCapture=cv2.VideoCapture(0)
fps=videoCapture.get(cv2.CAP_PROP_FPS)
size=(int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),\
     int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(fps,size)

success,img=videoCapture.read()
cv2.imwrite('camera.jpg', img)

filename = 'camera.jpg'
client=init.init_baidu()
img=init.image(filename)
options=init.option()
result = client.detect(img, 'BASE64',options)
img2 = cv2.imread(filename)
index=0
while index<len(result['result']['face_list']):
    face=result['result']['face_list'][index]
    print("性别：", face['gender']['type'])
    print("年龄：", face['age'])
    x1 = int(face['location']['left'])
    y1 = int(face['location']['top'])
    x2 = int(x1 + face['location']['width'])
    y2 = int(y1 + face['location']['height'])
    print('(',x1,y1,')','(',x2,y2,')',"\n")
    imgSave = img2[y1:y2, x1:x2]
    cv2.imwrite('%d.jpg' % index, imgSave)

    index+=1
