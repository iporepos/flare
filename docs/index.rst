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

.. card-carousel:: 1

    .. card:: Numbers
        :link: numbers
        :link-type: ref

        .. list-table::
           :widths: 30 30
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

        :bdg-primary-line:`see more`

    .. card:: Timestamps and Epochs
        :link: datetime
        :link-type: ref

        .. list-table::
           :widths: 30 50
           :header-rows: 1

           * - Encoded
             - Decoded
           * - ``20140302``
             - 2014-03-02
           * - ``20140302T124804P1ZW0300``
             - 2014-03-02 12:48:04.1 -03:00
           * - ``20140302u20140305``
             - 2014-03-02 :math:`\rightarrow` 2014-03-05

        :bdg-primary-line:`see more`

    .. card:: Literal Flags
        :link: flags
        :link-type: ref

        .. list-table::
           :widths: 30 50
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

        :bdg-primary-line:`see more`

    .. card:: Standard Names
        :link: names
        :link-type: ref

        .. list-table::
           :widths: 30 50
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

        :bdg-primary-line:`see more`

    .. card:: card 5

    .. card:: card 6


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
