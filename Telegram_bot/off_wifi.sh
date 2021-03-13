#!/bin /bash


# Disable WiFi-device
uci set wireless.radio0.disabled="1"

# Disable WiFi-interface
uci set wireless.default_radio0.disabled="1"

wifi reload
sleep 1s
uci commit wireless; wifi
