import cv2 

img=cv2.imread("flower.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow("Origanal Image :",img)

# Use Edge Dection  function

edg=cv2.Canny(img,50,150)

cv2.imshow("Edges :",edg)
cv2.waitKey()
cv2.destroyAllWindows()  