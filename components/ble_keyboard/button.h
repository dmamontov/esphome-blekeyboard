#pragma once

#ifdef USE_ESP32

#include "esphome/core/component.h"
#include "esphome/components/button/button.h"
#include "ble_keyboard.h"
#include <string>

namespace esphome {
    namespace ble_keyboard {
        class Esp32BleKeyboardButton : public button::Button, public Component {
            public:
                void set_parent(Esp32BleKeyboard *parent) { parent_ = parent; }

                void set_text_value(std::string text_value) { text_value_ = text_value; }
                void set_int_value(uint8_t int_value) { int_value_ = int_value; }
                void set_media_value(uint8_t first_value, uint8_t two_value) {
                    media_value_first_ = first_value;
                    media_value_two_ = two_value;
                }

            protected:
                void press_action() override;

                std::string text_value_{""};
                uint8_t int_value_{0};
                uint8_t media_value_first_{0};
                uint8_t media_value_two_{0};

                Esp32BleKeyboard *parent_;
        };
    }
}

#endif