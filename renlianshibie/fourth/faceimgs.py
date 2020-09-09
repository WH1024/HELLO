import init
import cv2
filename = 'A.jpg'
client=init.init_baidu()
img=init.image(filename)
options=init.option()
result = client.detect(img, 'BASE64',options)
img2 = cv2.imread(filename)
# 用代码实现进行裁剪的问题，确定问题所在

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




