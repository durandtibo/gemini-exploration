from __future__ import annotations

import gex


def test_version_exists() -> None:
    assert hasattr(gex, "__version__")
    assert isinstance(gex.__version__, str)
