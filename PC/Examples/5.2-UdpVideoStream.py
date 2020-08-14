# coding: utf-8


from test_env_setup import *
from Lib.CameraSocket import CameraSocket

import sys
import cv2


if len(sys.argv) == 3:
    _host = sys.argv[1]
    _port = int(sys.argv[2])
else:
    print("Add adress and port to bind")
    sys.exit(0)


socket = CameraSocket().Bind(_host, _port)
connected = socket.WaitConnection()


if not connected:
    print("Timeout error: waiting connection from Hololens")
    sys.exit(0)
else:
    print("Connected to {}".format(socket.client))

while True:

    frame = socket.GetFrame()

    # display
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) == ord('q'): break


socket.Exit()
socket.close()
cv2.destroyAllWindows()