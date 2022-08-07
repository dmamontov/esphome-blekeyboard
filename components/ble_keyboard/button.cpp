#ifdef USE_ESP32

#include "button.h"
#include "esphome/core/log.h"
#include <string>

namespace esphome {
namespace ble_keyboard {
static const char *const TAG = "ble_keyboard";

void Esp32BleKeyboardButton::press_action() {
  if (text_value_.length() > 0) {
    parent_->press(text_value_);
  } else if (first_value_ != -1 && second_value_ != -1) {
    MediaKeyReport mediaKey = {(uint8_t) first_value_, (uint8_t) second_value_};

    parent_->press(mediaKey);
  } else if (first_value_ != -1) {
    parent_->press((uint8_t) first_value_);
  } else {
    parent_->release();
  }
}
}  // namespace ble_keyboard
}  // namespace esphome

#endif