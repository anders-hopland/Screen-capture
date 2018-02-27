from threading import Thread
import sys
import cv2
from queue import Queue

class Streamer:
    def __init__(self, queue_size=128):

        self.stream = cv2.VideoCapture('udp://@192.168.1.1:9999')
        self.stopped = False

        self.Q = Queue(maxsize=queueSize)

    def start(self):
        thread = Thread(target=self.update, args=())
        thread.daemon = True
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            if not self.Q.full():
                (ret, frame) = self.stream.read()


                if not grabbed:
                    self.stop()
                    return

                self.Q-put(frame)

    def read(self):
        return self.Q.get()

    def more(self):
        return self.Q.qsize() > 0

    def stop(self):
        self.stopped = True


