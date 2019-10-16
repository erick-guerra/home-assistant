"""Config flow for Somfy."""
import logging

from homeassistant.helpers import config_entry_oauth2_flow
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class SomfyConfigFlow(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Config flow to handle Somfy OAuth2 authentication."""

    DOMAIN = DOMAIN

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)

    async def async_step_import(self, user_input=None):
        """Handle a flow start."""
        if self.hass.config_entries.async_entries(DOMAIN):
            return self.async_abort(reason="already_setup")

        return await super().async_step_import(user_input)

    async def async_step_user(self, user_input=None):
        """Handle a flow start."""
        if self.hass.config_entries.async_entries(DOMAIN):
            return self.async_abort(reason="already_setup")

        return await super().async_step_user(user_input)
