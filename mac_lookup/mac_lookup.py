# -*- coding: utf-8 -*
"""
maclookup - Used to look up the model name of any MacBook via the serial
number.
"""
__author__ = "Jason Satti"
__version__ = "0.0"


import argparse
import logging.config
import xml.etree.ElementTree as Et

import requests

from config import BASE_APPLE_URL, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger("maclookup")


def log_raise(error_type, message):
    log.debug(message)
    raise error_type(message)


def verify_serial(serial):
    """Verify the serial number passed in via the CLI.

    :param serial: Str passed in via the CLI.
    :return: Str
    """
    if len(serial) > 12:
        log_raise(AttributeError, "Serial number contains more than 12 characters.")
    if len(serial) < 4:
        log_raise(
            AttributeError, "Serial number must contain at least the last 4 characters."
        )
    last_4 = serial[-4:]

    return last_4


def get_model(serial):
    """Retrieve model of MacBook based on last 4 digits of the serial number.

    :param serial: Str returned by verify_serial().
    :return: Str
    """
    url = f"{BASE_APPLE_URL}{serial}"
    r = requests.get(url)
    xml = Et.fromstring(r.text)
    for error in xml.iter("error"):
        if error.text:
            log_raise(AttributeError, "Serial number lookup error.")
    for code in xml.iter("configCode"):
        model = code.text

        return model


def main():
    """Get the model of a MacBook based on the serial number."""
    parser = argparse.ArgumentParser(description="Get Mac Serial Number.")
    parser.add_argument(
        "-sn",
        "--serial",
        required=True,
        type=str,
        help="Serial Number of MacBook for model lookup.",
    )
    args = parser.parse_args()
    serial = verify_serial(args.serial)
    print(get_model(serial))


if __name__ == "__main__":
    main()
