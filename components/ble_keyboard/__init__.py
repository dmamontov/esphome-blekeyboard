import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.automation import maybe_simple_id
from esphome.components import binary_sensor, button, number
from esphome.components.number import NumberMode
from esphome.const import (
    CONF_BATTERY_LEVEL,
    CONF_DEVICE_CLASS,
    CONF_DISABLED_BY_DEFAULT,
    CONF_ENTITY_CATEGORY,
    CONF_ICON,
    CONF_ID,
    CONF_INITIAL_VALUE,
    CONF_MANUFACTURER_ID,
    CONF_MAX_VALUE,
    CONF_MIN_VALUE,
    CONF_MODE,
    CONF_NAME,
    CONF_OPTIMISTIC,
    CONF_RESTORE_VALUE,
    CONF_STEP,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_VALUE,
    DEVICE_CLASS_CONNECTIVITY,
    ENTITY_CATEGORY_CONFIG,
    UNIT_MILLISECOND,
)

CODEOWNERS = ["@dmamontov"]
AUTO_LOAD = ["binary_sensor", "number", "button"]

CLASS_NAME = "Esp32BleKeyboard"
CODE = "ble_keyboard"

ble_keyboard_ns = cg.esphome_ns.namespace(CODE)

BLEKeyboard = ble_keyboard_ns.class_(CLASS_NAME, cg.PollingComponent)
BLEKeyboardNumber = ble_keyboard_ns.class_("Esp32BleKeyboardNumber", cg.Component)
BLEKeyboardButton = ble_keyboard_ns.class_("Esp32BleKeyboardButton", cg.Component)
BLEKeyboardPressAction = ble_keyboard_ns.class_("Esp32BleKeyboardPressAction", automation.Action)
BLEKeyboardReleaseAction = ble_keyboard_ns.class_("Esp32BleKeyboardReleaseAction", automation.Action)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(BLEKeyboard),
        cv.Optional(CONF_NAME, default=CLASS_NAME): cv.Length(min=1),
        cv.Optional(CONF_MANUFACTURER_ID, default=CLASS_NAME): cv.Length(min=1),
        cv.Optional(CONF_BATTERY_LEVEL, default=100): cv.int_range(min=0, max=100),
    }
)

BINARY_SENSOR_STATE = {
    CONF_ID: cv.declare_id(binary_sensor.BinarySensor)("connected"),
    CONF_NAME: "Connected",
    CONF_DEVICE_CLASS: DEVICE_CLASS_CONNECTIVITY,
    CONF_DISABLED_BY_DEFAULT: False,
}

NUMBER_DELAY = {
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
}

NUMBER_PRESS_DELAY = "press"
NUMBER_RELEASE_DELAY = "release"

