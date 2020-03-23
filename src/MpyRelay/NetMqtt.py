'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2020.02.15
License:     GNU, see LICENSE for more details
Description: 
'''

import umqtt.simple

class TMqtt
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
    # Attach call back handler to be called on receiving messages
    client.set_callback(onMessage)
    client.connect()
    client.publish(CONFIG['TOPIC'], "ESP8266 is Connected")
    client.publish(CONFIG['TOPIC'], "off")
    client.subscribe(CONFIG['TOPIC'])
    print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))

