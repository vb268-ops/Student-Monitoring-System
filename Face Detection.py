import cv2
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture video from webcam 
cap = cv2.VideoCapture(0)

n=0
b=0
initial_time=0
i=1

while i>0 :
    
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Time duration of a single frame
    gray = cv2.resize(gray, (500,300))
    final_time=time.time()
    if i>1 :
        a = final_time-initial_time
    else :
        a=0
    initial_time = final_time
    
    # Detect face
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw bounding box around face
    if(len(faces)>0):
        (x,y,w,h) = faces[0]
    else:
        n=n+a
        print(n)

    # Inform that attendance will not be given
    if n>3 :
        print("You have been missing for more than", 3 ,"seconds")
        f = " You Will be Marked Absent, Sorry! "
        print(f)
        g = 1
        break
        
    # Display video on real-time basis
    cv2.imshow('img', img)

    i=i+1
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture object
cap.release()


