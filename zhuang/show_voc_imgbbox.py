import cv2

# img=cv2.imread("/home/zhj/py/keras-yolo3-master/VOCdevkit/VOC2007/JPEGImages/000061.jpg")
# img=cv2.imread("/home/zhj/py/keras-yolo3-master/VOCdevkit2007/VOC2007/JPEGImages/000061.jpg")
#
# width=img.shape[1]
# height=img.shape[0]
# print(width)
# file=open("/home/zhj/py/keras-yolo3-master/VOCdevkit/VOC2007/labels/000061.txt")
# while(1):
#     line=file.readline()
#     print("line=",line)
#     list=line.split(' ')
#     print(len(list))
#     print(list)
#     #中心坐标x,y和w,h系数
#     w=float(list[3])*width
#     h=float(list[4])*height
#     x=float(list[1])*width-w/2
#     y=float(list[2])*height-h/2
#     print(x,y,w,h)
#     x,y,w,h = int(x),int(y),int(w),int(h)
#     cv2.rectangle(img,(x,y),(x + w, y + h),(255,0,0))
#     cv2.imshow("img",img)
#     if cv2.waitKey(0)==ord('q'):
#         break

file=open("/home/zhj/py/keras-yolo3-master/2012_traindel.txt")
while(1):
    line=file.readline()
    print(line)
    list = line.split(' ')
    print(list)
    if(len(list)<2):continue
    img = cv2.imread(list[0])
    list2=[]
    for i in range(int(len(list)-1)):
        list3=list[i+1].split(",")
        list2.append(list3)
    print("len",len(list2))
    for i in range(int(len(list2))):
        print(list2)
        print(list2[i][0])
        print(list2[i][1])
        print(list2[i][2])
        print(list2[i][3])
        ####xmin,ymin,xmax,ymax实际大小，非系数
        w=(float(list2[i][2])-float(list2[i][0]))
        h=(float(list2[i][3])-float(list2[i][1]))
        x=float(list2[i][0])
        y=float(list2[i][1])
        x,y,w,h = int(x),int(y),int(w),int(h)
        cv2.rectangle(img,(x,y),(x + w, y + h),(255,0,0))
        cv2.imshow("imghe",img)
        if cv2.waitKey(0)==ord('q'):
            break