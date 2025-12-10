.. _names:

Names
############################################

Standard names provide users with a predefined vocabulary for common themes,
so that they can label assets without constantly reinventing terms.

Standard names are single, **human-readable words** designed to be immediately
interpretable rather than cryptic. Their purpose is to make labels self-explanatory
so users can understand the meaning without additional decoding.

.. dropdown:: Example
    :icon: info
    :open:

    Population is a common variable in demographic studies. ``FLARE`` can define ``population`` as a
    standard name.

    Also, the statistics related to ``population`` can be defined as ``sum`` or ``mean``.
    So a compound label for a field in a database would be ``population_mean``, etc.



.. _names-attributes:

Attributes
============================================

Each standard name has a set of basic attributes, and may optionally include
extended attributes when used for more specific contexts (e.g., thematic variables).

The core attributes set is given in the table below:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Attribute
     - Type / Format
     - Purpose
   * - name
     - Single word
     - Name immediately interpretable by humans.
   * - alias
     - Short single word (up to 5 characters)
     - Short alternative identifier used in compact or symbolic contexts.
   * - title
     - Single phrase
     - Full formal name; concise but descriptive label for the concept.
   * - description
     - Long text, multiple phrases allowed
     - Extended explanation providing context and elaboration beyond the title.


.. _names-metadata:

Metadata Names
============================================

Metadata Names are standard names given to properties of an asset.
For instance, the label ``timestamp`` is given to identify the time of a givern record.

The core metadata names set in ``FLARE`` is given in the table below.

.. csv-table::
   :file: /data/metadata_core.csv
   :header-rows: 1
   :widths: auto
   :delim: ;

.. _names-stats:

Statistics Names
============================================

Statistics Names are typical

.. include:: ./includes/ipsum.rst

.. csv-table::
   :file: /data/statistics_core.csv
   :header-rows: 1
   :widths: auto
   :delim: ;

.. _names-variables:

Thematic Variables
============================================

Thematic variables are standard names related to common information found in scientific and technical contexts.

Each thematic variable is associated with a **theme**, which represents the kind of information it carries,
whether **quantitative** (numeric measures) or **qualitative** (categorical information).

Variables can include suggested **data types** for storing the variable in fields or files, ensuring that datasets are created and encoded consistently across projects.

``FLARE`` also allows **compact modes for data types**: for example, numeric values can be stored as integers together with a **multiplier**. The multiplier enables efficient storage while preserving the actual value range, since the stored integer can be divided by the multiplier to reconstruct the original value. This approach provides a structured and standardized way to encode variables, making them machine-actionable while maintaining clarity and portability in labels.




.. _names-programming-vars:

Programming Variables
============================================

``FLARE`` also applies to **symbols**, which are the identifiers used in code for static and dynamic structures in programming environments (constants, functions, classes, etc).

While the exact naming rules for symbols depend on the programming language, ``FLARE`` provides a consistent approach to structuring symbol names across contexts.

Symbols may follow the same hierarchical logic of domains and subdomains, allowing them to encode information in a structured way that remains human-readable and machine-actionable. Like fields, hyphens are not allowed in symbols, as they are interpreted as subtraction operators in most languages.



.. dropdown:: Example of labeling of a dictionary in Python
    :icon: code
    :open:

    .. code-block:: python

       dc_files = {"a": "C:/report_2025.pdf"}
