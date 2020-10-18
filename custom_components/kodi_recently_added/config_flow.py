import logging
from typing import Optional

from homeassistant import config_entries
from homeassistant.components.kodi.const import DOMAIN as KODI_DOMAIN
from homeassistant.core import callback
import voluptuous as vol

from .const import CONF_HIDE_WATCHED, DOMAIN

_LOGGER = logging.getLogger(__name__)
CONF_KODI_INSTANCE = "kodi_entry_id"

OPTIONS_SCHEMA = vol.Schema({vol.Optional(CONF_HIDE_WATCHED, default=False): bool})


class KodiRecentlyAddedConfifFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Kodi Recently Added config flow."""

    async def async_step_user(self, user_input):
        """Handle a flow initialized by the user interface."""
        kodi_instances = {
            entry.entry_id: entry.title
            for entry in self.hass.config_entries.async_entries(KODI_DOMAIN)
            if entry.source != "ignore"
        }
        data_schema = vol.Schema(
            {vol.Required(CONF_KODI_INSTANCE): vol.In(list(kodi_instances.values()))}
        )

        errors = {}
        if not kodi_instances:
            errors["base"] = "kodi_not_configured"

        if user_input is not None:
            config_entry_id: Optional[str] = None
            for entry_id, title in kodi_instances.items():
                if title == user_input[CONF_KODI_INSTANCE]:
                    config_entry_id = entry_id
                    break
            if config_entry_id is None:
                errors["base"] = "kodi_not_configured"

            if not errors:
                return self.async_create_entry(
                    title="Kodi Recently Added", data={"kodi_entry_id": config_entry_id}
                )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handles options flow for the component."""

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=OPTIONS_SCHEMA,
        )
