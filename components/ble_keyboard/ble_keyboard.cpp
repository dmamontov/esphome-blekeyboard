#ifdef USE_ESP32

#include "ble_keyboard.h"
#include "esphome/core/log.h"
#include <string>

namespace esphome {
namespace ble_keyboard {
static const char *const TAG = "ble_keyboard";

void Esp32BleKeyboard::setup() {
  ESP_LOGI(TAG, "Setting up...");

  bleKeyboard.begin();
  bleKeyboard.releaseAll();
}

void Esp32BleKeyboard::update() { state_sensor_->publish_state(bleKeyboard.isConnected()); }

bool Esp32BleKeyboard::is_connected() {
  if (!bleKeyboard.isConnected()) {
    ESP_LOGI(TAG, "Disconnected");

    return false;
  }

  return true;
}

void Esp32BleKeyboard::update_timer() {
  this->cancel_timeout((const std::string) TAG);
  this->set_timeout((const std::string) TAG, release_delay_, [this]() { this->release(); });
}

void Esp32BleKeyboard::press(std::string message) {
  if (this->is_connected()) {
    if (message.length() >= 5) {
      for (unsigned i = 0; i < message.length(); i += 5) {
        bleKeyboard.print(message.substr(i, 5).c_str());

        delay(default_delay_);
      }

      return;
    }

    bleKeyboard.print(message.c_str());
  }
}

void Esp32BleKeyboard::press(uint8_t key, bool with_timer) {
  if (this->is_connected()) {
    if (with_timer) {
      this->update_timer();
    }

    bleKeyboard.press(key);
  }
}

void Esp32BleKeyboard::press(MediaKeyReport key, bool with_timer) {
  if (this->is_connected()) {
    if (with_timer) {
      this->update_timer();
    }
    bleKeyboard.press(key);
  }
}

void Esp32BleKeyboard::release() {
  if (this->is_connected()) {
    this->cancel_timeout((const std::string) TAG);
    bleKeyboard.releaseAll();
  }
}
}  // namespace ble_keyboard
}  // namespace esphome

#endif