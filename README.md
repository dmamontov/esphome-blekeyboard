# ESPHome BLE Keyboard
[![CodeQL](https://img.shields.io/badge/CODEQL-Passing-30C854.svg?style=for-the-badge)](https://github.com/dmamontov/hass-miwifi/actions?query=CodeQL)
[![Telegram](https://img.shields.io/badge/Telegram-channel-34ABDF.svg?style=for-the-badge)](https://t.me/hass_mamontov_tech)

Custom [esphome](https://esphome.io/) component to implement a virtual BLE keyboard.

## More info

- [Base configuration](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration)
  - [Adding a component](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#adding-a-component)
  - [Configuration](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#configuration)
  - [Actions](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#actions)
    - [ble_keyboard.print](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardprint)
    - [ble_keyboard.press](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardpress)
    - [ble_keyboard.release](https://github.com/dmamontov/esphome-blekeyboard/wiki/Base-configuration#ble_keyboardrelease)
- [Supported OS](https://github.com/dmamontov/esphome-blekeyboard/wiki/Supported-OS)
- [Keys](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys)
  - [Default](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys#default)
  - [Media](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys#media)
- [Entities](https://github.com/dmamontov/esphome-blekeyboard/wiki/Entities)
- [Example](blekeyboard.yaml)

## Supported OS
| OS      | Description             |
|---------|-------------------------|
| Windows | Fully supported         |
| Linux   | Fully supported         |
| Android | Fully supported         |
| MacOS   | It does not work stably |
| IOS     | It does not work stably |

## Base configuration

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
```

* **id** (Optional, string): Component ID. Needed for action;
* **name** (Optional, string): Keyboard name (default: Esp32BleKeyboard);
* **manufacturer_id** (Optional, string): Keyboard manufacturer (default: Esp32BleKeyboard);
* **battery_level** (Optional, int): Keyboard battery level (default: 100).

### Actions

#### ble_keyboard.print

Print arbitrary text.

```yaml
ble_keyboard.print:
  id: my_ble_keyboard 
  text: "hello"
```

* **id** (Required, string): Component ID;
* **text** (Required, string): The text to be printed.

#### ble_keyboard.press

Press a key.

```yaml
ble_keyboard.press:
  id: my_ble_keyboard 
  code: 0x80
```

* **id** (Required, string): Component ID;
* **code** (Required, int): [Key code](https://github.com/dmamontov/esphome-blekeyboard/wiki/Keys).

#### ble_keyboard.release

Release keys.

```yaml
ble_keyboard.release: my_ble_keyboard
```

* **id** (Required, string): Component ID;
