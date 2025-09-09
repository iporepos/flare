"""
{pythonmodule.py}
-----------------

# todo [major docstring improvement] -- heading
{One sentence module description}

# todo [major docstring improvement] -- main features
Main features:
 - {feature 1}
 - {feature 2}
 - {feature 3}
 - {etc}

Overview
--------

# todo [major docstring improvement] -- overview
Mauris gravida ex quam, in porttitor lacus lobortis vitae.
In a lacinia nisl. Pellentesque habitant morbi tristique senectus
et netus et malesuada fames ac turpis egestas.

Examples
--------

# todo [major docstring improvement] -- examples
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla mollis tincidunt erat eget iaculis. Mauris gravida ex quam,
in porttitor lacus lobortis vitae. In a lacinia nisl.

"""
# --------------- imports ---------------
# import modules from other libs

# ---- native imports ----
import unittest

# ---- external imports ----
# fill [external imports]

# ---- project imports ----
from flare.numflare import encode_number, decode_number

# --------------- constants ---------------

# ---- public ----


# ---- private ----


# --------------- functions ---------------

# ---- public ----


# ---- private ----


# --------------- classes ---------------
# ---- public ----

class TestFlareNumbers(unittest.TestCase):

    def test_simple_integers(self):
        """Test encoding and decoding of plain integers without magnitude or decimals."""
        numbers = [0, 1, 12, 123]
        for n in numbers:
            encoded = encode_number(n, decimals=0, len_min=1, collapse_magnitude=False)
            decoded = decode_number(encoded)
            self.assertAlmostEqual(decoded, n)

    def test_decimals(self):
        """Test encoding and decoding of numbers with decimal fractions."""
        numbers = [0.1, 2.34, -5.67, 123.45]
        for n in numbers:
            encoded = encode_number(n, decimals=2, len_min=1, collapse_magnitude=False)
            decoded = decode_number(encoded)
            self.assertAlmostEqual(decoded, n)

    def test_sign_flags(self):
        """Test that sign flags for latitude/longitude are handled correctly."""
        # Example: negative latitude = 's', positive longitude = 'e'
        encoded = encode_number(-23, decimals=0, is_latitude=True)
        self.assertTrue(encoded.startswith('s'))
        encoded = encode_number(45, decimals=0, is_latitude=False)
        self.assertTrue(encoded.startswith('e'))

    def test_known_encoded_values(self):
        """Test decoding of specific known encoded strings."""
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


# ---- private ----


# --------------- script ---------------
# standalone behaviour as a script
if __name__ == "__main__":
    print("hello world!")
    unittest.main()

