"""The Kodi Recently Added integration."""

import asyncio
import logging

from homeassistant import config_entries, core

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
PLATFORMS = ["sensor"]


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Set up platforms from a ConfigEntry."""
    kodi_entry_id = entry.data["kodi_entry_id"]
    hass.data[DOMAIN][entry.entry_id] = {"kodi_config_entry_id": kodi_entry_id}

    if not entry.unique_id:
        hass.config_entries.async_update_entry(
            entry, unique_id="kodi_recently_added_media"
        )

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    return True


async def async_unload_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Kodi Recently Added Media component.

    This component can only be configured through the Integrations UI.
    """
    hass.data.setdefault(DOMAIN, {})
    return True