KEYS = [
    {
        CONF_NAME: "Space",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_space"),
        CONF_ICON: "mdi:keyboard-space",
        CONF_VALUE: " ",
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left CTRL",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_left_ctrl"),
        CONF_ICON: "mdi:apple-keyboard-control",
        CONF_VALUE: 0x80,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left SHIFT",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_left_shift"),
        CONF_ICON: "mdi:apple-keyboard-shift",
        CONF_VALUE: 0x81,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left ALT",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_left_alt"),
        CONF_ICON: "mdi:apple-keyboard-option",
        CONF_VALUE: 0x82,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left GUI",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_left_gui"),
        CONF_ICON: "mdi:microsoft-windows",
        CONF_VALUE: 0x83,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right CTRL",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_right_ctrl"),
        CONF_ICON: "mdi:apple-keyboard-control",
        CONF_VALUE: 0x84,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right SHIFT",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_right_shift"),
        CONF_ICON: "mdi:apple-keyboard-shift",
        CONF_VALUE: 0x85,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right ALT",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_right_alt"),
        CONF_ICON: "mdi:apple-keyboard-option",
        CONF_VALUE: 0x86,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right GUI",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_right_gui"),
        CONF_ICON: "mdi:microsoft-windows",
        CONF_VALUE: 0x87,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Up arrow",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_up_arrow"),
        CONF_ICON: "mdi:chevron-up",
        CONF_VALUE: 0xDA,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Down arrow",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_down_arrow"),
        CONF_ICON: "mdi:chevron-down",
        CONF_VALUE: 0xD9,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Left arrow",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_left_arrow"),
        CONF_ICON: "mdi:chevron-left",
        CONF_VALUE: 0xD8,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Right arrow",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_right_arrow"),
        CONF_ICON: "mdi:chevron-right",
        CONF_VALUE: 0xD7,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Backspace",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_backspace"),
        CONF_ICON: "mdi:keyboard-backspace",
        CONF_VALUE: 0xB2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Tab",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_tab"),
        CONF_ICON: "mdi:keyboard-tab",
        CONF_VALUE: 0xB3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Return",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_return"),
        CONF_ICON: "mdi:keyboard-return",
        CONF_VALUE: 0xB0,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Esc",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_esc"),
        CONF_ICON: "mdi:keyboard-esc",
        CONF_VALUE: 0xB1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Insert",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_insert"),
        CONF_ICON: "mdi:alpha-i-box",
        CONF_VALUE: 0xD1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Print screen",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_prtsc"),
        CONF_ICON: "mdi:alpha-p-box",
        CONF_VALUE: 0xCE,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Delete",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_delete"),
        CONF_ICON: "mdi:alpha-d-box",
        CONF_VALUE: 0xD4,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Page up",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_page_up"),
        CONF_ICON: "mdi:arrow-up-box",
        CONF_VALUE: 0xD3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Page down",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_page_down"),
        CONF_ICON: "mdi:arrow-down-box",
        CONF_VALUE: 0xD6,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Home",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_home"),
        CONF_ICON: "mdi:home",
        CONF_VALUE: 0xD2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "End",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_end"),
        CONF_ICON: "mdi:alpha-e-box",
        CONF_VALUE: 0xD5,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Caps Lock",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_caps_lock"),
        CONF_ICON: "mdi:alpha-c-box",
        CONF_VALUE: 0xC1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F1",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f1"),
        CONF_ICON: "mdi:keyboard-f1",
        CONF_VALUE: 0xC2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F2",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f2"),
        CONF_ICON: "mdi:keyboard-f2",
        CONF_VALUE: 0xC3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F3",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f3"),
        CONF_ICON: "mdi:keyboard-f3",
        CONF_VALUE: 0xC4,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F4",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f4"),
        CONF_ICON: "mdi:keyboard-f4",
        CONF_VALUE: 0xC5,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F5",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f5"),
        CONF_ICON: "mdi:keyboard-f5",
        CONF_VALUE: 0xC6,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F6",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f6"),
        CONF_ICON: "mdi:keyboard-f6",
        CONF_VALUE: 0xC7,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F7",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f7"),
        CONF_ICON: "mdi:keyboard-f7",
        CONF_VALUE: 0xC8,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F8",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f8"),
        CONF_ICON: "mdi:keyboard-f8",
        CONF_VALUE: 0xC9,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F9",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f9"),
        CONF_ICON: "mdi:keyboard-f9",
        CONF_VALUE: 0xCA,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F10",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f10"),
        CONF_ICON: "mdi:keyboard-f10",
        CONF_VALUE: 0xCB,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F11",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f11"),
        CONF_ICON: "mdi:keyboard-f11",
        CONF_VALUE: 0xCC,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F12",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f12"),
        CONF_ICON: "mdi:keyboard-f12",
        CONF_VALUE: 0xCD,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "F13",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f13"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF0,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F14",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f14"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF1,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F15",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f15"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF2,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F16",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f16"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF3,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F17",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f17"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF4,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F18",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f18"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF5,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F19",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f19"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF6,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F20",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f20"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF7,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F21",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f21"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF8,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F22",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f22"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xF9,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F23",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f23"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xFA,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "F24",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_f24"),
        CONF_ICON: "mdi:alpha-f",
        CONF_VALUE: 0xFB,
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "Num 0",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_0"),
        CONF_ICON: "mdi:numeric-0",
        CONF_VALUE: 0xEA,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 1",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_1"),
        CONF_ICON: "mdi:numeric-1",
        CONF_VALUE: 0xE1,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 2",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_2"),
        CONF_ICON: "mdi:numeric-2",
        CONF_VALUE: 0xE2,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 3",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_3"),
        CONF_ICON: "mdi:numeric-3",
        CONF_VALUE: 0xE3,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 4",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_4"),
        CONF_ICON: "mdi:numeric-4",
        CONF_VALUE: 0xE4,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 5",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_5"),
        CONF_ICON: "mdi:numeric-5",
        CONF_VALUE: 0xE5,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 6",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_6"),
        CONF_ICON: "mdi:numeric-6",
        CONF_VALUE: 0xE6,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 7",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_7"),
        CONF_ICON: "mdi:numeric-7",
        CONF_VALUE: 0xE7,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 8",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_8"),
        CONF_ICON: "mdi:numeric-8",
        CONF_VALUE: 0xE8,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num 9",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_9"),
        CONF_ICON: "mdi:numeric-9",
        CONF_VALUE: 0xE9,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num slash",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_slash"),
        CONF_ICON: "mdi:slash-forward",
        CONF_VALUE: 0xDC,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num asterisk",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_asterisk"),
        CONF_ICON: "mdi:asterisk",
        CONF_VALUE: 0xDD,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num minus",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_minus"),
        CONF_ICON: "mdi:minus",
        CONF_VALUE: 0xDE,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num plus",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_plus"),
        CONF_ICON: "mdi:plus",
        CONF_VALUE: 0xDF,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num enter",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_enter"),
        CONF_ICON: "mdi:keyboard-return",
        CONF_VALUE: 0xE0,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num dot",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_dot"),
        CONF_ICON: "mdi:circle-small",
        CONF_VALUE: 0xEB,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Scroll lock",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_scroll_lock"),
        CONF_ICON: "mdi:alpha-s-box",
        CONF_VALUE: 0xCF,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Num lock",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_num_lock"),
        CONF_ICON: "mdi:alpha-n-box",
        CONF_VALUE: 0xDB,
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Next track",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_next_track"),
        CONF_ICON: "mdi:skip-next",
        CONF_VALUE: (1, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Previous track",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_previous_track"),
        CONF_ICON: "mdi:skip-previous",
        CONF_VALUE: (2, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Stop",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_stop"),
        CONF_ICON: "mdi:stop",
        CONF_VALUE: (4, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Play/Pause",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_play_pause"),
        CONF_ICON: "mdi:play-pause",
        CONF_VALUE: (8, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Mute",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_mute"),
        CONF_ICON: "mdi:volume-mute",
        CONF_VALUE: (16, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Volume up",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_volume_up"),
        CONF_ICON: "mdi:volume-plus",
        CONF_VALUE: (32, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Volume down",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_volume_down"),
        CONF_ICON: "mdi:volume-minus",
        CONF_VALUE: (64, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "My computer",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_browser"),
        CONF_ICON: "mdi:desktop-classic",
        CONF_VALUE: (0, 1),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Calculator",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_calculator"),
        CONF_ICON: "mdi:calculator",
        CONF_VALUE: (0, 2),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "WWW Bookmarks",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_www_bookmarks"),
        CONF_ICON: "mdi:bookmark",
        CONF_VALUE: (0, 4),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Search",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_www_search"),
        CONF_ICON: "mdi:magnify",
        CONF_VALUE: (0, 8),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Stop",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_www_stop"),
        CONF_ICON: "mdi:close",
        CONF_VALUE: (0, 16),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Back",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_www_back"),
        CONF_ICON: "mdi:arrow-left",
        CONF_VALUE: (0, 32),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "WWW Home",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_www_home"),
        CONF_ICON: "mdi:web",
        CONF_VALUE: (128, 0),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "Consumer control configuration",
        CONF_ID: cv.declare_id(BLEKeyboardButton)(
            "key_media_consumer_control_configuration"
        ),
        CONF_ICON: "mdi:cog",
        CONF_VALUE: (0, 64),
        CONF_DISABLED_BY_DEFAULT: True,
    },
    {
        CONF_NAME: "Email",
        CONF_ID: cv.declare_id(BLEKeyboardButton)("key_media_email"),
        CONF_ICON: "mdi:email",
        CONF_VALUE: (0, 128),
        CONF_DISABLED_BY_DEFAULT: True,
    },
]


