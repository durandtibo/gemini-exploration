r"""Define utility functions for environment variables."""

from __future__ import annotations

__all__ = ["check_env_api_key"]

import logging
import os

from coola.utils.secret import mask_secret

logger = logging.getLogger(__name__)


def check_env_api_key(name: str) -> None:
    r"""Check if the API key is set as an environment variable.

    Args:
        name: Name of the environment variable.

    Raises:
        RuntimeError: If the API key is not set.

    Example:
        ```pycon
        >>> from gex.utils.env import check_env_api_key
        >>> check_env_api_key()

        ```
    """
    key = os.environ.get(name)
    if not key:
        msg = f"{name} environment variable is not set or empty"
        raise RuntimeError(msg)
    logger.info(f"{name}={mask_secret(key)}")
