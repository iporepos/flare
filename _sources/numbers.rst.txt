.. _numbers:

Numbers
############################################

Numbers are a core component, since they are present in nearly every type of label.
``FLARE`` provides a structured approach to encoding **integer numbers, real numbers, sign and magnitude multipliers**.
Each type has a specific role and format within a label.

.. _numbers-summary:

Summary
============================================

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Number convention
     - Rule / Format
     - Notes
   * - Integer numbers
     - Zero-filled, fixed length
     - Ensures alignment and lexical sorting
   * - Real numbers
     - ``{integer}p{decimals}``
     - Uses ``p`` instead of ``.`` for decimals
   * - Signal (prefixes)
     - flags ``w``, ``s``, ``e``, ``n``
     - Case-insensitive; applied as prefixes
   * - Magnitude (suffixes)
     - flags ``d``, ``c``, ``k``, ``m``, ``b``
     - Case-insensitive; applied as suffixes


.. _numbers-integers:

Integers
============================================

Integer numbers are the most basic form of numerical encoding in ``FLARE``.
They are used to represent counts, indices, or sequential identifiers.
To ensure proper alignment and **consistent sorting**, integers are typically represented in a **zero-filled format** with a pre-set length for each label chunk.
This avoids issues where, for example, ``2`` would otherwise appear after ``20`` in a lexical sort.

* **Format:** zero-filled integers of fixed length.
* **Purpose:** alignment, sorting, and clarity.

.. dropdown:: Examples
    :icon: info
    :open:

    .. list-table::
       :widths: 50 50
       :header-rows: 1

       * - Encoded
         - Decoded
       * - ``00002``
         - :math:`+ 2`
       * - ``00020``
         - :math:`+ 20`
       * - ``01223``
         - :math:`+ 1223`


.. _numbers-real:

Real numbers
============================================

Real numbers extend the integer format by allowing **decimal plates**.
Because certain characters, like the period ``.``, are prohibited in labels,
``FLARE`` uses the letter ``p`` as a decimal separator.
This allows precise numerical values to be encoded without violating the text-only principle.

* **Format:** ``[integer]p[decimals]``
* **Purpose:** represent fractional values in a fully text-compatible way.

.. dropdown:: Examples
    :icon: info
    :open:

    .. list-table::
       :widths: 50 50
       :header-rows: 1

       * - Encoded
         - Decoded
       * - ``002p3``
         - :math:`+ 2.3`
       * - ``023p4``
         - :math:`+ 23.4`
       * - ``125p0``
         - :math:`+ 125.0`


.. _numbers-sign:

Sign
============================================

By default, ``FLARE`` assumes the sign of a number is **positive**. But in some contexts, numbers need to convey **direction, polarity, or orientation**, such as in georeferencing or coordinate systems. For this, ``FLARE`` uses **signal flags**, which are letters placed at the **beginning of a number**, to indicate whether it is positive or negative.

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Prefix
     - Sign
     - Quadrant
   * - ``w``
     - negative
     - West
   * - ``s``
     - negative
     - South
   * - ``e``
     - positive
     - East
   * - ``n``
     - positive
     - North

* Sign flags are **case-insensitive** and are always **prefixes to the numeric value**.

.. dropdown:: Examples
    :icon: info
    :open:

    .. list-table::
       :widths: 50 50
       :header-rows: 1

       * - Encoded
         - Decoded
       * - ``S002p3``
         - :math:`- 2.3`
       * - ``N023p4``
         - :math:`+ 23.4`
       * - ``w125p0``
         - :math:`- 125.0`

.. _numbers-magnitude:

Magnitude
============================================

By default, ``FLARE`` assumes the multiplier of a number is 1. Sometimes, it is necessary to indicate that a number should be interpreted with a **scale or multiplier**, such as hundreds or thousands.
``FLARE`` uses **magnitude multiplier flags** as **suffixes** to numbers, separate from signals, to encode this information.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Suffix
     - Multiplier
   * - ``d``
     - tens (x10)
   * - ``c``
     - hundreds (x100)
   * - ``k``
     - thousands (x1,000)
   * - ``m``
     - millions (x1,000,000)
   * - ``b``
     - billions (x1,000,000,000)

* Multipliers are **optional** and **case-insensitive**, allowing consistent scaling in numeric encoding.

.. dropdown:: Examples
    :icon: info
    :open:

    .. list-table::
       :widths: 50 50
       :header-rows: 1

       * - Encoded
         - Decoded
       * - ``02p3k``
         - :math:`+ 2,300.0`
       * - ``23p44c``
         - :math:`+ 2,344.0`
       * - ``W05P0M``
         - :math:`- 5,000,000.0`

.. _numbers-flags:

Literal Flags
============================================

.. csv-table::
       :file: /data/flags_number.csv
       :header-rows: 1
       :widths: auto
       :delim: ;