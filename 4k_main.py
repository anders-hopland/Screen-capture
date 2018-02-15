import numpy as np
import cv2

cap = cv2.VideoCapture('udp://@192.168.1.1:9999')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output1.avi', fourcc, 30.0, (1280, 720))
out2 = cv2.VideoWriter('output2.avi', fourcc, 30.0, (1280, 720))
out3 = cv2.VideoWriter('output3.avi', fourcc, 30.0, (1280, 720))
out4 = cv2.VideoWriter('output4.avi', fourcc, 30.0, (1280, 720))
out5 = cv2.VideoWriter('output5.avi', fourcc, 30.0, (1280, 720))

while(cap.isOpened):
    ret, frame = cap.read()

    ret, frame = cap.read()
    if ret:

        width = cap.get(3)   # float
        height = cap.get(4) # float

        print(width)
        print(height)

        frame1 = frame[0:720, 0:1280]
        frame2 = frame[720:1440, 0:1280]
        frame3 = frame[1440:2160, 0:1280]
        frame4 = frame[0:720, 1280:2560]
        frame5 = frame[720:1440, 1280:2560]

        # write the flipped frame
        out1.write(frame1)
        out2.write(frame2)
        out3.write(frame3)
        out4.write(frame4)
        out5.write(frame5)

    else:
        break

# Release everything if job is finished
cap.release()

out1.release()
out2.release()
out3.release()
out4.release()
out5.release()
cv2.destroyAllWindows()
