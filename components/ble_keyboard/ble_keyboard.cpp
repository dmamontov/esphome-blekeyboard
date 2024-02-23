#ifdef USE_ESP32

#include "ble_keyboard.h"
#include "esphome/core/log.h"
#include <NimBLEServer.h>
#include <NimBLEDevice.h>
#include <NimBLEService.h>
#include <NimBLECharacteristic.h>
#include <NimBLEAdvertising.h>
#include <string>
#include <list>

namespace esphome {
namespace ble_keyboard {
static const char *const TAG = "ble_keyboard";

void Esp32BleKeyboard::setup() {
  if (this->setup_) {
    ESP_LOGW(TAG, "BLE keyboard already setup.");
    return;
  }

  ESP_LOGCONFIG(TAG, "Setting up BLE keyboard...");

  bleKeyboard.begin();

  pServer = BLEDevice::getServer();

  ESP_LOGCONFIG(TAG, "advertiseOnDisconnect(%s)", this->reconnect_ ? "true" : "false");
  pServer->advertiseOnDisconnect(this->reconnect_);

  if (!this->advertise_on_start_) {
    ESP_LOGCONFIG(TAG, "stopAdvertising() because advertise_on_start is false");
    pServer->stopAdvertising();
  }

  bleKeyboard.releaseAll();
  this->setup_ = true;
  ESP_LOGCONFIG(TAG, "Finished setting up up BLE keyboard.");
}

void Esp32BleKeyboard::stop() {
  if (!this->setup_) {
    ESP_LOGW(TAG, "Attempting to use without setup.  Not doing anything.");
    return;
  }

  ESP_LOGD(TAG, "stop()");
  if (this->reconnect_) {
    ESP_LOGD(TAG, "advertiseOnDisconnect(false)");
    pServer->advertiseOnDisconnect(false);
  }

  std::vector<uint16_t> ids = pServer->getPeerDevices();

  if (ids.size() > 0) {
    for (uint16_t &id : ids) {
      pServer->disconnect(id);
    }
  } else {
    pServer->stopAdvertising();
  }
}

void Esp32BleKeyboard::start() {
  if (!this->setup_) {
    ESP_LOGW(TAG, "Attempting to use without setup.  Not doing anything.");
    return;
  }
  ESP_LOGD(TAG, "start()");
  if (this->reconnect_) {
    ESP_LOGD(TAG, "advertiseOnDisconnect(true)");
    pServer->advertiseOnDisconnect(true);
  }

  pServer->startAdvertising();
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
  if (!this->setup_) {
    ESP_LOGW(TAG, "Attempting to use without setup.  Not doing anything.");
    return;
  }
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
  if (!this->setup_) {
    ESP_LOGW(TAG, "Attempting to use without setup.  Not doing anything.");
    return;
  }
  if (this->is_connected()) {
    if (with_timer) {
      this->update_timer();
    }

    bleKeyboard.press(key);
  }
}

void Esp32BleKeyboard::press(MediaKeyReport key, bool with_timer) {
  if (!this->setup_) {
    ESP_LOGW(TAG, "Attempting to use without setup.  Not doing anything.");
    return;
  }
  if (this->is_connected()) {
    if (with_timer) {
      this->update_timer();
    }
    bleKeyboard.press(key);
  }
}

void Esp32BleKeyboard::release() {
  if (!this->setup_) {
    ESP_LOGW(TAG, "Attempting to use without setup.  Not doing anything.");
    return;
  }
  if (this->is_connected()) {
    this->cancel_timeout((const std::string) TAG);
    bleKeyboard.releaseAll();
  }
}
}  // namespace ble_keyboard
}  // namespace esphome

#endif
