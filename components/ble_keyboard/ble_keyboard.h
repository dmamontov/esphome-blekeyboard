#pragma once

#ifdef USE_ESP32

#include "esphome/core/component.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include <BleKeyboard.h>
#include <string>

namespace esphome {
namespace ble_keyboard {
class Esp32BleKeyboard : public PollingComponent {
 public:
  Esp32BleKeyboard(std::string name, std::string manufacturer_id, uint8_t battery_level)
      : PollingComponent(1000), bleKeyboard(name, manufacturer_id, battery_level) {}

  void setup() override;
  void update() override;

  float get_setup_priority() const override { return setup_priority::AFTER_BLUETOOTH; }

  void set_delay(uint32_t delay_ms);
  void set_release_delay(uint32_t delay_ms) { release_delay_ = delay_ms; };
  void set_state_sensor(binary_sensor::BinarySensor *state_sensor) { state_sensor_ = state_sensor; }

  void press(std::string message);
  void press(uint8_t key);
  void press(MediaKeyReport key);
  void release();

 protected:
  binary_sensor::BinarySensor *state_sensor_;

 private:
  bool is_connected();
  void update_timer();

  BleKeyboard bleKeyboard;
  uint32_t default_delay_{100};
  uint32_t release_delay_{8};
};
}  // namespace ble_keyboard
}  // namespace esphome

#endif