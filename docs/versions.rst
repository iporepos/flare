.. _versions:

Versions
############################################

Versions are a structural component of all labels associated with assets whose state evolves over time.
They provide an interpretable mechanism for expressing change, maturity, and ordering across
successive releases.

Within the ``FLARE`` specification, version schemes must be deterministic, machine-readable, and easy to compare.
To accommodate different operational contexts, ``FLARE`` standardizes three complementary versioning schemes:
semantic versioning, compact semantic versioning, and timestamp-based versioning.

.. _versions-summary:

Summary
============================================

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Scheme
     - Canonical Pattern
     - Description
   * - **Semantic Versioning**
     - ``{major}.{minor}.{patch}``
     - Industry-standard versioning model emphasizing compatibility, stability, and explicit change semantics. Suitable for APIs, libraries, and stable interfaces.
   * - **Semantic Versioning (Compact)**
     - ``v{major}{minor}{patch}``
     - Four-character compact encoding (``v`` + three digits). Constrained to single-digit domains (0–9 for each component). Intended for short identifiers in resource-limited contexts.
   * - **Timestamp Versioning**
     - ``v{timestamp}``
     - Chronologically ordered versioning based on a timestamp with at least second-level resolution. Structured or unstructured formats are allowed, including zoned timestamps.


.. _versions-semantic:

Semantic Versioning
============================================

`Semantic Versioning <https://semver.org/>`_ is a widely adopted versioning standard used to communicate the
evolution, stability, and compatibility of an API or system. It provides a deterministic and interpretable structure,
helping users understand the impact of a release and anticipate integration risks.

A semantic version follows the canonical structure:

.. code-block:: none

    {major}.{minor}.{patch}

with the following rules:

1. **major**
   Non-negative integer incremented when introducing changes that break backward compatibility.

2. **minor**
   Non-negative integer incremented when adding new functionality in a backward-compatible manner.

3. **patch**
   Non-negative integer incremented when applying backward-compatible bug fixes.

A version with **major = 0** (e.g., ``0.0.1``) denotes an unstable development phase in which public interfaces may
change frequently and without notice.

.. seealso::

    Read more about the Semantic Versioning at https://semver.org/

.. _versions-semantic-compact:

Semantic Versioning Compact
============================================

``FLARE`` supports a compact semantic versioning variant in which the separating dots are omitted and the version
string is prefixed with ``v``. This produces a shorter, strictly numeric representation while preserving the underlying
semantic structure.

The canonical compact representation is:

.. code-block:: none

    v{major}{minor}{patch}

.. note::

    Compact flavor of semantic versioning in ``FLARE``

    .. code-block:: none

        '1.0.3'  =  'v103'

.. warning::

    Compact versioning is restricted to **single-digit domains**.
    The compact form is strictly 4 characters long (``v`` + three digits).
    As a consequence:

    - ``major`` must be in the range 0–9
    - ``minor`` must be in the range 0–9
    - ``patch`` must be in the range 0–9

    Values above 9 (e.g., ``10`` or ``11`` for ``minor`` or ``patch``) cannot be encoded in compact form.
    In such cases, the full semantic notation (``major.minor.patch``) must be used.

.. _versions-timestamp:

Timestamp Versioning
============================================

Timestamp-based versioning assigns versions according to the precise moment an artifact is created or released. This
approach is particularly suited for automated workflows, continuous integration pipelines, and environments in which
chronological ordering is more informative than semantic increments.

A timestamp version in ``FLARE`` is any string that encodes a **timestamp with at least day-level resolution**.
The format may be zoned or un-zoned, compact or extended, and may include separators or timezone indicators.

A canonical representation is:

.. code-block:: none

    v{timestamp}


.. seealso::

    Get more details about timestamps on :ref:`Date and Time <datetime>` documentation page.