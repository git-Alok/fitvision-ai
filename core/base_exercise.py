import math
from abc import ABC, abstractmethod


class BaseExercise(ABC):
    def __init__(self):
        self.reps = 0
        self.stage = None

    def calculate_angle(self, a, b, c):
        radians = math.atan2(c[1]-b[1], c[0]-b[0]) - \
                  math.atan2(a[1]-b[1], a[0]-b[0])
        angle = abs(math.degrees(radians))

        if angle > 180:
            angle = 360 - angle

        return angle

    def get_point(self, landmarks, idx):
        p = landmarks[idx]
        return (p.x, p.y)

    @abstractmethod
    def process(self, landmarks):
        pass

    @abstractmethod
    def reset(self):
        pass