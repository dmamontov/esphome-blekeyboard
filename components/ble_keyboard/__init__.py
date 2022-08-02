"""BleKeyboard component."""

from __future__ import annotations

from typing import Final

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.automation import maybe_simple_id
from esphome.components import binary_sensor, button, number
from esphome.const import (
    CONF_BATTERY_LEVEL,
    CONF_CODE,
    CONF_DELAY,
    CONF_ID,
    CONF_INITIAL_VALUE,
    CONF_MANUFACTURER_ID,
    CONF_MAX_VALUE,
    CONF_MIN_VALUE,
    CONF_NAME,
    CONF_STEP,
    CONF_VALUE,
)
from esphome.core import ID
from esphome.cpp_generator import LambdaExpression, MockObj, TemplateArguments

from .const import (
    ACTION_COMBINATION_CLASS,
    ACTION_PRESS_CLASS,
    ACTION_PRINT_CLASS,
    ACTION_RELEASE_CLASS,
    BINARY_SENSOR_STATE,
    BUILD_FLAGS,
    BUTTONS_KEY,
    COMPONENT_BUTTON_CLASS,
    COMPONENT_CLASS,
    COMPONENT_NUMBER_CLASS,
    CONF_BUTTONS,
    CONF_KEYS,
    CONF_TEXT,
    DOMAIN,
    LIBS,
    NUMBER_BASE_DELAY,
    NUMBER_PRESS_DELAY,
    NUMBER_RELEASE_DELAY,
)

CODEOWNERS: Final = ["@dmamontov"]
AUTO_LOAD: Final = ["binary_sensor", "number", "button"]

ble_keyboard_ns = cg.esphome_ns.namespace(DOMAIN)

BLEKeyboard = ble_keyboard_ns.class_(COMPONENT_CLASS, cg.PollingComponent)
BLEKeyboardNumber = ble_keyboard_ns.class_(COMPONENT_NUMBER_CLASS, cg.Component)
BLEKeyboardButton = ble_keyboard_ns.class_(COMPONENT_BUTTON_CLASS, cg.Component)

CONFIG_SCHEMA: Final = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(BLEKeyboard),
        cv.Optional(CONF_NAME, default=COMPONENT_CLASS): cv.Length(min=1),
        cv.Optional(CONF_MANUFACTURER_ID, default=COMPONENT_CLASS): cv.Length(min=1),
        cv.Optional(CONF_BATTERY_LEVEL, default=100): cv.int_range(min=0, max=100),
        cv.Optional(CONF_BUTTONS, default=True): cv.boolean,
    }
)


async def to_code(config: dict) -> None:
    """Generate component

    :param config: dict
    """

    var = cg.new_Pvariable(
        config[CONF_ID],
        config[CONF_NAME],
        config[CONF_MANUFACTURER_ID],
        config[CONF_BATTERY_LEVEL],
    )

    await cg.register_component(var, config)

    await adding_binary_sensors(var)
    await adding_numbers(var)

    if config[CONF_BUTTONS]:
        await adding_buttons(var)

    adding_dependencies()


async def adding_buttons(var: MockObj) -> None:
    """Adding buttons

    :param var: MockObj
    """

    for key in BUTTONS_KEY:
        new_key: MockObj = await button.new_button(
            key | {CONF_ID: cv.declare_id(BLEKeyboardButton)(key[CONF_ID])}
        )
        cg.add(new_key.set_parent(var))

        if CONF_VALUE not in key:
            continue

        if isinstance(key[CONF_VALUE], tuple):
            cg.add(new_key.set_value(*key[CONF_VALUE]))
        else:
            cg.add(new_key.set_value(key[CONF_VALUE]))


async def adding_numbers(var: MockObj) -> None:
    """Adding numbers

    :param var: MockObj
    """

    for num in [NUMBER_PRESS_DELAY, NUMBER_RELEASE_DELAY]:
        data: dict = NUMBER_BASE_DELAY | {
            CONF_ID: cv.declare_id(BLEKeyboardNumber)(f"{num}_delay"),
            CONF_NAME: f"Delay {num}",
        }

        number_delay: MockObj = await number.new_number(
            data,
            min_value=data[CONF_MIN_VALUE],
            max_value=data[CONF_MAX_VALUE],
            step=data[CONF_STEP],
        )
        cg.add(number_delay.set_parent(var))
        cg.add(number_delay.set_initial_value(data[CONF_INITIAL_VALUE]))
        if DOMAIN == NUMBER_PRESS_DELAY:
            cg.add(number_delay.enable_press())
        cg.add(number_delay.setup())


