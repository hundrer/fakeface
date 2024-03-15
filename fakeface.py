from speech_recognition import Recognizer, WaitTimeoutError, UnknownValueError, Microphone
from cv2 import imshow, waitKey
from fake_camera import FakeCamera  # import the class

class fakeface:
    def speech(self):
        r = Recognizer()
        with Microphone(device_index=1) as source:
            try:
                audio = r.listen(source, phrase_time_limit=0.35, timeout=0.10)
            except(WaitTimeoutError, UnknownValueError):
                return False
            else:
                return True
    def main(self):
        blink = 0
        while True:
            if self.speech(): #saying or not saying
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
            imshow("fakeface", snapshot)
            blink += 1
            if waitKey(1) & 0xFF == ord("q"):
                break
if __name__ == "__main__":
    a = fakeface()
    a.main() # an endless loop