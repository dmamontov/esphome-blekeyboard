# ESPHome BLE Keyboard
[![CodeQL](https://img.shields.io/badge/CODEQL-Passing-30C854.svg?style=for-the-badge)](https://github.com/dmamontov/hass-miwifi/actions?query=CodeQL)
[![Telegram](https://img.shields.io/badge/Telegram-channel-34ABDF.svg?style=for-the-badge)](https://t.me/hass_mamontov_tech)

Custom [esphome](https://esphome.io/) component to implement a virtual BLE keyboard.

## More info

- [Base configuration](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration)
  - [Requirements](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#requirements)
  - [Adding a component](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#adding-a-component)
  - [Configuration](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#configuration)
  - [Actions](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#actions)
    - [ble_keyboard.print](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardprint)
    - [ble_keyboard.press](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardpress)
    - [ble_keyboard.release](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardrelease)
    - [ble_keyboard.combination](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardcombination)
    - [ble_keyboard.start](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardstart)
    - [ble_keyboard.stop](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardstop)
- [Supported OS](https://github.com/dmamontov/esphome-blekeyboard/wiki/Supported-OS)
- [Keys](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys)
  - [Default](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys#default)
  - [Media](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys#media)
- [Entities](https://github.com/dmamontov/esphome-blekeyboard/wiki/Entities)
- [Cookbook](https://github.com/dmamontov/esphome-blekeyboard/wiki/Cookbook)
  - [Sending a simple message](https://github.com/dmamontov/esphome-blekeyboard/wiki/Cookbook#sending-a-simple-message)
  - [Pressing the ENTER key](https://github.com/dmamontov/esphome-blekeyboard/wiki/Cookbook#pressing-the-enter-key)
  - [Press CTRL + ALT + DELETE](https://github.com/dmamontov/esphome-blekeyboard/wiki/Cookbook#press-ctrl--alt--delete)
  - [Press CTRL + A](https://github.com/dmamontov/esphome-blekeyboard/wiki/Cookbook#press-ctrl--a)
  - [Lock an iPad](https://github.com/dmamontov/esphome-blekeyboard/wiki/Cookbook#lock-an-ipad)
- [Examples](examples)
  - [esp32](examples/esp32.yaml)
  - [esp32c3](examples/esp32c3.yaml)
- [Credits](https://github.com/dmamontov/esphome-blekeyboard/wiki/Credits)

## Supported OS
| OS      | Description             |
|---------|-------------------------|
| Windows | Fully supported         |
| Linux   | Fully supported         |
| Android | Fully supported         |
| MacOS   | It does not work stably |
| IOS     | It does not work stably |

## Base configuration

### Requirements
* **Board**: esp32, esp32s2, esp32s3, esp32c3 and esp32h2;
* **Framework**: arduino.

### Adding a component

```yaml
external_components:
  - source: github://dmamontov/esphome-blekeyboard
```

### Configuration

```yaml
ble_keyboard:
  id: mamontech_keyboard
  name: "MamonTechKeyboard"
  manufacturer_id: "MamonTech"
  battery_level: 50
  reconnect: true
  buttons: true
  use_default_libs: false
```

* **id** (Optional, string): Component ID. Needed for action;
* **name** (Optional, string): Keyboard name (default: Esp32BleKeyboard);
* **manufacturer_id** (Optional, string): Keyboard manufacturer (default: Esp32BleKeyboard);
* **battery_level** (Optional, int): Keyboard battery level (default: 100);
* **reconnect** (Optional, bool): Automatic reconnect service after disconnecting the device. (default: true);
* **buttons** (Optional, bool): Whether to add separate buttons for [keys](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys) (default: true);
* **use_default_libs** (Optional, bool): Whether to use the arduino standard library. (default: false).

### Actions

#### ble_keyboard.print

Print arbitrary text.

```yaml
ble_keyboard.print:
  id: my_ble_keyboard 
  text: "hello"
```

* **id** (Required, string): Component ID;
* **text** (Required, string): The text to be printed. Supports lambda.

#### ble_keyboard.press

Press a key.

```yaml
ble_keyboard.press:
  id: my_ble_keyboard 
  code: 0x80
```

For media keys:
```yaml
ble_keyboard.press:
  id: my_ble_keyboard 
  code:
    - 0
    - 1
```

* **id** (Required, string): Component ID;
* **code** (Required, int|list[int]): [Key code](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys). Supports lambda for int only.

#### ble_keyboard.release

Release all keys.

```yaml
ble_keyboard.release: 
  id: my_ble_keyboard
```

Release a specific Key
```yaml
ble_keyboard.release
  id: my_ble_keyboard
  code: 0x80
```

Release a specific media Key
```yaml
ble_keyboard.release
  id: my_ble_keyboard
  code: 
    - 0
    - 1
```

#### ble_keyboard.combination

Press a key combination.

```yaml
ble_keyboard.combination:
  id: my_ble_keyboard
  delay: 8
  keys:
    - 0x80 # Left CTRL
    - "a"
```

* **id** (Required, string): Component ID;
* **delay** (Required, int): Delay between clicks. Supports lambda;
* **keys** (Required, list[int, string]): [Key list](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys). Doesn't support lambda.

#### ble_keyboard.start

Start advertising.

```yaml
ble_keyboard.start: my_ble_keyboard
```

#### ble_keyboard.stop

Stop advertising and disable customers.

```yaml
ble_keyboard.stop: my_ble_keyboard
```

## Credits
* Thanks to all [ESPHome](https://github.com/esphome/esphome) contributors;
* Thanks to [@T-vK](https://github.com/T-vK) for the [ESP32-BLE-Keyboard](https://github.com/T-vK/ESP32-BLE-Keyboard) library;
* Thanks to [@h2zero](https://github.com/h2zero) for the [NimBLE-Arduino](https://github.com/h2zero/NimBLE-Arduino) library.