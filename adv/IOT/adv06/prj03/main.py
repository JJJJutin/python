#########################匯入模組#########################
import paho.mqtt.client as mqtt


#########################函式與類別定義#########################
def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"Connect Finish:{reason_code}")
    client.subscribe("abifaelahfbe;Bhbfe")


def on_message(client, userdata, msg):
    print(f"My Subscribe Topic Is:{msg.topic}, Get Msg:{msg.payload.decode('utf-8')}")


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect

client.on_message = on_message

client.username_pw_set("singular", "Singular#1234")

client.connect("mqtt.singularinnovation-ai.com", 1883, 60)

client.loop_forever()
#########################主程式#########################
