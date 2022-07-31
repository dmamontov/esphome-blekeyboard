#pragma once

#ifdef USE_ESP32

#include "esphome/core/component.h"
#include "esphome/core/preferences.h"
#include "esphome/components/number/number.h"
#include "ble_keyboard.h"

namespace esphome {
namespace ble_keyboard {
class Esp32BleKeyboardNumber : public number::Number, public Component {
 public:
  void setup() override;

  float get_setup_priority() const override { return setup_priority::AFTER_BLUETOOTH; }

  void set_initial_value(float initial_value) { initial_value_ = initial_value; }
  void set_parent(Esp32BleKeyboard *parent) { parent_ = parent; }
  void enable_press() { is_press_ = true; }

 protected:
  void control(float value) override;

  float initial_value_{NAN};
  bool is_press_{false};

  Esp32BleKeyboard *parent_;
  ESPPreferenceObject pref_;
};
}  // namespace ble_keyboard
}  // namespace esphome

#endif