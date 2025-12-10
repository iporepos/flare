# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2025 The Project Authors
# See pyproject.toml for authors/maintainers.
# See LICENSE for license details.
"""
{Short module description (1-3 sentences)}
todo docstring

Features
--------
todo docstring

* {feature 1}
* {feature 2}
* {feature 3}
* {etc}

Overview
--------
todo docstring
{Overview description}

Examples
--------
todo docstring
{Examples in rST}

Print a message

.. code-block:: python

    # print message
    print("Hello world!")
    # [Output] >> 'Hello world!'


"""
# IMPORTS
# ***********************************************************************
# import modules from other libs

# Native imports
# =======================================================================
import unittest
import time

# ... {develop}

# External imports
# =======================================================================
# import {module}
# ... {develop}

# Project-level imports
# =======================================================================
from flare.numflare import encode_number, decode_number
from tests import conftest

# ... {develop}


# CONSTANTS
# ***********************************************************************
# define constants in uppercase

# CONSTANTS -- Project-level
# =======================================================================
# ... {develop}

# CONSTANTS -- Module-level
# =======================================================================
# ... {develop}


# FUNCTIONS
# ***********************************************************************

# FUNCTIONS -- Project-level
# =======================================================================
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
class TestFlareNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Runs once before all tests in this class.
        """
        cls.data = conftest.load_numbers_data()
        return None

    '''
    def setUp(self):
        """
        Runs before each test method.
        """
        #conftest.testprint(f"setting up {type(self).__name__}")
        return None
    '''

    def test_simple_integers(self):
        """
        Test encoding and decoding of plain integers without magnitude or decimals.
        """
        print(conftest.testprint("simple integers"))
        numbers = self.data["v1"].values
        for n in numbers:
            encoded = encode_number(n, decimals=0, len_min=1, collapse_magnitude=False)
            decoded = decode_number(encoded)
            self.assertAlmostEqual(decoded, n)

    def test_decimals(self):
        """
        Test encoding and decoding of numbers with decimal fractions.
        """
        print(conftest.testprint("decimals"))
        numbers = self.data["v3"].round(2).values
        for n in numbers:
            encoded = encode_number(n, decimals=2, len_min=1, collapse_magnitude=False)
            decoded = decode_number(encoded)
            self.assertAlmostEqual(decoded, n)

    def test_sign_flags(self):
        """
        Test that sign flags for latitude/longitude are handled correctly.
        """
        print(conftest.testprint("sign flag"))
        # Example: negative latitude = 's', positive longitude = 'e'
        encoded = encode_number(-23, decimals=0, is_latitude=True)
        self.assertTrue(encoded.startswith("s"))
        encoded = encode_number(45, decimals=0, is_latitude=False)
        self.assertTrue(encoded.startswith("e"))

    def test_known_encoded_values(self):
        """
        Test decoding of specific known encoded strings.
        """
        print(conftest.testprint("decoding"))
        known_pairs = [
            ("n002p3", 2.3),
            ("s023p4", -23.4),
            ("w05p0m", -5_000_000.0),
            ("23p44c", 2344.0),
            ("00002", 2),
        ]
        for encoded, expected in known_pairs:
            decoded = decode_number(encoded)
            self.assertAlmostEqual(decoded, expected)


# ... {develop}


# SCRIPT
# ***********************************************************************
# standalone behaviour as a script
if __name__ == "__main__":
    unittest.main()
