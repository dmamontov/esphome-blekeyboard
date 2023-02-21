"""BleKeyboard component const."""

# pylint: disable=line-too-long

from __future__ import annotations

from typing import Final

import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.components.number import NumberMode
from esphome.const import (
    CONF_DEVICE_CLASS,
    CONF_DISABLED_BY_DEFAULT,
    CONF_ENTITY_CATEGORY,
    CONF_ICON,
    CONF_ID,
    CONF_INITIAL_VALUE,
    CONF_MAX_VALUE,
    CONF_MIN_VALUE,
    CONF_MODE,
    CONF_NAME,
    CONF_OPTIMISTIC,
    CONF_RESTORE_VALUE,
    CONF_STEP,
    CONF_TYPE,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_VALUE,
    DEVICE_CLASS_CONNECTIVITY,
    ENTITY_CATEGORY_CONFIG,
    UNIT_MILLISECOND,
    UNIT_PERCENT,
)

DOMAIN: Final = "ble_keyboard"

CONF_TEXT: Final = "text"
CONF_KEYS: Final = "keys"
CONF_RECONNECT: Final = "reconnect"
CONF_BUTTONS: Final = "buttons"
CONF_USE_DEFAULT_LIBS: Final = "use_default_libs"

COMPONENT_CLASS: Final = "Esp32BleKeyboard"
COMPONENT_NUMBER_CLASS: Final = "Esp32BleKeyboardNumber"
COMPONENT_BUTTON_CLASS: Final = "Esp32BleKeyboardButton"

ACTION_START_CLASS: Final = "Esp32BleKeyboardStartAction"
ACTION_STOP_CLASS: Final = "Esp32BleKeyboardStopAction"
ACTION_PRINT_CLASS: Final = "Esp32BleKeyboardPrintAction"
ACTION_PRESS_CLASS: Final = "Esp32BleKeyboardPressAction"
ACTION_RELEASE_CLASS: Final = "Esp32BleKeyboardReleaseAction"
ACTION_COMBINATION_CLASS: Final = "Esp32BleKeyboardCombinationAction"

"""Libraries"""
LIBS_DEFAULT: Final = [
    ("ESP32 BLE Arduino", "1.0.2", None),
]

LIBS_ADDITIONAL: Final = [
    (
        "h2zero/NimBLE-Arduino",
        "1.4.0",
        None,
    ),
    (
        "t-vk/ESP32 BLE Keyboard",
        "0.3.2",
        None,
    ),
]

BUILD_FLAGS: Final = "-D USE_NIMBLE"

"""Binary sensors"""
BINARY_SENSOR_STATE: Final = {
    CONF_ID: cv.declare_id(binary_sensor.BinarySensor)("connected"),
    CONF_NAME: "Connected",
    CONF_DEVICE_CLASS: DEVICE_CLASS_CONNECTIVITY,
    CONF_DISABLED_BY_DEFAULT: False,
}

"""Numbers"""
TYPE_PRESS: Final = 0
TYPE_RELEASE: Final = 1
TYPE_BATTERY_LEVEL: Final = 2

