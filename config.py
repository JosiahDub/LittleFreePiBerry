import os
# For testing outside of the Pi
if os.uname()[4][:3] == 'arm':
    import picamera


# camera = picamera.PiCamera()
