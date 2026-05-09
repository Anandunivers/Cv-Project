import cv2

image=cv2.imread("img1.png")
if image is not None:
    Success=cv2.imwrite("output.png",image)
    if Success:
        print("Image Svae Succesfully as output.png")
    else:
        print("falid to save  an image")
else:
    print("Error: Image could not find")