NUMBERS: Final = [
    {
        CONF_ID: "press_delay",
        CONF_NAME: "Delay press",
        CONF_TYPE: TYPE_PRESS,
        CONF_DISABLED_BY_DEFAULT: False,
        CONF_OPTIMISTIC: True,
        CONF_MIN_VALUE: 1.0,
        CONF_MAX_VALUE: 60000.0,
        CONF_STEP: 1.0,
        CONF_UNIT_OF_MEASUREMENT: UNIT_MILLISECOND,
        CONF_RESTORE_VALUE: True,
        CONF_INITIAL_VALUE: 8.0,
        CONF_MODE: NumberMode.NUMBER_MODE_AUTO,
        CONF_ENTITY_CATEGORY: cv.entity_category(ENTITY_CATEGORY_CONFIG),
    },
    {
        CONF_ID: "release_delay",
        CONF_NAME: "Delay release",
        CONF_TYPE: TYPE_RELEASE,
        CONF_DISABLED_BY_DEFAULT: False,
        CONF_OPTIMISTIC: True,
        CONF_MIN_VALUE: 1.0,
        CONF_MAX_VALUE: 60000.0,
        CONF_STEP: 1.0,
        CONF_UNIT_OF_MEASUREMENT: UNIT_MILLISECOND,
        CONF_RESTORE_VALUE: True,
        CONF_INITIAL_VALUE: 8.0,
        CONF_MODE: NumberMode.NUMBER_MODE_AUTO,
        CONF_ENTITY_CATEGORY: cv.entity_category(ENTITY_CATEGORY_CONFIG),
    },
    {
        CONF_ID: "battery_level",
        CONF_NAME: "Battery level",
        CONF_ICON: "mdi:battery-bluetooth",
        CONF_TYPE: TYPE_BATTERY_LEVEL,
        CONF_DISABLED_BY_DEFAULT: False,
        CONF_OPTIMISTIC: True,
        CONF_MIN_VALUE: 1.0,
        CONF_MAX_VALUE: 100.0,
        CONF_STEP: 1.0,
        CONF_UNIT_OF_MEASUREMENT: UNIT_PERCENT,
        CONF_RESTORE_VALUE: True,
        CONF_INITIAL_VALUE: 100.0,
        CONF_MODE: NumberMode.NUMBER_MODE_AUTO,
        CONF_ENTITY_CATEGORY: cv.entity_category(ENTITY_CATEGORY_CONFIG),
    },
]

