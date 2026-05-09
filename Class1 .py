import cv2

image=cv2.imread("img1.png")

# image load 

# image load 
# if image is None:
#     print("Error :Image Not Found")
# else:
#     print("Image load Done")

# Now iamge show used imshow()function

'''image show '''

if image is not None:
    cv2.imshow("Image Show",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")