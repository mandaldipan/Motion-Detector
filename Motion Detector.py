"""
- Image processing from Video (Webcam) using Opencv
  This contains Face and Eye Detection using the
  Haar Cascade Classifier (Viola Jones Algorithm) & openCV module.
@author : Dipan Mandal
"""

import cv2

initial_frame = None
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    # print(frame)        # Prints the NumPy array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (25, 25), 0)

    if initial_frame is None:
        initial_frame = gray
        continue

    delta_frame = cv2.absdiff(initial_frame, gray)
    thresh_delta = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
    (cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 2000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(frame,'Motion Detected!!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Blurred Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_delta)

    key = cv2.waitKey(1)
    if key == ord(27):
        break

print(a)
video.release()
cv2.destroyAllWindows()
