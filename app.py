import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while True:
  ret,frame =cap.read()  
  cv2.imshow("Video Original",frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cv2.destroyAllWindows()
cap.release()