import time, neopixel
from machine import Pin, Timer
np = neopixel.NeoPixel(Pin(16), 3, timing=1)


class LEDCtrl(object):
    def __init__(self):
        self.deadline = 0
        self.beating = False
        self.beat = 0
        self.fingerPresent = False

    def heartbeat(self):
        print("heartbeat")
        for i in range(0, 4 * 256, 8):
            for j in range(np.n):
                if (i // 256) % 2 == 0:
                    val = i & 0xff
                else:
                    val = 255 - (i & 0xff)
                np[j] = (val, 0, 0) 
            np.write()
            time.sleep_ms(2)
        self.beating = False
        print("end heartbeat")
        self.beatPerMinute(self.beat, self.fingerPresent)

    def pulseTimer(self, t):
        if (time.ticks_ms() >= self.deadline):
            self.beating = True
            t.deinit()
            self.heartbeat()

    def beatPerMinute(self, beat, on): 
        self.beat = beat
        self.fingerPresent = on
        if self.fingerPresent:
            # finger is on
            if self.beating == False:
                self.beating = True
                # calculate the time to wait in between pulses
                pulse = int( (60 * 1000) / beat )
                self.deadline = time.ticks_add(time.ticks_ms(), pulse)
                print("d:", self.deadline, "pulse:", pulse)
                timer = Timer(0)  # timer id is in range 0-3     
                timer.init(period=80, mode=Timer.PERIODIC, callback=self.pulseTimer)

        else:
            self.deadline = time.ticks_ms()
            #print("no finger")  

