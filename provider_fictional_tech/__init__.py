#!/usr/bin/env python

import importlib.metadata

from provider_fictional_tech.plugin import FictionalTechPlugin

__all__ = ["FictionalTechPlugin", "__version__"]

__version__ = importlib.metadata.version("provider_fictional_tech")
