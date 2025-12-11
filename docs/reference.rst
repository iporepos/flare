.. _reference:

Reference
############################################

``FLARE`` organizes its labeling system around a few **concepts** that define how labels are created, structured, and applied.

.. toctree::
   :maxdepth: 1

   Reference <self>
   flags
   numbers
   datetime
   names
   files
   fields
   layers

.. _reference-summary:

Summary
============================================

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Concept
     - Definition
     - Key Features

   * - :ref:`Labels<reference-labels>`
     - Primary identifier in ``FLARE`` used to name any asset.
     - Hierarchical (left-to-right); domains separated by ``_`` ; subdomains optionally separated by ``-``.

   * - :ref:`Components<reference-components>`
     - Fundamental structural elements that compose a label.
     - Include domains, subdomains, numbers, datetime parts, literal flags, and names; ensures consistent semantics.

   * - :ref:`Literal Flags<reference-flags>`
     - Label component. Reserved single-character encodings used to replace otherwise prohibited characters.
     - Encode decimal separators, signs, units, and other symbolic elements; used when domains require precision while preserving valid notation.

   * - :ref:`Numbers<reference-numbers>`
     - Label component. Structured numeric encodings used in labels.
     - Supports integers, real numbers using literal decimal flags, magnitude multipliers, and signed values; ensures machine-readable numeric semantics.

   * - :ref:`Date and Time<reference-datetime>`
     - Label component. Temporal encodings used to represent instants or intervals.
     - Two domains: *timestamp* (exact time) and *epoch* (named or structured periods); standardized YYYYMMDD… formats.

   * - :ref:`Names<reference-names>`
     - Label component. Standardized vocabulary for variables, statistics, domains, and common descriptors.
     - Includes long and short forms; reduces ambiguity and improves consistency across assets.

   * - :ref:`Assets<reference-assets>`
     - Anything that can be labeled.
     - Includes Files, Fields and Layers; each governed by specific constraints on notation, extensions, and allowed characters.

   * - :ref:`Files<reference-files>`
     - Assets stored in the filesystem, often with an extension.
     - Flexible format; extensions allowed; hyphens and subdomains permitted; suitable for descriptive, long-form labels.

   * - :ref:`Fields<reference-fields>`
     - Asset. Columns in tables, datasets, or databases.
     - Strict notation: ASCII letters, digits, underscores only; hyphens prohibited; optimized for database compatibility.

   * - :ref:`Layers<reference-layers>`
     - Asset. Intermediate structured assets (e.g., GIS layers, document sections, database tables, drawing layers).
     - No extensions; hyphens discouraged; plain ASCII tokenization.





.. _reference-labels:

Labels
============================================

The core concept in ``FLARE`` is the **label**.

.. important::

    A **label** is a plain text string used to identify an **asset** in a way that is both human-readable and machine-actionable.

Unlike metadata that sits inside a file, the label itself **encodes** essential descriptive information directly in the asset name. This makes labels stand-alone identifiers: they can be read without opening the file and can be used by scripts for filtering, indexing, or automation.

.. _reference-labels-domains:

Domains
---------------------------------------------

Labels follow a **hierarchical structure**, where information is organized into ordered parts.
Each part represents a **domain** of information and domains are always read from **left to right**, with the most important domain on the left and the least important on the right. This ordering principle applies at all levels of detail: from domains to **subdomains** and down to components.

.. dropdown:: Example
    :icon: code
    :open:

    .. code-block:: none
    
       {domain1}_{subdomain1-subdomain2}_{domain3}

.. _reference-labels-underscore:

Underscore
---------------------------------------------

Underscore ``_`` is the **domain separator**. It is used to split the **domains of information** in the label.

.. dropdown:: Example
    :icon: code
    :open:

    .. code-block:: none

       {domain1}_{domain2}_{domain3}_{domain4}

.. _reference-labels-hyphen:

Hyphen
---------------------------------------------

Hyphen ``-`` is the **subdomain separator**. It applies only in specific cases, such as breaking down a domain into finer parts of **subdomains**. 

.. dropdown:: Example
    :icon: code
    :open:

    .. code-block:: none

       {domain1}_{subdomain1-subdomain2}_{domain3}


.. warning::

    Hyphen separator is optional and sometimes prohibited (e.g., in database field names).

.. _reference-components:

Components
============================================

Components are the building blocks of labels. As mentioned above the underscore ``_`` and the hyphen ``-`` are components
that separate the label in a hierarchy of parts (domains and subdomains).
But the parts itself may use several other components, like Literal Flags, Numbers, Datetime and Standard Names.

