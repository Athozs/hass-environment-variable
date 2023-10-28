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


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up Environment Variable component."""

    try:
        set_environment_variable(config)
    except:
        _LOGGER.warning("Environment Variable setup has been interrupted.")
        raise

    return True


def set_environment_variable(config: ConfigType) -> bool:
    """Set an environment variable at HA application level."""

    conf = config.get(DOMAIN)

    for env_var_name, env_var_value in conf.items():
        os.environ[str(env_var_name).upper()] = str(env_var_value)

    return True
