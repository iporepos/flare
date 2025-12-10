.. _names:

Names
############################################

.. include:: ./includes/ipsum.rst

Variables
---------------------------------------------

Variables are a variation of standard names. Each variable is associated with a **topic**, which represents the kind of information it carries, whether **quantitative** (numeric measures) or **qualitative** (categorical information).

Variables can include suggested **data types** for storing the variable in fields or files, ensuring that datasets are created and encoded consistently across projects.

``FLARE`` also allows **compact modes for data types**: for example, numeric values can be stored as integers together with a **multiplier**. The multiplier enables efficient storage while preserving the actual value range, since the stored integer can be divided by the multiplier to reconstruct the original value. This approach provides a structured and standardized way to encode variables, making them machine-actionable while maintaining clarity and portability in labels.

Statistics
---------------------------------------------

TODO

.. include:: ./includes/ipsum.rst


.. _concepts-symbols:

Symbols
---------------------------------------------

``FLARE`` also applies to **symbols**, which are the identifiers used in code for static and dynamic structures in programming environments (constants, functions, classes, etc).

While the exact naming rules for symbols depend on the programming language, ``FLARE`` provides a consistent approach to structuring symbol names across contexts.

Symbols may follow the same hierarchical logic of domains and subdomains, allowing them to encode information in a structured way that remains human-readable and machine-actionable. Like fields, hyphens are not allowed in symbols, as they are interpreted as subtraction operators in most languages.



.. dropdown:: Example of labeling of a dictionary in Python
    :icon: code
    :open:

    .. code-block:: python

       dc_files = {"a": "C:/report_2025.pdf"}
