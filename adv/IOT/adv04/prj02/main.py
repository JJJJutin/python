#########################匯入模組#########################
import network

#########################函式與類別定義#########################

#########################宣告與設定#########################
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)

# search wifi
wifi_list = wlan.scan()
print("Scan resualt")
for i in range(len(wifi_list)):
    print(wifi_list[i])

wlSSID = "SingularClass"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD)
while not (wlan.isconnected()):
    pass
print("connet ok", wlan.ifconfig())
#########################主程式#########################