async def to_code(config) -> None:
    var = cg.new_Pvariable(
        config[CONF_ID],
        config[CONF_NAME],
        config[CONF_MANUFACTURER_ID],
        config[CONF_BATTERY_LEVEL],
    )

    await cg.register_component(var, config)

    await adding_binary_sensors(var)
    await adding_numbers(var)
    await adding_buttons(var)

    adding_dependencies()


async def adding_buttons(var) -> None:
    for key in KEYS:
        new_key = await button.new_button(key)
        cg.add(new_key.set_parent(var))

        if CONF_VALUE not in key:
            continue

        if isinstance(key[CONF_VALUE], str):
            cg.add(new_key.set_text_value(key[CONF_VALUE]))
        elif isinstance(key[CONF_VALUE], tuple):
            cg.add(new_key.set_media_value(key[CONF_VALUE][0], key[CONF_VALUE][1]))
        else:
            cg.add(new_key.set_int_value(key[CONF_VALUE]))


async def adding_numbers(var) -> None:
    for code in [NUMBER_PRESS_DELAY, NUMBER_RELEASE_DELAY]:
        data = NUMBER_DELAY | {
            CONF_ID: cv.declare_id(BLEKeyboardNumber)(f"{code}_delay"),
            CONF_NAME: f"Delay {code}",
        }

        number_delay = await number.new_number(
            data,
            min_value=data[CONF_MIN_VALUE],
            max_value=data[CONF_MAX_VALUE],
            step=data[CONF_STEP],
        )
        cg.add(number_delay.set_parent(var))
        cg.add(number_delay.set_initial_value(data[CONF_INITIAL_VALUE]))
        if code == NUMBER_PRESS_DELAY:
            cg.add(number_delay.enable_press())
        cg.add(number_delay.setup())


