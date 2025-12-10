# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2025 The Project Authors
# See pyproject.toml for authors/maintainers.
# See LICENSE for license details.
"""
Core utilities for encoding and decoding numbers in Flare labels, including integers,
fractions, sign flags and magnitude multipliers.

Features
--------
 - Encode numeric values into compact, human-readable strings
 - Decode previously encoded numbers back into floats
 - Handle latitude/longitude sign flags (`n`, `s`, `e`, `w`)
 - Optional magnitude suffixes (`d`, `c`, `k`, `m`, `b`)

Overview
--------

This module provides a structured, text-based representation of numbers that is
consistent, sortable, and machine-actionable. It supports integers, real numbers
with decimal fractions, optional directional signs, and optional magnitude multipliers.
For full conceptual details, refer to the Flare documentation on **Numbers**.

Examples
--------

Encoding a number

.. code-block:: python

    # Encode a negative latitude with decimals and minimum length
    encoded_lat = encode_number(-12.3, decimals=1, len_min=4, is_latitude=True)
    print(encoded_lat)
    # Output: 's0012p3'


Decoding a number

.. code-block:: python

    # Decode an encoded number
    decoded_lat = decode_number("s0012p3")
    print(decoded_lat)
    # Output: -12.3

Magnitude feature

.. code-block:: python

    # Encode a number with magnitude
    encoded_mag = encode_number(2500, decimals=0, len_min=2, collapse_magnitude=True)
    print(encoded_mag)
    # Output: 'n25k'


"""
# IMPORTS
# ***********************************************************************
# import modules from other libs

# Native imports
# =======================================================================
import re

# ... {develop}

# External imports
# =======================================================================
# import {module}
# ... {develop}

# Project-level imports
# =======================================================================
# import {module}
# ... {develop}


# CONSTANTS
# ***********************************************************************
# define constants in uppercase

# CONSTANTS -- Project-level
# =======================================================================
SIGN = {
    "latitude": {
        "positive": "n",
        "negative": "s",
    },
    "longitude": {
        "positive": "e",
        "negative": "w",
    },
}

DECIMAL = "p"

MAGNITUDES = {
    "d": 10,
    "c": 100,
    "k": 1000,
    "m": 1_000_000,
    "b": 1_000_000_000,
}
# ... {develop}

# CONSTANTS -- Module-level
# =======================================================================
# ... {develop}


# FUNCTIONS
# ***********************************************************************

# FUNCTIONS -- Project-level
# =======================================================================


