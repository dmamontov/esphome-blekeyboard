#ifdef USE_ESP32

#include "number.h"
#include "esphome/core/log.h"

namespace esphome {
namespace ble_keyboard {
static const char *const TAG = "ble_keyboard";

void Esp32BleKeyboardNumber::setup() {
  float value;

  this->pref_ = global_preferences->make_preference<float>(this->get_object_id_hash());
  if (!this->pref_.load(&value)) {
    if (!std::isnan(this->initial_value_)) {
      value = this->initial_value_;
    }
  }

  this->publish_state(value);
}

void Esp32BleKeyboardNumber::control(float value) {
  if (is_press_) {
    parent_->set_delay((uint32_t) value);
  } else {
    parent_->set_release_delay((uint32_t) value);
  }

  this->publish_state(value);
  this->pref_.save(&value);
}
}  // namespace ble_keyboard
}  // namespace esphome

#endif