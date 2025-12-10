.. _concepts:

Concepts
############################################

``FLARE`` organizes its labeling system around a few **concepts** that define how labels are created, structured, and applied.

.. toctree::
   :maxdepth: 1

   Concepts <self>
   flags
   numbers
   datetime
   names
   files

.. _concepts-summary:

Summary
============================================

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Concept
     - Definition
     - Key Features / Notes
   * - **Label**
     - The primary identifier in ``FLARE``, a text string for naming an asset.
     - Hierarchical; domains left-to-right; separators `_` and `-`; literal flags for compact info.
   * - **Assets**
     - Anything that can be labeled.
     - Includes **Files**, **Fields**, **Layers**, and **Symbols**. Each has specific constraints on notation, extensions, and allowed characters.
   * - **Files**
     - Asset stored in filesystem, often with an extension.
     - Flexible labeling; extensions allowed; hyphens and subdomains permitted; e.g., `'usgs_landsat8_b01_brazil_20250607.tif'`.
   * - **Fields**
     - Columns in datasets or databases.
     - Stricter notation: only ASCII letters, numbers, underscore; hyphens prohibited; e.g., `'population_mean'`.
   * - **Layers**
     - Intermediate assets: database tables, GIS layers, drawing layers.
     - Restricted notation like fields; no extensions; hyphens discouraged.
   * - **Names**
     - Predefined vocabulary for common variables, statistics, and domains.
     - Supports long and short mode; reduces ambiguity; improves consistency; e.g., ``population`` / ``pop``, ``sum``, ``mean``.


.. _concepts-labels:

Labels
============================================

The core concept in ``FLARE`` is the **label**. A label is a plain text string used to identify an **asset** in a way that is both human-readable and machine-actionable. 

Unlike metadata that sits inside a file, the label itself **encodes** essential descriptive information directly in the asset name. This makes labels stand-alone identifiers: they can be read without opening the file and can be used by scripts for filtering, indexing, or automation.

.. _concepts-labels-domain:

Domain
---------------------------------------------

Labels follow a **hierarchical structure**, where information is organized into ordered parts. Each part represents a **domain** of information and domains are always read from **left to right**, with the most important domain on the left and the least important on the right. This ordering principle applies at all levels of detail: from domains to **subdomains** and down to components. 

.. dropdown:: Example
    :icon: code
    :open:

    .. code-block:: none
    
       {domain1}_{subdomain1-subdomain2}_{domain3}

.. _concepts-labels-underscore:

Underscore
---------------------------------------------

Underscore ``_`` is the **domain separator**. It is used to split the **domains of information** in the label.

.. dropdown:: Example
    :icon: code
    :open:

    .. code-block:: none

       {domain1}_{domain2}_{domain3}_{domain4}

.. _concepts-labels-hyphen:

Hyphen
---------------------------------------------

Hyphen ``-`` is the **subdomain separator**. It applies only in specific cases, such as breaking down a domain into finer parts of **subdomains**. 

.. dropdown:: Example
    :icon: code
    :open:

    .. code-block:: none

       {domain1}_{subdomain1-subdomain2}_{domain3}


.. important::

    Hyphen separator is optional and sometimes prohibited (e.g., in database field names).

.. _concepts-components:

Components
============================================

TODO explain a bit

.. _concepts-flags:

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


.. _concepts-numbers:

Numbers
---------------------------------------------

Numbers are a core component, since they are present in nearly every type of label.
``FLARE`` provides a structured approach to encoding **integer numbers, real numbers, signals, and magnitude multipliers**.
Each type has a specific role and format within a label.

.. seealso::

    Get more details on :ref:`Numbers <numbers>` documentation page.


.. _concepts-datetime:

Date and Time
---------------------------------------------

Date and Time (aka **datetime**) is a fundamental component, since nearly most labels require temporal reference.
To cover different use cases, ``FLARE`` provides two main **domains** of temporal encoding:

* **Timestamp** -- instant records of the timeline.
* **Epoch** -- arbitrary time interval of the timeline.

.. seealso::

    Get more details on :ref:`Date and Time <datetime>` documentation page.

.. _concepts-names:

Names
---------------------------------------------

Standard names as a way to simplify and harmonize labeling, so these are important components.

Standard names provide users with a predefined vocabulary for common domains and variables,
so that they can label assets without constantly reinventing terms.

A standard name is often used in contexts where certain terms occur repeatedly,
such as **scientific variables** in datasets or **statistics** applied to them.

.. dropdown:: Example
    :icon: info
    :open:

    Population is a common variable in demographic studies. ``FLARE`` can define ``population`` as a
    standard name, while also allowing a **short mode** like ``pop`` when brevity is required.


.. seealso::

    Get more details on :ref:`Names <names>` documentation page.


.. _concepts-assets:

Assets
============================================

In ``FLARE``, the term **asset** refers to anything that can be labeled.
Assets are the objects of labeling: the things for which a label provides meaning.

.. _concepts-assets-files:

Files
---------------------------------------------

The most obvious type of asset is the **file**.

Files are the classic case: they live in the file system, they carry **extensions** (e.g., ``.csv``, ``.pdf``, ``.png``)
that indicate their structure, and they are usually the first candidates for labeling.

File labels benefit from extensions because they add information about the internal format directly to the name.
Within files, there can still be **categories** (for example, documents, images, datasets),
and these may sometimes call for specialized labeling styles.

.. dropdown:: Example of labeling as raster file
    :icon: info
    :open:
    
    .. code-block:: none
    
       'usgs_landsat8_b01_brazil_20250607.tif'

.. seealso::

    Get more details on :ref:`Files <files>` documentation page.

.. _concepts-assets-fields:

Fields
---------------------------------------------

Another important type of asset is the **field**. Fields are the **column names** of tables in a database or dataset. 

When working with complex databases, relational models, or analytical workflows,
fields become central assets that must be labeled consistently. Unlike files,
fields do not have extensions, and their notation is stricter.

.. warning:: Hyphens in fields are prohibited

    Hyphens in fields are prohibited, and the recommended characters are limited to ASCII letters,
    numbers, and underscores. This ensures maximum compatibility across database systems.


.. dropdown:: Example of labeling of a table field
    :icon: info
    :open:

    .. code-block:: none
    
       'population_mean'

.. _concepts-assets-layers:

Layers
---------------------------------------------

Between files and fields, there is a large set of **intermediate assets**, which ``FLARE`` refers to as **layers**. 

Layers can appear in different contexts: database schemas, database tables, GIS vector layers, or any asset that contain multiple labeled divisions. Layers are not files in the filesystem, but they are not atomic fields either—they occupy the middle ground. 

Layers do not carry extensions and the use of hyphens is discouraged. Their labels must remain plain, unambiguous, and strictly ASCII-based.

