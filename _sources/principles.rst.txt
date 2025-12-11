.. _principles:

Principles
############################################

``FLARE`` is based on a set of **core principles** that define how labels are created and interpreted.
These principles ensure that labels are **robust, consistent, human-readable, and machine-actionable**.

.. seealso::

    Check out the :ref:`Reference <reference>` page for all technical details.


.. _principles-summary:

Summary
============================================

.. list-table::
   :widths: 20 50 30
   :header-rows: 1

   * - Principle
     - Rule
     - Example
   * - Stand-alone information
     - Labels must encode essential information
     - ``project_dataset_2025_v2``
   * - Text-based
     - Only ASCII letters, numbers, ``_``, and ``-`` allowed
     - ``experiment_trial_01``
   * - Hierarchy and separators
     - ``_`` = primary separator, ``-`` = secondary, literal flags for edge cases
     - ``temperature_36P5_celsius``
   * - Case-insensitive
     - Casing has no effect; all labels are parsed as lowercase
     - ``DATASET_V2`` = ``Dataset_V2``


.. _principles-information:

Stand-alone information
============================================

Labels must encode **stand-alone information** relevant for identification and retrieval.
Even when metadata exists inside the asset (e.g., EXIF in images, metadata in PDFs, etc), the **label itself must carry enough descriptive information**.

* A label should be readable by a human without opening the file.
* A script should be able to retrieve or filter assets **based only on the label**.
* Labels reduce ambiguity by encoding essential descriptive elements (e.g., dataset, date, version, type).
* File storage space for naming is used as a meaningful metadata channel.

.. _principles-text:

Text-based
============================================

Every label is a **plain text string** in `ASCII <https://www.ascii-code.com/>`_ format, built from a restricted character set.

* Allowed characters:
    * **Letters**: ``abcdefghijklmnopqrstuvxywz``
    * **Numbers**: ``0123456789``
    * **Underscore:** ``_``
    * **Hyphen**: ``-``

* Prohibited characters:
    * All other ASCII special characters: ``.,:;!?@#$%&*+=/\|[]{}()^~'"``
    * Spaces and accented characters
    * Non-ASCII characters

This ensures **cross-platform portability** and avoids naming issues in operating systems, databases, and scripts.

.. _principles-hyerarchy:

Hierarchy
============================================

Information in ``FLARE`` is structured in a hierarchy of three levels:

1. **domain**: major level of information;
2. **subdomain**: minor level of information;
3. **component**: finer detail of information

``FLARE`` uses standard reserved characters for structuring information with separators and literal flags. This system ensures that labels are **unambiguous, consistent, and easy to parse**,
while still allowing flexibility for specialized encodings.


.. _principles-case:

Case-insensitivity
============================================

``FLARE`` is a **case-insensitive system**.

* A label is considered the **same**, regardless of whether it is written in lowercase, UPPERCASE, camelCase, or any other casing style.
* Internally, ``FLARE`` normalizes all labels to **lowercase** (snakecase) for retrieval, formatting, and automated processes.
* Non-snakecase are optional for convencience (human-readability) sometimes prohibited (e.g., in database field names).
* Every unique label is therefore **case-insensitive** by definition.

.. dropdown:: Example
    :icon: info
    :open:

    .. code-block:: none

       Project_Dataset_2025
       project_dataset_2025
       PROJECT_DATASET_2025
       Project_Dataset_2025