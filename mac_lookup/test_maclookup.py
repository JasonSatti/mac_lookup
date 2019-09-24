from unittest import mock

import pytest
import requests

from mac_lookup import get_model, verify_serial


def get_successfulcall():
    """Sample of a successful API call.

    :return: reqeusts.Response object.
    """
    successful_call = requests.Response
    successful_call.text = (
        '<?xml version="1.0" encoding="utf-8" '
        "?><root><name>CPU Name</name><configCode>MacBook Pro (15-inch, 2019)</configCode><locale>en_US</locale></root>"
    )

    return successful_call


def get_failedcall():
    """Sample of a failed API call.

    :return: reqeusts.Response object.
    """
    failed_call = requests.Response
    failed_call.text = (
        '<?xml version="1.0" encoding="utf-8" '
        "?><root><error>0009</error><locale>en_US</locale></root>"
    )

    return failed_call


@mock.patch("mac_lookup.requests.get", autospec=True)
def test_getmodel(mock_getmodel):
    """Test a successful called based on a live accurate MacBook serial number.

    :return: True
    """
    mock_getmodel.return_value = get_successfulcall()
    serial = "C02Z20D2LVDT"
    assert (get_model(serial)) == "MacBook Pro (15-inch, 2019)"


@mock.patch("mac_lookup.requests.get", autospec=True)
def test_wrongserial(mock_getmodel):
    """Test a failed called based on an inaccurate MacBook serial number.

    :return: True
    """
    mock_getmodel.return_value = get_failedcall()
    serial = "C02Z20D2LVDS"
    with pytest.raises(AttributeError, match="Serial number lookup error."):
        get_model(serial)


def test_longserial():
    """Test a failed serial verification based on length being longer than
    12 characters.

    :return: True
    """
    serial = "C02LR3KJRNRTI"
    with pytest.raises(
        AttributeError, match="Serial number contains more than 12 characters."
    ):
        verify_serial(serial)


def test_shortserial():
    """Test a failed serial verification based on length being shorter than
    4 characters.

    :return: True
    """
    serial = "RTI"
    with pytest.raises(
        AttributeError,
        match="Serial number must contain at least the last 4 characters.",
    ):
        verify_serial(serial)


def test_emptyserial():
    """Test a failed serial verification based on length being 0.

    :return: True
    """
    serial = ""
    with pytest.raises(
        AttributeError,
        match="Serial number must contain at least the last 4 characters.",
    ):
        verify_serial(serial)


def test_nullserial():
    """Test a failed serial verification based on argument not being passed in.

    :return: True
    """
    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'serial'"
    ):
        verify_serial()


# No longer needed due to verify_serial()
# @mock.patch("mac_lookup.requests.get", autospec=True)
# def test_longserial(mock_getmodel):
#     mock_getmodel.return_value = get_failedcall()
#     serial = "1252151251214214"
#     with pytest.raises(AttributeError, match="Serial number lookup error."):
#         get_model(serial)


# No longer needed due to verify_serial()
# @mock.patch("mac_lookup.requests.get", autospec=True)
# def test_shortserial(mock_getmodel):
#     mock_getmodel.return_value = get_failedcall()
#     serial = "VDT"
#     with pytest.raises(AttributeError, match="Serial number lookup error."):
#         get_model(serial)


# No longer needed due to verify_serial()
# @mock.patch("mac_lookup.requests.get", autospec=True)
# def test_emptyserial(mock_getmodel):
#     mock_getmodel.return_value = get_failedcall()
#     serial = ""
#     with pytest.raises(AttributeError, match="Serial number lookup error."):
#         get_model(serial)
