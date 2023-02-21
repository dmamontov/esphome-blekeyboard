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
  ESP_LOGI(TAG, "Setting up...");

  bleKeyboard.begin();

  pServer = BLEDevice::getServer();

  pServer->advertiseOnDisconnect(this->reconnect_);

  bleKeyboard.releaseAll();
}

void Esp32BleKeyboard::stop() {
  if (this->reconnect_) {
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
  if (this->reconnect_) {
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

void Esp32BleKeyboard::release(uint8_t key) {
  if(this->is_connected()) {
    this->cancel_timeout((const std::string) TAG);
    bleKeyboard.release(key);
  }
}

void Esp32BleKeyboard::release(MediaKeyReport key) {
  if(this->is_connected()) {
    this->cancel_timeout((const std::string) TAG);
    bleKeyboard.release(key);
  }
}

}  // namespace ble_keyboard
}  // namespace esphome

#endif