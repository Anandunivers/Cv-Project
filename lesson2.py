# Resizing and Scaling Image (cv2.resize)

'''
1 .We use for size and  Proseccing
Syntax 

variable=lib(cv2.).function(resize)(original(Src),diminsion Size(dsize),optional( fx,fy,interpolation))

'''

import cv2

# load image

# image=cv2.imread("img1.png")
# if image is None:
#     print("Image not found ")
# else:
#     print("Image Found")
#     # In this function put value in form of tuple 
#     resized=cv2.resize(image,(300,300))

#     cv2.imshow("Origanal image:",image)
#     cv2.imshow("Resized image:",resized)

#     cv2.imwrite("Resized_img.png",resized)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Cropping Image using Slicing in opneCv 
#  Crop a image form real image 

# Load a image 

image=cv2.imread("img1.png")

# Check image is not found 


'''if image is not None:
    cropped=image[150:300,500:800]

    cv2.imshow("Original:",image)
    cv2.imshow("CroppedImage:",cropped)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
else:
    print("Image not Found")'''


if image is None:
    print("Image Not found;")
else:

    filp_h=cv2.flip(image,1)
    filp_v=cv2.flip(image,0)
    filp_both=cv2.flip(image,-1)

    cv2.imshow("Origanal",image)
    cv2.imshow("Horizontal",filp_h)
    cv2.imshow("vartical",filp_v)
    cv2.imshow("Both",filp_both)


    cv2.waitKey(0)
    cv2.destroyAllWindows()