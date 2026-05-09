import cv2
img=cv2.imread("img1.png")


'''Image Diminsion Use shaep attribute '''
<<<<<<< HEAD
'''if img is not None:
=======
if img is not None:
>>>>>>> 201bd9673a88088aa461d35d6d4ba26a6730b795
    h,w,c=img.shape
    print(f"Higth:{h},width:{w},Chennal:{c}")
else:
    print("Image not found")
<<<<<<< HEAD
'''

# cvtcolor  { Change the color full image in black white }

'''if img is not None:
    # Use cvtcolor function for chnage color 
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Black and white image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error:Image Could not load")'''

# 
=======

>>>>>>> 201bd9673a88088aa461d35d6d4ba26a6730b795
