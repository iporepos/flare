.. _names:

Names
############################################

Standard names provide users with a predefined vocabulary for common themes,
so that they can label assets without constantly reinventing terms.

.. toctree::
   :maxdepth: 1

   metadata
   statistics
   variables

.. _names-rule:

Structure
============================================

Standard names are single, **human-readable words** designed to be immediately
interpretable rather than cryptic. Their purpose is to make labels self-explanatory
so users can understand the meaning without additional decoding.

.. dropdown:: Example
    :icon: info
    :open:

    Population is a common variable in demographic studies. ``FLARE`` define ``population`` as a
    standard name, so it must be used when labeling a column.


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
     - Style
     - Abstract
   * - ``name``
     - Single word
     - Name immediately interpretable by humans.
   * - ``alias``
     - Short single word (up to 5 characters)
     - Short alternative identifier used in compact or symbolic contexts.
   * - ``title``
     - Single phrase
     - Full formal name; concise but descriptive label for the concept.
   * - ``abstract``
     - One paragraph, multiple phrases allowed
     - Extended explanation providing context and elaboration beyond the title.


.. _names-metadata:

Metadata
============================================

Metadata names are standard names given to properties of an asset.
For instance, the label ``timestamp`` is given to identify the time of a given record.
Metadata names spam across a range of themes, depending on the kind of data it refers.

.. dropdown:: Core metadata names
    :icon: table
    :animate: fade-in-slide-down
    :open:

    .. csv-table::
       :file: /data/metadata_core.csv
       :header-rows: 1
       :widths: auto
       :delim: ;

.. seealso::

    Check out :ref:`all metadata names <metadata>` organized by theme.


.. _names-stats:

Statistics
============================================

Statistics names are standard names given to typical statistical measures derived from quantitative data.
For instance, the label ``mean`` is given to identify the arithmetic mean of the sample or population values.
Statistics names spam across some themes, depending on the kind of analysis it refers, like curve fitting or
hypothesis testing.

.. dropdown:: Core statistics names
    :icon: table
    :animate: fade-in-slide-down
    :open:

    .. csv-table::
       :file: /data/statistics_core.csv
       :header-rows: 1
       :widths: auto
       :delim: ;

.. seealso::

    Check out :ref:`all statistics names <statistics>` organized by theme.

.. _names-variables:

Thematic Variables
============================================

Thematic variables are found in scientific and technical contexts.
Each thematic variable is associated with a theme, which represents the kind of information it carries,
whether **quantitative** (numeric measures) or **qualitative** (categorical information).

Names for thematic variables include extra attributes, like *units* and *data-type*.

.. seealso::

    Check out :ref:`all thematic variables <variables>` organized by theme.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Attribute
     - Title
     - Abstract

   * - category
     - Physical unit expressed as a string (e.g., ``m``, ``kg``, ``mm/day``).
     - Conveys measurement units for correct interpretation, conversions, and dimensional checks.

   * - units
     - Physical unit expressed as a string (e.g., ``m``, ``kg``, ``mm/day``).
     - Conveys measurement units for correct interpretation, conversions, and dimensional checks.

   * - dtype
     - Primitive data-type category.
     - Defines the fundamental nature of the data in a language-agnostic way.

   * - min
     - Minimum or lower bound in natural range.
     - Encodes the natural minimum feasible value of the variable; unbounded if null.

   * - max
     - Maximum or lower bound in natural range.
     - Encodes the natural maximum feasible value of the variable; unbounded if null.

   * - dtype_storage
     - Suggested storage data-type in NumPy style.
     - Defines the data-type in NumPy style considering the scale factor.

   * - scale
     - Suggested numeric factor multiplier for efficient storage.
     - Indicates compression or scaling applied during storage; actual value is obtained by applying the inverse of the multiplier.

   * - nodata
     - Suggested value reserved for null value in storage.
     - Specifies the conventional placeholder for missing or undefined values in storage.



.. _names-programming-vars:

Code Variables
============================================

Code variables,
which are the identifiers used in code for static and dynamic structures in
programming environments (constants, functions, classes, etc).

While the exact naming rules for symbols depend on the programming language, ``FLARE`` provides a consistent approach to structuring symbol names across contexts.

Symbols may follow the same hierarchical logic of domains and subdomains, allowing them to encode information in a structured way that remains human-readable and machine-actionable. Like fields, hyphens are not allowed in symbols, as they are interpreted as subtraction operators in most languages.


.. dropdown:: Example of labeling of a dictionary in Python
    :icon: code
    :open:

    .. code-block:: python

       dc_files = {"a": "C:/report_2025.pdf"}
