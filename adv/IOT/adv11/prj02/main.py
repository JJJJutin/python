#########################匯入模組#########################
import time
import mcu


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "Jutin", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
mqtt_client.subscribe("mdfk", on_message)

gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)

m = 0
#########################主程式#########################
while True:
    mqtt_client.check_msg()
    servo.angle(int(m))
    time.sleep(1)
