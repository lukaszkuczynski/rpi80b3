import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
from gpiozero import CPUTemperature

oled_reset = digitalio.DigitalInOut(board.D4)

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)


def update_stats():


  oled.fill(0)
  oled.show()

  image = Image.new("1", (oled.width, oled.height))
  draw = ImageDraw.Draw(image)
  font = ImageFont.load_default()

  cpu = CPUTemperature()
  text = "RPi80B3\nCPU temp: %.2f" % cpu.temperature
  (font_width, font_height) = font.getsize(text)
  draw.text(
    (0,0),
    text,
    font=font,
    fill=255,
  )
  oled.image(image)
  oled.show()


while 1:
  update_stats()
  time.sleep(2)