.. important::

    A **component** is a building block of a label.

.. _reference-flags:

Literal Flags
---------------------------------------------

**Literal Flags** are reserved characters that encoding certain information. 
These letters replace special characters that are otherwise prohibited.

.. dropdown:: Example
    :icon: info
    :open:
    
    In a domain of a :ref:`Number <numbers>`, the letter ``p`` encodes the decimal separator of the integer and the fractional parts of a number:

    .. code-block:: none

        '0p34' = 0.34

.. seealso:: 

    Get more details on the :ref:`Literal Flags <flags>` documentation page.


.. _reference-numbers:

Numbers
---------------------------------------------

Numbers are a core component, since they are present in nearly every type of label.
``FLARE`` provides a structured approach to encoding **integer numbers, real numbers, signals, and magnitude multipliers**.
Each type has a specific role and format within a label.

.. dropdown:: Example
    :icon: info
    :open:

    Numbers support the decimal separator using the flag ``p`` to merge the integer and the fractional parts of a number:

    .. code-block:: none

        '0P34' = 0.34

    Also, the sign can be encoded using ``n`` and ``e`` for positive and ``s`` and ``w`` for negative:

    .. code-block:: none

        'S023P4' = -23.4

.. seealso::

    Get more details on :ref:`Numbers <numbers>` documentation page.


.. _reference-datetime:

Date and Time
---------------------------------------------

Date and Time (aka **datetime**) is a component used when labels require temporal reference.
To cover different use cases, ``FLARE`` provides two main components of temporal encoding:

* **Timestamp** -- instant records of the timeline.
* **Epoch** -- arbitrary time interval of the timeline.

.. dropdown:: Example
    :icon: info
    :open:

    The flag ``t`` in datetime is used for denoting the time part:

    .. code-block:: none

        '20140302T124804' = 2014-03-02 12:48:04


.. seealso::

    Get more details on :ref:`Date and Time <datetime>` documentation page.

.. _reference-names:

Standard Names
---------------------------------------------

Standard names are components used in many cases, since it provide users with a predefined vocabulary for common themes.
Pre-set naming conventions helps to label assets without constantly reinventing terms.

.. seealso::

    Get more details on :ref:`Names <names>` documentation page.


.. _reference-assets:

Assets
============================================

The term **asset** refers to anything that can be labeled.

.. important::

    Assets are the objects of labeling: the things for which a label provides meaning.

.. _reference-files:

Files
---------------------------------------------

The most obvious type of asset is the **file**.

Files live in the file system of the computer, they carry an **extension suffix** (e.g., ``.csv``, ``.pdf``, ``.png``)
that indicate their structure, and they are usually the first candidates for labeling.

File labels benefit from extensions suffix because they add information about the internal format directly to the name.
Within files, there can still be broad file **categories** (for example, documents, images, datasets),
and these may sometimes call for specialized labeling structures.

.. dropdown:: Example of labeling as raster file
    :icon: info
    :open:

    A raster file is an image with geospatial data stored inside.
    A typical structure for labeling this file would be:

    .. code-block:: none

        '{source}_{product}_{variable}_{extent}_{datetime}.tif'

    So the SRTM Digital Elevation Model for Brazil would look like this:

    .. code-block:: none
    
        'usgs_srtm_dem_brazil_2004.tif'

.. seealso::

    Get more details on :ref:`Files <files>` documentation page.

.. _reference-fields:

Fields
---------------------------------------------

Another important type of asset is the **field**.
Fields are the **column names** of tables in a database or dataset.

When working with complex databases, relational models, or analytical workflows,
fields become central assets that must be labeled consistently. Unlike files,
fields do not have extensions, and their notation is stricter.

.. warning::

    Hyphens in fields are prohibited, and the recommended characters are limited to ASCII letters,
    numbers, and underscores. This ensures maximum compatibility across database systems.

.. seealso::

    Get more details on :ref:`Fields <fields>` documentation page.

.. _reference-layers:

Layers
---------------------------------------------

Between files and fields, there is a large set of **intermediate assets**, which ``FLARE`` refers to as **layers**. 

Layers can appear in different contexts: database schemas, database tables, GIS vector layers,
or any asset that contain multiple labeled divisions. Layers are not files in the filesystem,
but they are not atomic fields either — they occupy the middle ground.

Layers do not carry extensions and the use of hyphens is discouraged.
Their labels must remain plain, unambiguous, and strictly ASCII-based.

.. seealso::

    Get more details on :ref:`Layers <layers>` documentation page.