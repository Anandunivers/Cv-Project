import cv2

# Load iamge form computer System
# Task one take iamge as a input from user 

path = input("Enter image path: ")
image = cv2.imread(path)

# Convert in  Gray scale and Show the image 
print("What you want Show(Press 1 for show ),only save Name")
User=int(input("Enter a Value 1 or 2 :"))

if image is not None:
    if User==1:
    
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Black and White :",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif User==2:
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        name=input("Enter your File Name:")
        save=cv2.imwrite(name,gray)
        if save:
            print(f"Your iamge Save Succesfully:{name}")
        else:
            print("Image Not Found ")


else:
    print("Image Is not found ")

