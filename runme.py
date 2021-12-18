import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "0"	# Blinking
        exit()
    elif gaze.is_right():
        text = "1"	# Right
    elif gaze.is_left():
        text = "2"	# Left
    elif gaze.is_center():
        text = "3"	# Center

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 0, 255), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0,255,0), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0,255,0), 1)
    
    """Store the coordinates in a variable and write it to a file"""

    left_co=str(text)    
    file1=open("pswdfile.txt", "a")
    file1.write(left_co)
    file1.close()
    
    cv2.imshow("GAZE", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
