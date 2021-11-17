# ESPHome BLE Keyboard
[![donate paypal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/dslonyara)
[![donate tinkoff](https://img.shields.io/badge/Donate-Tinkoff-yellow.svg)](https://www.tinkoff.ru/sl/3FteV5DtBOV)

The firmware implements the ability to connect your esp32 device as a BLE keyboard and send keystrokes via Home Assistant

## Table of Contents
- [FAQ](#faq)
- [Build](#build)
- [Sensors](#sensors)
- [Service](#service)
- [Examples](#examples)
- [Keys](#keys)

## FAQ
**Q. Are all keys supported?**

**A.** No, only those that are implemented in the [ESP32 BLE Keyboard library](https://github.com/T-vK/ESP32-BLE-Keyboard). This also applies to languages.

**Q. What devices can the keyboard be connected to?**

**A.** Windows, Linux, Android - Fully supported. MacOS, IOS - It does not work stably. But it works. More details in the library: [ESP32 BLE Keyboard library](https://github.com/T-vK/ESP32-BLE-Keyboard)

**Q. No keys are pressed or one is pressed several times. What to do?**

**A.** The delay modification will help.

## Build

1. Fill in WiFi credentials and esp32 board in [blekeyboard.yaml](https://github.com/dmamontov/esphome-blekeyboard/blekeyboard.yaml)
2. Use [ESPHome](https://esphome.io) to build and upload firmware

## Sensors

- Connected (binary_sensor) - Whether the device is connected to the keyboard.
- Delay (sensor) - The last set delay. After rebooting the device is reset to 8ms by default.
- Wifi Signal (sensor) - Wifi signal strength.

## Service

**Via GUI (Recommended)**

`Developer-tools` > `Service` > `esphome.blekeyboard_send`

**Via YAML (legacy way)**
```yaml
service: esphome.blekeyboard_send
data:
  message: 'Hello world!' # Message or key name, if the is_combination flag is set, then you can specify a key combination separated by +.
  is_combination: false # Whether a key combination is used in the message.
  delay_ms: 8 # Delay between clicks in milliseconds
```

## Examples

#### Sending a simple message

```yaml
service: esphome.blekeyboard_send
data:
  message: 'Hello world!'
  is_combination: false
  delay_ms: 8
```

#### Pressing the ENTER key

```yaml
service: esphome.blekeyboard_send
data:
  message: 'KEY_RETURN'
  is_combination: false
  delay_ms: 8
```

#### Press CTRL + ALT + DELETE

```yaml
service: esphome.blekeyboard_send
data:
  message: 'KEY_LEFT_CTRL+KEY_LEFT_ALT+KEY_DELETE'
  is_combination: true
  delay_ms: 10
```

## Keys

The following keys are supported:

- KEY_LEFT_CTRL
- KEY_LEFT_SHIFT
- KEY_LEFT_ALT
- KEY_LEFT_GUI
- KEY_RIGHT_CTRL
- KEY_RIGHT_SHIFT
- KEY_RIGHT_ALT
- KEY_RIGHT_GUI


- KEY_UP_ARROW
- KEY_DOWN_ARROW
- KEY_LEFT_ARROW
- KEY_RIGHT_ARROW
- KEY_BACKSPACE
- KEY_TAB
- KEY_RETURN
- KEY_ESC
- KEY_INSERT
- KEY_DELETE
- KEY_PAGE_UP
- KEY_PAGE_DOWN
- KEY_HOME
- KEY_END
- KEY_CAPS_LOCK
- KEY_F1
- KEY_F2
- KEY_F3
- KEY_F4
- KEY_F5
- KEY_F6
- KEY_F7
- KEY_F8
- KEY_F9
- KEY_F10
- KEY_F11
- KEY_F12
- KEY_F13
- KEY_F14
- KEY_F15
- KEY_F16
- KEY_F17
- KEY_F18
- KEY_F19
- KEY_F20
- KEY_F21
- KEY_F22
- KEY_F23
- KEY_F24


- KEY_MEDIA_NEXT_TRACK
- KEY_MEDIA_PREVIOUS_TRACK
- KEY_MEDIA_STOP
- KEY_MEDIA_PLAY_PAUSE
- KEY_MEDIA_MUTE
- KEY_MEDIA_VOLUME_UP
- KEY_MEDIA_VOLUME_DOWN
- KEY_MEDIA_WWW_HOME
- KEY_MEDIA_LOCAL_MACHINE_BROWSER
- KEY_MEDIA_CALCULATOR
- KEY_MEDIA_WWW_BOOKMARKS
- KEY_MEDIA_WWW_SEARCH
- KEY_MEDIA_WWW_STOP
- KEY_MEDIA_WWW_BACK
- KEY_MEDIA_CONSUMER_CONTROL_CONFIGURATION
- KEY_MEDIA_EMAIL_READER
