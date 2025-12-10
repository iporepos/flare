.. _flags:

Literal Flags
############################################

Literal Flags are **reserved characters** that encode a meaning within the domain of information.

.. dropdown:: Example
    :icon: info
    :open:

    The ``p`` letter is the flag encoding decimal separator in numbers:

    .. code-block:: none

       '003p46' = 3.46

.. _flags-separators:

Separators
============================================

As mentioned in :ref:`Concepts <concepts-labels>`, separators are flags that give the label structure.

.. dropdown:: Example of separators
    :icon: code
    :open:

    .. code-block:: none

       {domain1}_{subdomain1-subdomain2}_{domain3}

.. _flags-separators-domain:

Domain
---------------------------------------------

The domain separator is the **Underscore** ``_`` character. It splits the domains in a label.

.. _flags-separators-subdomain:

Subdomain
---------------------------------------------

The subdomain separator is the **Hyphen** ``-`` character. It splits the subdomains in a label domain.

.. _flags-domain-flags:

Domain Flags
============================================

Domain Flags are all flags that a given domain requires in a specific form.
It must be interpreted given the expected domain. For instance, if a domain
is expected to be a :ref:`Number <numbers>`, the ``p`` letter is the
flag encoding decimal separator.

.. seealso:: See the flags catalog table below.

.. _flags-replacers:

Replacers
============================================

Some flags are **replacers**, so they always carry the same meaning and replace all information in a label domain.

.. important:: Disambiguating Replacers and Domain Flags

    Replacers always appear **alone** within a domain. Although they may resemble
    other Domain Flags, their distinguishing feature is that they occur
    by themselves between underscores. This pattern is the indicator that the
    element is a replacer.

.. _flags-replacers-null:

Null
---------------------------------------------

The flag ``x`` is a replacer for any domain in a label that is null (void or empty).

.. _flags-replacers-unknown:

Unknown
---------------------------------------------

The flag ``z`` is a replacer for any domain in a label that unknown.

.. _flags-replacers-na:

Not-apply
---------------------------------------------

The flag ``n`` is a replacer for any domain in a label that somehow not apply, like an exception to the rule.

.. _flags-replacers-obvious:

Obvious
---------------------------------------------

The flag ``o`` is a replacer for any domain in a label that is somewhat obvious,
like it is described in the documentation or metadata files.
It's the lazy option for not filling everything. Use with caution.

.. _flags-catalog:

Flag Catalog
============================================

See below the full catalog of flags in ``FLARE``.

.. csv-table::
   :file: ./data/flags.csv
   :header-rows: 1
   :widths: auto
   :delim: ;