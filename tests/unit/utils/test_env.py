from __future__ import annotations

from unittest.mock import patch

import pytest

from gex.utils.env import check_env_api_key, check_env_google_api_key

#######################################
#     Tests for check_env_api_key     #
#######################################


@patch.dict("os.environ", {}, clear=True)
def test_check_env_api_key_raises_when_missing() -> None:
    with pytest.raises(RuntimeError, match="MY_API_KEY environment variable is not set or empty"):
        check_env_api_key("MY_API_KEY")


@patch.dict("os.environ", {"MY_API_KEY": ""}, clear=True)
def test_check_env_api_key_raises_when_empty_string() -> None:
    with pytest.raises(RuntimeError, match="MY_API_KEY environment variable is not set or empty"):
        check_env_api_key("MY_API_KEY")


@patch.dict("os.environ", {"MY_API_KEY": "super-secret-value"}, clear=True)
def test_check_env_api_key_does_not_raise_when_set() -> None:
    check_env_api_key("MY_API_KEY")  # should not raise


@patch.dict("os.environ", {"MY_API_KEY": "abcdefghijklmnop"}, clear=True)
def test_check_env_api_key_logs_masked_value(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level("INFO"):
        check_env_api_key("MY_API_KEY")
    assert caplog.messages[0] == "MY_API_KEY=abc*********mnop"


##############################################
#     Tests for check_env_google_api_key     #
##############################################


@patch.dict("os.environ", {}, clear=True)
def test_check_env_google_api_key_raises_when_missing() -> None:
    with pytest.raises(
        RuntimeError, match="GOOGLE_API_KEY environment variable is not set or empty"
    ):
        check_env_google_api_key()


@patch.dict("os.environ", {"GOOGLE_API_KEY": ""}, clear=True)
def test_check_env_google_api_key_raises_when_empty_string() -> None:
    with pytest.raises(
        RuntimeError, match="GOOGLE_API_KEY environment variable is not set or empty"
    ):
        check_env_google_api_key()


@patch.dict("os.environ", {"GOOGLE_API_KEY": "super-secret-value"}, clear=True)
def test_check_env_google_api_key_does_not_raise_when_set() -> None:
    check_env_google_api_key()  # should not raise


@patch.dict("os.environ", {"GOOGLE_API_KEY": "abcdefghijklmnop"}, clear=True)
def test_check_env_google_api_key_logs_masked_value(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level("INFO"):
        check_env_google_api_key()
    assert caplog.messages[0] == "GOOGLE_API_KEY=abc*********mnop"
