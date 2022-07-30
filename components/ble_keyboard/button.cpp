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
            } else if (int_value_ > 0) {
                parent_->press(int_value_);
            } else if (media_value_first_ > 0 || media_value_two_ > 0) {
                MediaKeyReport mediaKey = {media_value_first_, media_value_two_};

                parent_->press(mediaKey);
            } else {
                parent_->release();
            }
        }
    }
}

#endif