"""The Environment Variable integration."""

from __future__ import annotations

import logging
import os

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({DOMAIN: {cv.string: cv.string}}, extra=vol.ALLOW_EXTRA)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up Environment Variable component."""

    try:
        await set_environment_variable(config)
    except:
        _LOGGER.warning("Environment Variable setup has been interrupted.")
        raise

    return True


async def set_environment_variable(config: ConfigType) -> bool:
    """Set an environment variable at HA application level."""

    conf = config.get(DOMAIN)

    for env_var_name, env_var_value in conf.items():
        var = str(env_var_name).upper()
        val = str(env_var_value)
        os.environ[var] = val
        _LOGGER.debug(f"Setting environment variable: {var} => {val}")

    return True
