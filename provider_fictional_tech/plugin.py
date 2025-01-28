from variantlib.config import KeyConfig
from variantlib.config import ProviderConfig

from provider_fictional_hw import __version__


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
        return ["1000000000", "100000", "25"]

    def run(self) -> ProviderConfig | None:
        keyconfigs = []

        # Top Priority
        if (values := self._get_supported_technologies()) is not None:
            keyconfigs.append(KeyConfig(key="technology", values=values))

        # Second Priority
        if (values := self._get_supported_quantum()) is not None:
            keyconfigs.append(KeyConfig(key="quantum", values=values))

        # Third Priority
        if (values := self._get_supported_risk_exposure()) is not None:
            keyconfigs.append(KeyConfig(key="risk_exposure", values=values))

        if keyconfigs:
            return ProviderConfig(
                provider=FictionalTechPlugin.__provider_name__,
                configs=keyconfigs,
            )

        return None
