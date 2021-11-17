#include <BleKeyboard.h>
#include "esphome.h"
#include "string.h"

using namespace std;

#define USE_NIMBLE

class Esp32BLEKeyboard : public PollingComponent {
   private:
    void write_message(const char* message, bool is_combination = false) {
        ESP_LOGD("Esp32BLEKeyboard", "Sending text(%s): %s", is_combination ? "combination" : "plain", message);

        if (strcmp(message, "KEY_LEFT_CTRL") == 0) {
            bleKeyboard.press(KEY_LEFT_CTRL);
        } else if (strcmp(message, "KEY_LEFT_SHIFT") == 0) {
            bleKeyboard.press(KEY_LEFT_SHIFT);
        } else if (strcmp(message, "KEY_LEFT_ALT") == 0) {
            bleKeyboard.press(KEY_LEFT_ALT);
        } else if (strcmp(message, "KEY_LEFT_GUI") == 0) {
            bleKeyboard.press(KEY_LEFT_GUI);
        } else if (strcmp(message, "KEY_RIGHT_CTRL") == 0) {
            bleKeyboard.press(KEY_RIGHT_CTRL);
        } else if (strcmp(message, "KEY_RIGHT_SHIFT") == 0) {
            bleKeyboard.press(KEY_RIGHT_SHIFT);
        } else if (strcmp(message, "KEY_RIGHT_ALT") == 0) {
            bleKeyboard.press(KEY_RIGHT_ALT);
        } else if (strcmp(message, "KEY_RIGHT_GUI") == 0) {
            bleKeyboard.press(KEY_RIGHT_GUI);
        } else if (strcmp(message, "KEY_UP_ARROW") == 0) {
            bleKeyboard.press(KEY_UP_ARROW);
        } else if (strcmp(message, "KEY_DOWN_ARROW") == 0) {
            bleKeyboard.press(KEY_DOWN_ARROW);
        } else if (strcmp(message, "KEY_LEFT_ARROW") == 0) {
            bleKeyboard.press(KEY_LEFT_ARROW);
        } else if (strcmp(message, "KEY_RIGHT_ARROW") == 0) {
            bleKeyboard.press(KEY_RIGHT_ARROW);
        } else if (strcmp(message, "KEY_BACKSPACE") == 0) {
            bleKeyboard.press(KEY_BACKSPACE);
        } else if (strcmp(message, "KEY_TAB") == 0) {
            bleKeyboard.press(KEY_TAB);
        } else if (strcmp(message, "KEY_RETURN") == 0) {
            bleKeyboard.press(KEY_RETURN);
        } else if (strcmp(message, "KEY_ESC") == 0) {
            bleKeyboard.press(KEY_ESC);
        } else if (strcmp(message, "KEY_INSERT") == 0) {
            bleKeyboard.press(KEY_INSERT);
        } else if (strcmp(message, "KEY_DELETE") == 0) {
            bleKeyboard.press(KEY_DELETE);
        } else if (strcmp(message, "KEY_PAGE_UP") == 0) {
            bleKeyboard.press(KEY_PAGE_UP);
        } else if (strcmp(message, "KEY_PAGE_DOWN") == 0) {
            bleKeyboard.press(KEY_PAGE_DOWN);
        } else if (strcmp(message, "KEY_HOME") == 0) {
            bleKeyboard.press(KEY_HOME);
        } else if (strcmp(message, "KEY_END") == 0) {
            bleKeyboard.press(KEY_END);
        } else if (strcmp(message, "KEY_CAPS_LOCK") == 0) {
            bleKeyboard.press(KEY_CAPS_LOCK);
        } else if (strcmp(message, "KEY_F1") == 0) {
            bleKeyboard.press(KEY_F1);
        } else if (strcmp(message, "KEY_F2") == 0) {
            bleKeyboard.press(KEY_F2);
        } else if (strcmp(message, "KEY_F3") == 0) {
            bleKeyboard.press(KEY_F3);
        } else if (strcmp(message, "KEY_F4") == 0) {
            bleKeyboard.press(KEY_F4);
        } else if (strcmp(message, "KEY_F5") == 0) {
            bleKeyboard.press(KEY_F5);
        } else if (strcmp(message, "KEY_F6") == 0) {
            bleKeyboard.press(KEY_F6);
        } else if (strcmp(message, "KEY_F7") == 0) {
            bleKeyboard.press(KEY_F7);
        } else if (strcmp(message, "KEY_F8") == 0) {
            bleKeyboard.press(KEY_F8);
        } else if (strcmp(message, "KEY_F9") == 0) {
            bleKeyboard.press(KEY_F9);
        } else if (strcmp(message, "KEY_F10") == 0) {
            bleKeyboard.press(KEY_F10);
        } else if (strcmp(message, "KEY_F11") == 0) {
            bleKeyboard.press(KEY_F11);
        } else if (strcmp(message, "KEY_F12") == 0) {
            bleKeyboard.press(KEY_F12);
        } else if (strcmp(message, "KEY_F13") == 0) {
            bleKeyboard.press(KEY_F13);
        } else if (strcmp(message, "KEY_F14") == 0) {
            bleKeyboard.press(KEY_F14);
        } else if (strcmp(message, "KEY_F15") == 0) {
            bleKeyboard.press(KEY_F15);
        } else if (strcmp(message, "KEY_F16") == 0) {
            bleKeyboard.press(KEY_F16);
        } else if (strcmp(message, "KEY_F17") == 0) {
            bleKeyboard.press(KEY_F17);
        } else if (strcmp(message, "KEY_F18") == 0) {
            bleKeyboard.press(KEY_F18);
        } else if (strcmp(message, "KEY_F19") == 0) {
            bleKeyboard.press(KEY_F19);
        } else if (strcmp(message, "KEY_F20") == 0) {
            bleKeyboard.press(KEY_F20);
        } else if (strcmp(message, "KEY_F21") == 0) {
            bleKeyboard.press(KEY_F21);
        } else if (strcmp(message, "KEY_F22") == 0) {
            bleKeyboard.press(KEY_F22);
        } else if (strcmp(message, "KEY_F23") == 0) {
            bleKeyboard.press(KEY_F23);
        } else if (strcmp(message, "KEY_F24") == 0) {
            bleKeyboard.press(KEY_F24);
        } else if (strcmp(message, "KEY_MEDIA_NEXT_TRACK") == 0) {
            bleKeyboard.press(KEY_MEDIA_NEXT_TRACK);
        } else if (strcmp(message, "KEY_MEDIA_PREVIOUS_TRACK") == 0) {
            bleKeyboard.press(KEY_MEDIA_PREVIOUS_TRACK);
        } else if (strcmp(message, "KEY_MEDIA_STOP") == 0) {
            bleKeyboard.press(KEY_MEDIA_STOP);
        } else if (strcmp(message, "KEY_MEDIA_PLAY_PAUSE") == 0) {
            bleKeyboard.press(KEY_MEDIA_PLAY_PAUSE);
        } else if (strcmp(message, "KEY_MEDIA_MUTE") == 0) {
            bleKeyboard.press(KEY_MEDIA_MUTE);
        } else if (strcmp(message, "KEY_MEDIA_VOLUME_UP") == 0) {
            bleKeyboard.press(KEY_MEDIA_VOLUME_UP);
        } else if (strcmp(message, "KEY_MEDIA_VOLUME_DOWN") == 0) {
            bleKeyboard.press(KEY_MEDIA_VOLUME_DOWN);
        } else if (strcmp(message, "KEY_MEDIA_WWW_HOME") == 0) {
            bleKeyboard.press(KEY_MEDIA_WWW_HOME);
        } else if (strcmp(message, "KEY_MEDIA_LOCAL_MACHINE_BROWSER") == 0) {
            bleKeyboard.press(KEY_MEDIA_LOCAL_MACHINE_BROWSER);
        } else if (strcmp(message, "KEY_MEDIA_CALCULATOR") == 0) {
            bleKeyboard.press(KEY_MEDIA_CALCULATOR);
        } else if (strcmp(message, "KEY_MEDIA_WWW_BOOKMARKS") == 0) {
            bleKeyboard.press(KEY_MEDIA_WWW_BOOKMARKS);
        } else if (strcmp(message, "KEY_MEDIA_WWW_SEARCH") == 0) {
            bleKeyboard.press(KEY_MEDIA_WWW_SEARCH);
        } else if (strcmp(message, "KEY_MEDIA_WWW_STOP") == 0) {
            bleKeyboard.press(KEY_MEDIA_WWW_STOP);
        } else if (strcmp(message, "KEY_MEDIA_WWW_BACK") == 0) {
            bleKeyboard.press(KEY_MEDIA_WWW_BACK);
        } else if (strcmp(message, "KEY_MEDIA_CONSUMER_CONTROL_CONFIGURATION") == 0) {
            bleKeyboard.press(KEY_MEDIA_CONSUMER_CONTROL_CONFIGURATION);
        } else if (strcmp(message, "KEY_MEDIA_EMAIL_READER") == 0) {
            bleKeyboard.press(KEY_MEDIA_EMAIL_READER);
        } else if (is_combination == true) {
            if (strlen(message) == 1) {
                bleKeyboard.press((uint8_t)atoi(message));
            }
        } else {
            bleKeyboard.print(message);
        }
    }

