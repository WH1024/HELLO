import init
import cv2

# 定义服务器常量client,初始化AipFace对象建立连接
client = init.init_baidu()
# 将大合照路径赋予变量filename
filename = './photo/8888.jpg'
# image方法读取图片
image = init.image(filename)
# 初始化人脸检测方法
options = init.option()
# 实现人脸检测功能
result = client.detect(image, 'BASE64', options)
# 使用cv2.imread方法读取图片
img = cv2.imread(filename)
i = 0
# 搜索人脸实现人脸搜索功能
for face in result['result']['face_list']:
    x1 = int(face['location']['left'])
    y1 = int(face['location']['top'])
    x2 = int(x1 + face['location']['width'])
    y2 = int(y1 + face['location']['height'])
    DetectFace = img[y1 - 40:y2 + 40, x1 - 40:x2 + 40]
    cv2.imwrite('./photo/DetectFace.jpg', DetectFace)
    # 调用人脸比对
    resultMatch = client.match([
        {'image': init.image('./photo/888.jpg'),
         'image_type': 'BASE64',
         },
        {'image': init.image('./photo/DetectFace.jpg'),
         'image_type': 'BASE64',
         }
    ])
    # 记录相似度较高的人脸信息
    if resultMatch['result']['score'] > 40:
        cv2.namedWindow("Image", 0)
        cv2.resizeWindow("Image", 200, 240);
        cv2.moveWindow("Image", 400, 300)
        cv2.imshow("Image", DetectFace)
        cv2.waitKey(0)
        cv2.destroyWindow("Image")
        i = 1
        break;
if (i == 0):
    print("not found")