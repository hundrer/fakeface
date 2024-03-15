import speech_recognition as sr
import cv2 as cv
from fake_camera import FakeCamera  # import the class

blink = 0
def speech():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as sourse:
        try:
            audio = r.listen(sourse, phrase_time_limit=0.35, timeout=0.10)
        except(sr.WaitTimeoutError, sr.UnknownValueError):
            return False
        else:
            return True
while True:
    if speech():
        if blink > 15:
            i = "blink_say.jpg"
            blink = 0
        else:
            i = "say.jpg"
    else:
        if blink > 15:
            i = "blink.jpg"
            blink = 0
        else:
            i = "neutral.jpg"
    fake_cam_object = FakeCamera().add_foreground_image(i).add_background_image().build()
    snapshot = fake_cam_object.get_snapshot()
    cv.imshow("Moving Image", snapshot)
    blink += 1
    if cv.waitKey(1) & 0xFF == ord("q"):
        break