"""Buttons"""
BUTTONS_KEY: Final = [
    {
        CONF_NAME: "Space",
        CONF_ID: "key_space",
        CONF_ICON: "mdi:keyboard-space",
        CONF_VALUE: " ",
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left CTRL",
        CONF_ID: "key_left_ctrl",
        CONF_ICON: "mdi:apple-keyboard-control",
        CONF_VALUE: 0x80,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left SHIFT",
        CONF_ID: "key_left_shift",
        CONF_ICON: "mdi:apple-keyboard-shift",
        CONF_VALUE: 0x81,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left ALT",
        CONF_ID: "key_left_alt",
        CONF_ICON: "mdi:apple-keyboard-option",
        CONF_VALUE: 0x82,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left GUI",
        CONF_ID: "key_left_gui",
        CONF_ICON: "mdi:microsoft-windows",
        CONF_VALUE: 0x83,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right CTRL",
        CONF_ID: "key_right_ctrl",
        CONF_ICON: "mdi:apple-keyboard-control",
        CONF_VALUE: 0x84,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right SHIFT",
        CONF_ID: "key_right_shift",
        CONF_ICON: "mdi:apple-keyboard-shift",
        CONF_VALUE: 0x85,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right ALT",
        CONF_ID: "key_right_alt",
        CONF_ICON: "mdi:apple-keyboard-option",
        CONF_VALUE: 0x86,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right GUI",
        CONF_ID: "key_right_gui",
        CONF_ICON: "mdi:microsoft-windows",
        CONF_VALUE: 0x87,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Up arrow",
        CONF_ID: "key_up_arrow",
        CONF_ICON: "mdi:chevron-up",
        CONF_VALUE: 0xDA,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Down arrow",
        CONF_ID: "key_down_arrow",
        CONF_ICON: "mdi:chevron-down",
        CONF_VALUE: 0xD9,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left arrow",
        CONF_ID: "key_left_arrow",
        CONF_ICON: "mdi:chevron-left",
        CONF_VALUE: 0xD8,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right arrow",
        CONF_ID: "key_right_arrow",
        CONF_ICON: "mdi:chevron-right",
        CONF_VALUE: 0xD7,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Backspace",
        CONF_ID: "key_backspace",
        CONF_ICON: "mdi:keyboard-backspace",
        CONF_VALUE: 0xB2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Tab",
        CONF_ID: "key_tab",
        CONF_ICON: "mdi:keyboard-tab",
        CONF_VALUE: 0xB3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Return",
        CONF_ID: "key_return",
        CONF_ICON: "mdi:keyboard-return",
        CONF_VALUE: 0xB0,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Esc",
        CONF_ID: "key_esc",
        CONF_ICON: "mdi:keyboard-esc",
        CONF_VALUE: 0xB1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Insert",
        CONF_ID: "key_insert",
        CONF_ICON: "mdi:alpha-i-box",
        CONF_VALUE: 0xD1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Print screen",
        CONF_ID: "key_prtsc",
        CONF_ICON: "mdi:alpha-p-box",
        CONF_VALUE: 0xCE,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Delete",
        CONF_ID: "key_delete",
        CONF_ICON: "mdi:alpha-d-box",
        CONF_VALUE: 0xD4,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Page up",
        CONF_ID: "key_page_up",
        CONF_ICON: "mdi:arrow-up-box",
        CONF_VALUE: 0xD3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Page down",
        CONF_ID: "key_page_down",
        CONF_ICON: "mdi:arrow-down-box",
        CONF_VALUE: 0xD6,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Home",
        CONF_ID: "key_home",
        CONF_ICON: "mdi:home",
        CONF_VALUE: 0xD2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "End",
        CONF_ID: "key_end",
        CONF_ICON: "mdi:alpha-e-box",
        CONF_VALUE: 0xD5,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Caps Lock",
        CONF_ID: "key_caps_lock",
        CONF_ICON: "mdi:alpha-c-box",
        CONF_VALUE: 0xC1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F1",
        CONF_ID: "key_f1",
        CONF_ICON: "mdi:keyboard-f1",
        CONF_VALUE: 0xC2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F2",
        CONF_ID: "key_f2",
        CONF_ICON: "mdi:keyboard-f2",
        CONF_VALUE: 0xC3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F3",
        CONF_ID: "key_f3",
        CONF_ICON: "mdi:keyboard-f3",
        CONF_VALUE: 0xC4,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F4",
        CONF_ID: "key_f4",
        CONF_ICON: "mdi:keyboard-f4",
        CONF_VALUE: 0xC5,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F5",
        CONF_ID: "key_f5",
        CONF_ICON: "mdi:keyboard-f5",
        CONF_VALUE: 0xC6,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F6",
        CONF_ID: "key_f6",
        CONF_ICON: "mdi:keyboard-f6",
        CONF_VALUE: 0xC7,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F7",
        CONF_ID: "key_f7",
        CONF_ICON: "mdi:keyboard-f7",
        CONF_VALUE: 0xC8,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F8",
        CONF_ID: "key_f8",
        CONF_ICON: "mdi:keyboard-f8",
        CONF_VALUE: 0xC9,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F9",
        CONF_ID: "key_f9",
        CONF_ICON: "mdi:keyboard-f9",
        CONF_VALUE: 0xCA,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F10",
        CONF_ID: "key_f10",
        CONF_ICON: "mdi:keyboard-f10",
        CONF_VALUE: 0xCB,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F11",
        CONF_ID: "key_f11",
        CONF_ICON: "mdi:keyboard-f11",
        CONF_VALUE: 0xCC,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F12",
        CONF_ID: "key_f12",
        CONF_ICON: "mdi:keyboard-f12",
        CONF_VALUE: 0xCD,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F13",
        CONF_ID: "key_f13",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF0,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F14",
        CONF_ID: "key_f14",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF1,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F15",
        CONF_ID: "key_f15",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF2,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F16",
        CONF_ID: "key_f16",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF3,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F17",
        CONF_ID: "key_f17",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF4,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F18",
        CONF_ID: "key_f18",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF5,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F19",
        CONF_ID: "key_f19",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF6,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F20",
        CONF_ID: "key_f20",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF7,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F21",
        CONF_ID: "key_f21",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF8,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F22",
        CONF_ID: "key_f22",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF9,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F23",
        CONF_ID: "key_f23",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xFA,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F24",
        CONF_ID: "key_f24",
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xFB,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "Num 0",
        CONF_ID: "key_num_0",
        CONF_ICON: "mdi:numeric-0",
        CONF_VALUE: 0xEA,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 1",
        CONF_ID: "key_num_1",
        CONF_ICON: "mdi:numeric-1",
        CONF_VALUE: 0xE1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 2",
        CONF_ID: "key_num_2",
        CONF_ICON: "mdi:numeric-2",
        CONF_VALUE: 0xE2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 3",
        CONF_ID: "key_num_3",
        CONF_ICON: "mdi:numeric-3",
        CONF_VALUE: 0xE3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 4",
        CONF_ID: "key_num_4",
        CONF_ICON: "mdi:numeric-4",
        CONF_VALUE: 0xE4,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 5",
        CONF_ID: "key_num_5",
        CONF_ICON: "mdi:numeric-5",
        CONF_VALUE: 0xE5,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 6",
        CONF_ID: "key_num_6",
        CONF_ICON: "mdi:numeric-6",
        CONF_VALUE: 0xE6,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 7",
        CONF_ID: "key_num_7",
        CONF_ICON: "mdi:numeric-7",
        CONF_VALUE: 0xE7,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 8",
        CONF_ID: "key_num_8",
        CONF_ICON: "mdi:numeric-8",
        CONF_VALUE: 0xE8,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 9",
        CONF_ID: "key_num_9",
        CONF_ICON: "mdi:numeric-9",
        CONF_VALUE: 0xE9,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num slash",
        CONF_ID: "key_num_slash",
        CONF_ICON: "mdi:slash-forward",
        CONF_VALUE: 0xDC,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num asterisk",
        CONF_ID: "key_num_asterisk",
        CONF_ICON: "mdi:asterisk",
        CONF_VALUE: 0xDD,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num minus",
        CONF_ID: "key_num_minus",
        CONF_ICON: "mdi:minus",
        CONF_VALUE: 0xDE,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num plus",
        CONF_ID: "key_num_plus",
        CONF_ICON: "mdi:plus",
        CONF_VALUE: 0xDF,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num enter",
        CONF_ID: "key_num_enter",
        CONF_ICON: "mdi:keyboard-return",
        CONF_VALUE: 0xE0,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num dot",
        CONF_ID: "key_num_dot",
        CONF_ICON: "mdi:circle-small",
        CONF_VALUE: 0xEB,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Scroll lock",
        CONF_ID: "key_scroll_lock",
        CONF_ICON: "mdi:alpha-s-box",
        CONF_VALUE: 0xCF,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num lock",
        CONF_ID: "key_num_lock",
        CONF_ICON: "mdi:alpha-n-box",
        CONF_VALUE: 0xDB,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Next track",
        CONF_ID: "key_media_next_track",
        CONF_ICON: "mdi:skip-next",
        CONF_VALUE: (1, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Previous track",
        CONF_ID: "key_media_previous_track",
        CONF_ICON: "mdi:skip-previous",
        CONF_VALUE: (2, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Stop",
        CONF_ID: "key_media_stop",
        CONF_ICON: "mdi:stop",
        CONF_VALUE: (4, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Play/Pause",
        CONF_ID: "key_media_play_pause",
        CONF_ICON: "mdi:play-pause",
        CONF_VALUE: (8, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Mute",
        CONF_ID: "key_media_mute",
        CONF_ICON: "mdi:volume-mute",
        CONF_VALUE: (16, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Volume up",
        CONF_ID: "key_media_volume_up",
        CONF_ICON: "mdi:volume-plus",
        CONF_VALUE: (32, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Volume down",
        CONF_ID: "key_media_volume_down",
        CONF_ICON: "mdi:volume-minus",
        CONF_VALUE: (64, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "My computer",
        CONF_ID: "key_media_browser",
        CONF_ICON: "mdi:desktop-classic",
        CONF_VALUE: (0, 1),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Calculator",
        CONF_ID: "key_media_calculator",
        CONF_ICON: "mdi:calculator",
        CONF_VALUE: (0, 2),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "WWW Bookmarks",
        CONF_ID: "key_media_www_bookmarks",
        CONF_ICON: "mdi:bookmark",
        CONF_VALUE: (0, 4),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Search",
        CONF_ID: "key_media_www_search",
        CONF_ICON: "mdi:magnify",
        CONF_VALUE: (0, 8),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Stop",
        CONF_ID: "key_media_www_stop",
        CONF_ICON: "mdi:close",
        CONF_VALUE: (0, 16),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Back",
        CONF_ID: "key_media_www_back",
        CONF_ICON: "mdi:arrow-left",
        CONF_VALUE: (0, 32),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Home",
        CONF_ID: "key_media_www_home",
        CONF_ICON: "mdi:web",
        CONF_VALUE: (128, 0),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "Consumer control configuration",
        CONF_ID: "key_media_consumer_control_configuration",
        CONF_ICON: "mdi:cog",
        CONF_VALUE: (0, 64),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "Email",
        CONF_ID: "key_media_email",
        CONF_ICON: "mdi:email",
        CONF_VALUE: (0, 128),
        CONF_DISABLED_BY_DEFAULT: True,
    },
]
