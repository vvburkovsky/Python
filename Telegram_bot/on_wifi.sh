#!/bin /bash


# Enable WiFi-device
uci set wireless.radio0.disabled="0"

# Enable WiFi-interface
uci set wireless.default_radio0.disabled="0"

wifi reload
sleep 1s
uci commit wireless; wifi
