#wget https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
#wget https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml

# import the opencv library
import cv2
# load haarcascade model
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# define a video capture object
vid = cv2.VideoCapture(0)
print("Frame default resolution: (" + str(vid.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)) + "; " + str(vid.get(cv2.CAP_PROP_FPS)) + ")")

# vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# vid.set(cv2.CAP_PROP_FPS, 30)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayframe)  # returns a list of coordinates
    # points are in x, y, width, height format.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('preview window', frame)
      
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
