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
  switch (type_) {
    case 0:
      parent_->set_delay((uint32_t) value);
      break;
    case 1:
      parent_->set_release_delay((uint32_t) value);
      break;
    case 2:
      parent_->set_battery_level((uint8_t) value);
      break;
  }

  this->publish_state(value);
  this->pref_.save(&value);
}
}  // namespace ble_keyboard
}  // namespace esphome

#endif