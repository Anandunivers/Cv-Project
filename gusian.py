import cv2
import numpy as np

img=cv2.imread("free-nature-images.jpg")
blured=cv2.GaussianBlur(img,(7,7),4)
# use the midean blur

MB=cv2.medianBlur(img,11)
# Now we use Sharpning 
''' In the sharpaning Use the np array filter  2d '''

Sharp_kernal=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])


# show the iamge 

cv2.imshow("Original iamge :",img)
cv2.imshow("Blured Image:",blured)
# Show the median blure

cv2.imshow("Median Blur:",MB)
# Show the Shapness of imaGE 
sh=cv2.filter2D(img,-1,Sharp_kernal)

cv2.imshow("Kernal Shapness:",sh)





cv2.waitKey(0)
cv2.destroyAllWindows()