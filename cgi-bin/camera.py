#!/usr/bin/python

import time
import cv2

def capture_camera(mirror=True, size=None):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if mirror is True:
        frame = frame[:,::-1]

    if size is not None and len(size) == 2:
        frame = cv2.resize(frame, size)

    cv2.imwrite('./foo.jpg', frame)
    cap.release()
    cv2.destroyAllWindows()

capture_camera()
print "Content-type: text/html\n"
print """
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="Refresh" content="1">
    <title>Camera</title>
  </head>
  <body>
    <div align = center><img src="/foo.jpg"></div>
   </body>
</html>
"""
