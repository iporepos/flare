.. _datetime:

Date and Time
############################################

Date and Time (aka **datetime**) is a fundamental component, since nearly most labels require temporal reference.
To cover different use cases, ``FLARE`` provides two main **domains** of temporal encoding:

* **Timestamp** -- instant records of the timeline.
* **Epoch** -- arbitrary time interval of the timeline.

.. seealso::

    See also the ``FLARE`` system for :ref:`Number <numbers>`.

.. _datetime-summary:

Summary
============================================

.. list-table::
   :widths: 15 30 30 25
   :header-rows: 1

   * - Domain
     - Structure / Signature
     - Example Encoded
     - Example Decoded
   * - Timestamp
     - YYYY[MM[DD[thhmmss[zshhmm]]]]
     - ``20140302t124804zw0300``
     - 2014-03-02 12:48:04 -03:00
   * - Epoch
     - ``{timestamp_start}u{timestamp_stop}``
     - ``20140302u20140305``
     - 2014-03-02 :math:`\rightarrow` 2014-03-05 (end excl.)

.. _datetime-timestamp:

Timestamp
============================================

A **timestamp** represent a precise record of a date and/or time. 

Timestamps are usually part of a **timeseries**, where each entry is valid until the next timestamp occurs. In this sense, the ``FLARE`` system is mostly based on the `ISO 8601 standard <https://en.wikipedia.org/wiki/ISO_8601>`_.

The table below show all variants of timestamps.

.. list-table::
   :widths: 25 15 30 15 15
   :header-rows: 1

   * - Variant
     - Alias
     - Signature
     - Length (chars)
     - Pattern
   * - Full
     - ``ts``
     - ``YYYYMMDDthhmmsszshhmm``
     - :math:`\ge` 21
     - ``*t*z*``
   * - Full human
     - ``tsh``
     - ``YYYY-MM-DD-thhmmss-zshhmm``
     - :math:`\ge` 25
     - ``*-*-t*-z*``
   * - Un-zoned
     - ``tsu``
     - ``YYYYMMDDthhmmss``
     - :math:`\ge` 15
     - ``*t*``
   * - Un-zoned human
     - ``tsuh``
     - ``YYYY-MM-DD-thhmmss``
     - :math:`\ge` 18
     - ``*-*-*-t*``
   * - Daily
     - ``tsd``
     - ``YYYYMMDD``
     - 8
     - ``*``
   * - Daily human
     - ``tsdh``
     - ``YYYY-MM-DD``
     - 10
     - ``*-*-*``
   * - Monthly
     - ``tsm``
     - ``YYYYMM``
     - 6
     - ``*``
   * - Monthly human
     - ``tsmh``
     - ``YYYY-MM``
     - 7
     - ``*-*``
   * - Yearly
     - ``tsy``
     - ``YYYY``
     - 4
     - ``*``

.. _datetime-timestamp-structure:

Structure
--------------------------------------------

The structure of a **full timestamp** is composed of three main subdomains:

.. code-block:: none

   {date}t{time}z{zone}

The **time** subdomain is prefixed by the flag ``t``. 
The **zone** subdomain prefixed by the flag ``z``.


.. _datetime-timestamp-date:

Date
--------------------------------------------

The date subdomain is encoded as the following components:

.. code-block:: none

   {year}{month}{day} = YYYYMMDD

Where:

* year (``YYYY``) = 4 digits integer number;
* month (``MM``) = 2 digits integer number;
* day (``DD``)= 2 digits integer number.

.. _datetime-timestamp-time:

Time
--------------------------------------------

The time subdomain is encoded as the following components:

.. code-block:: none

   {hour}{minute}{second} = hhmmss

Where:

* hour (``hh``) = 2 digits integer number;
* minute (``mm``) = 2 digits integer number;
* second (``ss``)= 2 digits integer number or (optional) real number with 2 digits for the integer part.

Hours and minutes are always 2 digits integers. Seconds have at least 2 digits but may optionally include decimals.

.. _datetime-timestamp-zone:

Zone
--------------------------------------------

The zone subdomain is a timezone offset from `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_. It has a `signal prefix <https://github.com/ipo-exe/flare/blob/main/docs/numbers.md#signal>`_ (``w/e`` or ``s/n``) and an offset in ``{hour}{minute}``.

.. code-block:: none

   {sign}{hour}{minute} = shhmmss

.. _datetime-timestamp-human:

Human-readable mode
--------------------------------------------

**Human-readable mode** allows insertion of hyphens (``-``) between timestamp components
and in the subcomponents of **date** to improve readability:

.. code-block:: none

   YYYY-MM-DD-thhmmss-zshhmm

.. _datetime-timestamp-examples:

Examples
--------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Encoded
     - Decoded (ISO 8601)
   * - ``20140302t124804p143zw0300``
     - 2014-03-02 12:48:04.143 -03:00
   * - ``20140302t124804``
     - 2014-03-02 12:48:04 (no zone)
   * - ``2014-03-02-T124804``
     - 2014-03-02 12:48:04 (no zone)
   * - ``20140302``
     - 2014-03-02 (daily)
   * - ``2014-03``
     - 2014-03 (monthly)
   * - ``2014``
     - 2014 (yearly)


.. _datetime-epoch:

Epoch
============================================

An **Epoch** represent any arbitrary interval between a start and end point in the timeline. These are used when the temporal span must be explicitly delimited.

.. _datetime-structure:

Structure
--------------------------------------------

The epoch is simply a concatenation of two timestamps denoting the interval. 
The flag for separator is the ``u`` letter, denoting the "union":

.. code-block:: none

   {timestamp_start}u{timestamp_stop}

Where:

* ``timestamp_start`` is the starting time of the interval (inclusive lower limit);
* ``timestamp_stop`` is the stopping time of the interval (exclusive upper limit).

.. note:: 

    By *exclusive upper limit* ``FLARE`` means that at that moment the epoch is no longer valid. Hence, in an epoch of ``2020u2030`` the year 2030 is not included.

.. _datetime-epoch-examples:

Examples
--------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Encoded
     - Decoded
   * - ``20140302t124804u20140302t134804``
     - 2014-03-02 12:48:04 :math:`\rightarrow` 2014-03-02 13:48:04
   * - ``20140302u20140305``
     - 2014-03-02 :math:`\rightarrow` 2014-03-05 (daily interval)
   * - ``2014-03u2014-04``
     - 2014-03 :math:`\rightarrow` 2014-04 (monthly interval)
   * - ``2014U2015``
     - 2014 :math:`\rightarrow` 2015 (yearly interval)
   * - ``20140302t124804p143zw0300u20140302t134804zw0300``
     - 2014-03-02 12:48:04.143 -03:00 :math:`\rightarrow` 2014-03-02 13:48:04 -03:00


.. _datetime-flags:

Literal Flags
============================================

.. list-table::
   :widths: 15 25 25 35
   :header-rows: 1

   * - Flag
     - Domain
     - Subdomain
     - Meaning
   * - ``t``
     - Timestamp
     - Time
     - Prefix for time notation
   * - ``z``
     - Timestamp
     - Zone
     - Prefix for zone notation
   * - ``u``
     - Epoch
     - Stop
     - Separator of timestamps