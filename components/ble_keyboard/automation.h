#pragma once

#ifdef USE_ESP32

#include "esphome/core/component.h"
#include "esphome/core/automation.h"
#include "ble_keyboard.h"
#include <string>

namespace esphome {
namespace ble_keyboard {
template<typename... Ts> class Esp32BleKeyboardPrintAction : public Action<Ts...> {
 public:
  explicit Esp32BleKeyboardPrintAction(Esp32BleKeyboard *ble_keyboard) : ble_keyboard_(ble_keyboard) {}
  TEMPLATABLE_VALUE(std::string, text)

  void play(Ts... x) override { this->ble_keyboard_->press(this->text_.value(x...)); }

 protected:
  Esp32BleKeyboard *ble_keyboard_;
};

template<typename... Ts> class Esp32BleKeyboardPressAction : public Action<Ts...> {
 public:
  explicit Esp32BleKeyboardPressAction(Esp32BleKeyboard *ble_keyboard) : ble_keyboard_(ble_keyboard) {}
  TEMPLATABLE_VALUE(uint8_t, code)

  void play(Ts... x) override {
    if (keys_.size() > 1) {
      MediaKeyReport mediaKey = {keys_[0], keys_[1]};

      this->ble_keyboard_->press(mediaKey);
    } else {
      this->ble_keyboard_->press(this->code_.value(x...));
    }
  }

  void set_keys(const std::vector<uint8_t> &keys) { keys_ = keys; }

 protected:
  std::vector<uint8_t> keys_;
  Esp32BleKeyboard *ble_keyboard_;
};

template<typename... Ts> class Esp32BleKeyboardReleaseAction : public Action<Ts...> {
 public:
  explicit Esp32BleKeyboardReleaseAction(Esp32BleKeyboard *ble_keyboard) : ble_keyboard_(ble_keyboard) {}

  void play(Ts... x) override { this->ble_keyboard_->release(); }

 protected:
  Esp32BleKeyboard *ble_keyboard_;
};

template<typename... Ts> class Esp32BleKeyboardCombinationAction : public Action<Ts...> {
 public:
  explicit Esp32BleKeyboardCombinationAction(Esp32BleKeyboard *ble_keyboard) : ble_keyboard_(ble_keyboard) {}
  TEMPLATABLE_VALUE(uint32_t, delay)

  void play(Ts... x) override {
    uint32_t delay_ms = this->delay_.value(x...);

    for (std::string &key : keys_) {
      if (this->is_number(key)) {
        this->ble_keyboard_->press((uint8_t) atoi(key.c_str()), false);
      } else {
        this->ble_keyboard_->press(key);
      }

      delay(delay_ms);
    }

    this->ble_keyboard_->release();
  }

  void set_keys(const std::vector<std::string> &keys) { keys_ = keys; }

 protected:
  std::vector<std::string> keys_;
  Esp32BleKeyboard *ble_keyboard_;

 private:
  bool is_number(const std::string &s) {
    return !s.empty() && std::find_if(s.begin(), s.end(), [](unsigned char c) { return !std::isdigit(c); }) == s.end();
  }
};
}  // namespace ble_keyboard
}  // namespace esphome

#endif