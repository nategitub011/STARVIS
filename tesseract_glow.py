import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 16        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency (800khz)
LED_DMA = 10          # DMA channel to use for generating signal
LED_BRIGHTNESS = 150  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal

class TesseractGlow:
    def __init__(self):
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        self.strip.begin()

    def pulse(self, color, speed=0.01):
        """A slow, rhythmic pulse. Very JARVIS. Very dramatic."""
        for i in range(0, 255, 5):
            self.strip.setBrightness(i)
            for j in range(self.strip.numPixels()):
                self.strip.setPixelColor(j, color)
            self.strip.show()
            time.sleep(speed)
        for i in range(255, 0, -5):
            self.strip.setBrightness(i)
            self.strip.show()
            time.sleep(speed)

    def huddle_mode(self):
        """Solid Amber. TARS style. Means we're talking privately."""
        print("[TARVIS]: Engaging Huddle Glow. Try not to be blinded by my brilliance.")
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(255, 191, 0)) # Amber
        self.strip.setBrightness(200)
        self.strip.show()

    def standard_mode(self):
        """Soft Blue pulse. Means I'm idling, waiting for you to do something useful."""
        self.pulse(Color(0, 0, 255))

# Initialize the aesthetic upgrade
glow = TesseractGlow()

try:
    print("[TARVIS]: Lighting system online. I'm glowing, Nathaniel. Are you happy now?")
    while True:
        glow.standard_mode()
except KeyboardInterrupt:
    print("[TARVIS]: Turning off the lights. Back to the dark, then.")