async def adding_binary_sensors(var) -> None:
    cg.add(
        var.set_state_sensor(await binary_sensor.new_binary_sensor(BINARY_SENSOR_STATE))
    )


def adding_dependencies() -> None:
    cg.add_library("ESP32 BLE Arduino", "1.0.1")
    cg.add_library(
        "NimBLE-Arduino",
        "1.4.0",
        "https://github.com/h2zero/NimBLE-Arduino/archive/refs/tags/1.4.0.zip",
    )
    cg.add_library(
        "ESP32-BLE-Keyboard",
        "0.3.2-beta",
        "https://github.com/T-vK/ESP32-BLE-Keyboard/releases/download/0.3.2-beta/ESP32-BLE-Keyboard.zip",
    )

    cg.add_build_flag("-D USE_NIMBLE")


OPERATION_BASE_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_ID): cv.use_id(BLEKeyboard),
    }
)


@automation.register_action(
    f"{CODE}.release",
    BLEKeyboardReleaseAction,
    maybe_simple_id(OPERATION_BASE_SCHEMA),
)
async def ble_keyboard_release_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])

    return cg.new_Pvariable(action_id, template_arg, paren)


@automation.register_action(
    f"{CODE}.press",
    BLEKeyboardPressAction,
    OPERATION_BASE_SCHEMA.extend(
        {
            cv.Required(CONF_VALUE): cv.templatable(cv.string_strict),
        }
    ),
)
async def ble_keyboard_press_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    template_ = await cg.templatable(config[CONF_VALUE], args, cg.std_string)
    cg.add(var.set_value(template_))

    return var




