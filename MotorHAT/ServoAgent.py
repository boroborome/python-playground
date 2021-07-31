
class ServoAgent(object):

    def __init__(self, channel, min, max, pwm, initAngle=50):
        self.channel = channel
        self.min = min
        self.max = max
        self.pwm = pwm
        self.currentAngle = initAngle
        self.delta = 5  # 舵机转动幅度

    def setServoPulse(self, pulse):
        pulseLength = 1000000.0  # 1,000,000 us per second
        pulseLength /= 50.0  # 60 Hz
        print("%d us per period" % pulseLength)
        pulseLength /= 4096.0  # 12 bits of resolution
        print("%d us per bit" % pulseLength)
        pulse *= 1000.0
        pulse /= (pulseLength * 1.0)
        # pwmV=int(pluse)
        print("pluse: %f  " % (pulse))
        self.pwm.setPWM(self.channel, 0, int(pulse))

    # Angle to PWM
    def write(self, angle):
        y = angle / 90.0 + 0.5
        y = max(y, 0.5)
        y = min(y, 2.5)
        self.setServoPulse(y)

    def setAngle(self, angle):
        if angle < self.min:
            angle = self.min
        if angle > self.max:
            angle = self.max

        self.write(angle)

    def increase(self):
        self.setAngle(self.currentAngle + self.delta)

    def decrease(self):
        self.setAngle(self.currentAngle - self.delta)

    def takePlace(self):
        self.setAngle(self.currentAngle)
