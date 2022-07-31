#pragma once

#ifdef USE_ESP32

#include "esphome/core/component.h"
#include "esphome/components/button/button.h"
#include "ble_keyboard.h"
#include <string>

namespace esphome {
namespace ble_keyboard {
class Esp32BleKeyboardButton : public button::Button, public Component {
 public:
  void set_parent(Esp32BleKeyboard *parent) { parent_ = parent; }

  void set_value(std::string value) { text_value_ = value; }
  void set_value(int8_t first_value, int8_t second_value = -1) {
    first_value_ = first_value;
    second_value_ = second_value;
  }

 protected:
  void press_action() override;

  std::string text_value_{""};
  int8_t first_value_{-1};
  int8_t second_value_{-1};

  Esp32BleKeyboard *parent_;
};
}  // namespace ble_keyboard
}  // namespace esphome

#endif