   public:
    BleKeyboard bleKeyboard;
    BinarySensor *connected_binarysensor = new BinarySensor();
    Sensor *delay_sensor = new Sensor();

    Esp32BLEKeyboard(std::string name, std::string manufacturer) : PollingComponent(1000), bleKeyboard(name, manufacturer, 100) {}

    void setup() override {
        ESP_LOGD("Esp32BLEKeyboard", "Setting up BLE Keyboard...");
        bleKeyboard.begin();
        bleKeyboard.releaseAll();

        delay_sensor->publish_state(8);
    }

    void update() override {
        connected_binarysensor->publish_state(bleKeyboard.isConnected());
    }

    void send_message(const char* message, bool is_combination = false, uint32_t delay_ms = 8) {
        ESP_LOGD("Esp32BLEKeyboard", "Set delay: %d", delay_ms);

        bleKeyboard.setDelay(delay_ms);
        delay_sensor->publish_state(delay_ms);

        if (is_combination) {
            char *buff[] = {(char*) message};
            char * position = strtok(buff[0], "+");

            while (position != 0) {
                write_message(p, true);
                position = strtok(NULL, "+");
            }

            delay(100);
        } else {
            write_message(message);
        }

        if (std::string(message).find("KEY_") != std::string::npos) {
            bleKeyboard.releaseAll();
        }
    }
};