async def adding_binary_sensors(var: MockObj) -> None:
    """Adding binary sensor

    :param var: MockObj
    """

    cg.add(
        var.set_state_sensor(await binary_sensor.new_binary_sensor(BINARY_SENSOR_STATE))
    )


def adding_dependencies() -> None:
    """Adding dependencies"""

    for lib in LIBS:
        cg.add_library(*lib)

    cg.add_build_flag(BUILD_FLAGS)


OPERATION_BASE_SCHEMA: Final = cv.Schema(
    {
        cv.Required(CONF_ID): cv.use_id(BLEKeyboard),
    }
)

BLEKeyboardReleaseAction = ble_keyboard_ns.class_(
    ACTION_RELEASE_CLASS, automation.Action
)


@automation.register_action(
    f"{DOMAIN}.release",
    BLEKeyboardReleaseAction,
    maybe_simple_id(OPERATION_BASE_SCHEMA),
)
async def ble_keyboard_release_to_code(
    config: dict, action_id: ID, template_arg: TemplateArguments, args: list
) -> MockObj:
    """Action release

    :param config: dict
    :param action_id: ID
    :param template_arg: TemplateArguments
    :param args: list
    :return: MockObj
    """

    paren: MockObj = await cg.get_variable(config[CONF_ID])

    return cg.new_Pvariable(action_id, template_arg, paren)


BLEKeyboardPrintAction = ble_keyboard_ns.class_(ACTION_PRINT_CLASS, automation.Action)


@automation.register_action(
    f"{DOMAIN}.print",
    BLEKeyboardPrintAction,
    OPERATION_BASE_SCHEMA.extend(
        {
            cv.Required(CONF_TEXT): cv.templatable(cv.string_strict),
        }
    ),
)
async def ble_keyboard_print_to_code(
    config: dict, action_id: ID, template_arg: TemplateArguments, args: list
) -> MockObj:
    """Action print

    :param config: dict
    :param action_id: ID
    :param template_arg: TemplateArguments
    :param args: list
    :return: MockObj
    """

    paren: MockObj = await cg.get_variable(config[CONF_ID])
    var: MockObj = cg.new_Pvariable(action_id, template_arg, paren)
    template_: LambdaExpression = await cg.templatable(
        config[CONF_TEXT], args, cg.std_string
    )

    cg.add(var.set_text(template_))

    return var


BLEKeyboardPressAction = ble_keyboard_ns.class_(ACTION_PRESS_CLASS, automation.Action)


@automation.register_action(
    f"{DOMAIN}.press",
    BLEKeyboardPressAction,
    OPERATION_BASE_SCHEMA.extend(
        {
            cv.Required(CONF_CODE): cv.Any(
                cv.templatable(cv.positive_int),
                cv.All(
                    [cv.uint8_t],
                    cv.Length(min=2, max=2),
                ),
            ),
        }
    ),
)
async def ble_keyboard_press_to_code(
    config: dict, action_id: ID, template_arg: TemplateArguments, args: list
) -> MockObj:
    """Action press

    :param config: dict
    :param action_id: ID
    :param template_arg: TemplateArguments
    :param args: list
    :return: MockObj
    """

    paren: MockObj = await cg.get_variable(config[CONF_ID])
    var: MockObj = cg.new_Pvariable(action_id, template_arg, paren)

    if isinstance(config[CONF_CODE], list):
        cg.add(var.set_keys(config[CONF_CODE]))
    else:
        template_: LambdaExpression = await cg.templatable(config[CONF_CODE], args, int)

        cg.add(var.set_code(template_))

    return var


BLEKeyboardCombinationAction = ble_keyboard_ns.class_(
    ACTION_COMBINATION_CLASS, automation.Action
)


@automation.register_action(
    f"{DOMAIN}.combination",
    BLEKeyboardCombinationAction,
    OPERATION_BASE_SCHEMA.extend(
        {
            cv.Required(CONF_DELAY): cv.templatable(cv.positive_int),
            cv.Required(CONF_KEYS): cv.All(
                [cv.Any(cv.string_strict, cv.uint8_t)],
                cv.Length(min=2, max=5),
            ),
        }
    ),
)
async def ble_keyboard_combination_to_code(
    config: dict, action_id: ID, template_arg: TemplateArguments, args: list
) -> MockObj:
    """Action combination

    :param config: dict
    :param action_id: ID
    :param template_arg: TemplateArguments
    :param args: list
    :return: MockObj
    """

    paren: MockObj = await cg.get_variable(config[CONF_ID])
    var: MockObj = cg.new_Pvariable(action_id, template_arg, paren)
    template_: LambdaExpression = await cg.templatable(config[CONF_DELAY], args, int)

    cg.add(var.set_delay(template_))
    cg.add(var.set_keys([str(key) for key in config[CONF_KEYS]]))

    return var