def encode_number(
    number, decimals=0, len_min=1, is_latitude=True, collapse_magnitude=False
):
    """
    Encodes a given number (latitude or longitude) into a specific string format.

    :param number: The number to encode (latitude or longitude).
    :type number: float or int
    :param decimals: The number of decimal places to include. Default value = 0
    :type decimals: int
    :param len_min: The minimum length of the integer part, padded with leading zeros if necessary. Default value = 1
    :type len_min: int
    :param is_latitude: If True, the number is treated as a latitude; otherwise, as a longitude. Default value = True
    :type is_latitude: bool
    :param collapse_magnitude: If True, collapse the number into a magnitude suffix (d, c, k, m, b)
    :type collapse_magnitude: bool
    :return: The encoded number string.
    :rtype: str
    """

    def fill_integer_part(part, len_min):
        n_len_part = len(part)
        if n_len_part < len_min:
            return part.zfill(len_min)
        else:
            return part

    # Determine the sign flag based on number and coordinate type
    if is_latitude:  # Latitude: 's' for south (negative), 'n' for north (positive)
        if number < 0:
            sign_flag = SIGN["latitude"]["negative"]
        else:
            sign_flag = SIGN["latitude"]["positive"]
    else:  # Longitude: 'w' for west (negative), 'e' for east (positive)
        if number < 0:
            sign_flag = SIGN["longitude"]["negative"]
        else:
            sign_flag = SIGN["longitude"]["positive"]

    # Work with the absolute value for number representation
    abs_number = abs(number)

    # Handle magnitude
    magnitude_flag = ""
    if collapse_magnitude:
        for flag, factor in MAGNITUDES.items():
            if abs_number >= factor:
                abs_number = abs_number / factor
                magnitude_flag = flag
                break  # choose the largest possible factor only once

    encoded_number_part = ""

    # Handle decimals based on tolerance
    if decimals == 0:
        # If tolerance is zero, encode as an integer (no 'p')
        # Round the number to the nearest integer before converting to string
        integer_part_str = str(int(round(abs_number)))
        # Apply zfill to the integer part if zfill_amount is greater than its length
        integer_part_str = fill_integer_part(part=integer_part_str, len_min=len_min)
        encoded_number_part = integer_part_str
    else:
        # Format the number to the specified decimal places
        formatted_num_str = "{:.{}f}".format(abs_number, decimals)

        # Split into integer and fractional parts
        parts = formatted_num_str.split(".")
        integer_part_str = parts[0]
        fractional_part_str = parts[1]

        # Apply zfill to the integer part if zfill_amount is greater than its length
        integer_part_str = fill_integer_part(part=integer_part_str, len_min=len_min)

        # Reconstruct the number part with 'p'
        encoded_number_part = integer_part_str + DECIMAL + fractional_part_str

    # Combine sign flag and the encoded number part, ensure lowercase output
    return (sign_flag + encoded_number_part + magnitude_flag).lower()


def decode_number(encoded_number):
    """
    Decodes an encoded number string (latitude or longitude) back into a float.

    :param encoded_number: The encoded number string.
    :type encoded_number: str
    :return: The decoded number.
    :rtype: float
    """
    # Convert the input to lowercase
    encoded_number_lower = encoded_number.lower()

    # --------------- handle magnitude ---------------
    magnitude_multiplier = 1
    if encoded_number_lower[-1] in MAGNITUDES:
        magnitude_multiplier = MAGNITUDES[encoded_number_lower[-1]]
        encoded_number_lower = encoded_number_lower[:-1]  # strip the suffix

    # --------------- handle sign ---------------
    # Assume positive by default
    sign = 1
    # Check for negative signal flags
    tp_neg = (SIGN["longitude"]["negative"], SIGN["latitude"]["negative"])
    tp_pos = (SIGN["longitude"]["positive"], SIGN["latitude"]["positive"])
    if encoded_number_lower.startswith(tp_neg):
        sign = -1
        # Remove the sign flag
        encoded_number_lower = encoded_number_lower[1:]
    # Check for positive signal flags
    elif encoded_number_lower.startswith(tp_pos):
        # Remove the sign flag for number processing (sign remains positive)
        encoded_number_lower = encoded_number_lower[1:]

    # --------------- handle decimal ---------------
    if DECIMAL in encoded_number_lower:
        # Replace 'p' with '.' for standard float conversion
        _ls = encoded_number_lower.split(DECIMAL)
        integer_part = str(int(decode_number(encoded_number=_ls[0])))
        rational_part = _ls[1]
        encoded_number_lower = integer_part + "." + rational_part

    # return as float
    return sign * float(encoded_number_lower) * magnitude_multiplier


# ... {develop}

# FUNCTIONS -- Module-level
# =======================================================================
# ... {develop}


# CLASSES
# ***********************************************************************

# CLASSES -- Project-level
# =======================================================================
# ... {develop}

# CLASSES -- Module-level
# =======================================================================
# ... {develop}


# SCRIPT
# ***********************************************************************
# standalone behaviour as a script
if __name__ == "__main__":

    # Script section
    # ===================================================================
    n = 100
    s = encode_number(
        number=n, decimals=1, len_min=3, is_latitude=True, collapse_magnitude=True
    )
    print(s)
    n2 = decode_number(encoded_number=s)
    print(n2)
    # ... {develop}
