# ESPHome BLE Keyboard
[![donate paypal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/dslonyara)
[![donate tinkoff](https://img.shields.io/badge/Donate-Tinkoff-yellow.svg)](https://www.tinkoff.ru/sl/3FteV5DtBOV)

The firmware implements the ability to connect your esp32 device as a BLE keyboard and send keystrokes via Home Assistant

## Table of Contents
- [FAQ](#faq)
- [Build](#build)
- [Entities](#entities)
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

1. Fill in WiFi credentials and esp32 board in [blekeyboard.yaml](https://github.com/dmamontov/esphome-blekeyboard/blob/main/blekeyboard.yaml)
2. Use [ESPHome](https://esphome.io) to build and upload firmware

## Entities

- Connected (binary_sensor) - Whether the device is connected to the keyboard.
- Delay (sensor) - The last set delay. After rebooting the device is reset to 8ms by default.
- Wifi Signal (sensor) - Wifi signal strength.
- Restart (switch) - Reboots the device.

## Service

**Via GUI (Recommended)**

`Developer-tools` > `Service` > `esphome.blekeyboard_send`

**Via YAML (legacy way)**
```yaml
service: esphome.blekeyboard_send
data:
  message: 'Hello world!' # Message, key name or key combination separated by \+.
  delay_ms: 14 # Delay between clicks in milliseconds
```

## Examples

#### Sending a simple message

```yaml
service: esphome.blekeyboard_send
data:
  message: 'Hello world!'
  delay_ms: 14
```

#### Pressing the ENTER key

```yaml
service: esphome.blekeyboard_send
data:
  message: 'KEY_RETURN'
  delay_ms: 14
```

#### Press CTRL + ALT + DELETE

```yaml
service: esphome.blekeyboard_send
data:
  message: 'KEY_LEFT_CTRL\+KEY_LEFT_ALT\+KEY_DELETE'
  delay_ms: 14
```

#### Press CTRL + A

```yaml
service: esphome.blekeyboard_send
data:
  message: 'KEY_LEFT_CTRL\+a'
  delay_ms: 14
```

## Keys

[List of keys that are supported](https://github.com/dmamontov/esphome-blekeyboard/blob/main/inc/keymap.h)
