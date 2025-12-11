.. _home:

FLARE
############################################

.. adapt this welcoming message [CHANGE THIS]:

Welcome to ``FLARE`` documentation!

.. dropdown:: ``FLARE`` — *Formatting Labels for Archive and Retrieval Efficiency*
    :open:
    :color: warning
    :icon: flame

    ``FLARE`` is a system for creating and managing text-based labels.

    It provides conventions and nomenclature for labeling files, fields and layers,
    making them easier to organize, archive and retrieve.

Features
====================================

``FLARE`` offers a suite of features for formatting labels.

.. tab-set::

    .. tab-item:: Numbers

        Format integer numbers, real numbers, sign and magnitude multipliers using text and a few rules.

        .. list-table::
           :widths: auto
           :header-rows: 1

           * - Encoded
             - Decoded
           * - ``05P2``
             - :math:`+ 5.2`
           * - ``S02P33K``
             - :math:`- 2,330.0`
           * - ``n23p44c``
             - :math:`+ 2,344.0`
           * - ``W05P0M``
             - :math:`- 5,000,000.0`

        :ref:`See more <numbers>` :octicon:`link-external`

    .. tab-item:: Datetime

        Format timestamps records and epochs (periods) using a simple notation.

        .. list-table::
           :widths: auto
           :header-rows: 1

           * - Encoded
             - Decoded
           * - ``20140302``
             - 2014-03-02
           * - ``20140302T123401``
             - 2014-03-02 12:34:01
           * - ``20140302T124804P1ZW0300``
             - 2014-03-02 12:48:04.1 -03:00
           * - ``20140302u20140305``
             - 2014-03-02 :math:`\rightarrow` 2014-03-05

        :ref:`See more <datetime>` :octicon:`link-external`

    .. tab-item:: Literal Flags

        A set of reserved characters that encode conventional meaning.

        .. list-table::
           :widths: auto
           :header-rows: 1

           * - Flag
             - Meaning
           * - ``_``
             - Domain Separator
           * - ``-``
             - Subdomain Separator
           * - ``x``
             - Null value
           * - ``z``
             - Unknown value

        :ref:`See more <flags>` :octicon:`link-external`

    .. tab-item:: Versions

        Use versioning schemes suitable for assets that evolve over time.

        .. list-table::
           :widths: auto
           :header-rows: 1

           * - Scheme
             - Structure
             - Purpose
           * - Semantic
             - ``{major}.{minor}.{patch}``
             - Compatibility-oriented; communicates breaking changes, new features, and patches.
           * - Compact Semantic
             - ``v{major}{minor}{patch}`` (4 chars)
             - Space-saving variant; restricted to single-digit domains.
           * - Timestamp
             - ``v{timestamp}``
             - Chronological ordering using a timestamp.

        :ref:`See more <versions>` :octicon:`link-external`

    .. tab-item:: Standard Names

        A predefined vocabulary for common themes, so that you can make labels without constantly reinventing terms.

        .. list-table::
           :widths: auto
           :header-rows: 1

           * - Name
             - Title
           * - ``datetime``
             - Instant record
           * - ``id``
             - Primary Key
           * - ``mean``
             - Arithmetic mean
           * - ``tas``
             - Surface Air Temperature

        :ref:`See more <names>` :octicon:`link-external`

    .. tab-item:: Files

        Labeling schemes for files in different operational contexts.

        .. list-table::
           :widths: auto
           :header-rows: 1

           * - Scheme
             - Example

           * - Generic
             - ``REPORT_A002_F005_V002_X.pdf``

           * - Reference
             - ``Smith_2021_a.pdf``

           * - Dataset
             - ``COPERNICUS_COPDEM_GLO30_DGTE_S030W051_20111008T182325.tif``

        :ref:`See more <files>` :octicon:`link-external`


Contents
====================================

.. toctree::
   :maxdepth: 1

   Home <self>
   principles
   reference
   guide
   api
   development
