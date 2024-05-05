#########################匯入模組#########################
import mcu
from machine import Pin, I2C
import ssd1306

#########################函式與類別定義#########################
gpio = mcu.gpio()
i2C = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2C)

#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
#########################主程式########################
oled.fill(0)
oled.text(f"{wi.ip}", 0, 0)
oled.text("Mother", 0, 10)
oled.text("Fxcker", 0, 20)
oled.show()
