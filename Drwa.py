import cv2

image=cv2.imread("img2.jpg")

# Drwan the cricel 

if image is None:
    print("Oopos! Image is not Found")
else:
    print("Image Load Succesfully !")
    # Cricel 

    # cv2.circle(image,(300,350),100,(255,0,0))

    # pt1=(50,100)
    # pt2=(300,100)
    # color=(255,0,0)
    # tkn=5
    
    # Drwa line 
    # cv2.line(image,pt1,pt2,color,tkn)


    # cv2.imshow("Drwa a Cricle:",image)
    # cv2.imshow("Line Drwaing",image)

    # puttext on image 

    cv2.putText(image,"Hello Boys",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),2)

    cv2.imshow("Adding Text Over Iamge:",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()