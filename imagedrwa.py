# Line dwra 

import cv2

image=cv2.imread("img1.png")

if image is None:
    print("image is not found")
else:
    print("Image load Successfully")
    cv2.imshow("Origanal",image)

    pt1=(50,50)
    pt2=(250,200)
    color=(255,0,0)
    thickness=4
    
    # line and ractangel
    line=cv2.rectangle(image,pt1,pt2,color,thickness)
    ractangle=cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.line(image,pt1,pt2,color,thickness)
    
    cv2.imshow("Line On Image:",ractangle)
    cv2.imshow("Line on image",line)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

