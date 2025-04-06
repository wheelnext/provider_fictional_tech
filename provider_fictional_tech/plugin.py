from __future__ import annotations

from provider_fictional_tech import __version__
from variantlib.models.provider import ProviderConfig
from variantlib.models.provider import VariantFeatureConfig


class FictionalTechPlugin:
    __provider_name__ = "fictional_tech"
    __version__ = __version__

    def _get_supported_technologies(self) -> list[str]:
        """Lookup the system to decide what `technology` are supported on this system.
        Returns a list of strings in order of priority."""
        return ["auto_chef"]

    def _get_supported_quantum(self) -> list[str]:
        """Lookup the system to decide what `quantum` are supported on this system.
        Returns a list of strings in order of priority."""
        return ["FOAM", "SUPERPOSITION"]

    def _get_supported_risk_exposure(self) -> list[str]:
        """Lookup the system to decide what `risk_exposure` are supported on this
        system.
        Returns a list of strings in order of priority."""
        return ["25"]

    def get_supported_configs(self) -> ProviderConfig | None:
        keyconfigs = []

        # Top Priority
        if (values := self._get_supported_technologies()) is not None:
            keyconfigs.append(VariantFeatureConfig(name="technology", values=values))

        # Second Priority
        if (values := self._get_supported_quantum()) is not None:
            keyconfigs.append(VariantFeatureConfig(name="quantum", values=values))

        # Third Priority
        if (values := self._get_supported_risk_exposure()) is not None:
            keyconfigs.append(VariantFeatureConfig(name="risk_exposure", values=values))

        if keyconfigs:
            return ProviderConfig(
                provider=FictionalTechPlugin.__provider_name__,
                configs=keyconfigs,
            )

        return None
