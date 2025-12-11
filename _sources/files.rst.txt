.. _files:

.. note::

    This page is being developed.

Files
############################################

A file is the most obvious kind of asset in the ``FLARE`` system.

Files live in the file system of the computer, they carry an **extension suffix** (e.g., ``.csv``, ``.pdf``, ``.png``)
that indicate their structure, and they are usually the first candidates for labeling.

File labels benefit from extensions suffix because they add information about the internal format directly to the name.
Within files, there can still be broad file **categories** (for example, Documents, Images, Datasets),
and these may sometimes call for specialized labeling structures.

.. _files-labeling:

Labeling Schemes
=============================================

A labeling scheme defines the canonical structure of a file label, ensuring that
assets remain uniquely identifiable, interpretable, and easy to organize across
projects. ``FLARE`` currently supports two complementary schemes:

1. **Generic Scheme** — a versatile, multi-domain label suitable for versioned assets
   associated with projects, workflows, or operational documents.

2. **Reference Scheme** — a compact and human-readable convention tailored to
   bibliographic or publication-related assets (e.g., PDFs, BibTeX sources, reports).

Both schemes are designed to be deterministic, machine-parsable, and suitable for
large, heterogeneous collections of files.

.. _files-labeling-generic:

Generic Scheme
---------------------------------------------

The **generic scheme** is intended for general-purpose organizational use across
projects, deliverables, and operational artifacts.

The canonical representation is:

.. code-block:: none

    {type}_{project}_{item}_{version}_{suffix}

It encodes five domains:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Domain
     - Abstract
   * - ``type``
     - The nature of the file (e.g., ``report``, ``contract``, ``dataset``).
   * - project
     - A higher-level domain representing the project or overarching activity. Often an alphanumeric project code.
   * - ``item``
     - A lower-level domain nested within the project. Useful for representing components such as sub-tasks, contracts, proposals, or any subordinate classification.
   * - ``version``
     - Any version expressed using one of the supported versioning schemes (semantic, compact semantic, or timestamp).
   * - ``suffix``
     - An optional convenience tag. May be empty (``X``) or encode workflow states such as ``signed``, ``todo``, ``draft``, or other operational flags.


.. dropdown:: Example with semantic versioning
    :open:
    :icon: info

    .. code-block:: none

        REPORT_A002_F005_V002_X.pdf

.. dropdown:: Example with timestamp versioning
    :open:
    :icon: info

    .. code-block:: none

        CONTRACT_A002_F002_V20250314_signed.pdf

.. seealso::

    See :ref:`Versions <versions>` for details on supported version structures.

.. _files-labeling-reference:

Reference Scheme
---------------------------------------------

The **reference scheme** provides a cleaner and more human-readable labeling
standard for citable or publication-oriented assets, including:

- academic publications
- institutional reports
- datasets with bibliographic metadata
- BibTeX files
- digital repository entries

The canonical representation of the reference scheme is:

.. code-block:: none

    {author}_{year}_{item}

It encodes three domains:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Domain
     - Abstract
   * - ``author``
     - The primary author surname, institutional acronym, or a standard alias. Institutions with long formal names should use a short, interpretable acronym.
   * - ``year``
     - The four-digit publication or release year.
   * - ``item``
     - A disambiguation token (``a``, ``b``, ``c``...) used when the same author publishes multiple items in the same year.


.. dropdown:: Example of human author reference
    :open:
    :icon: info

    Here a 3 files are grouped for the document, the citation file and the notes.

    .. code-block:: none

        Smith_2021_a.pdf
        Smith_2021_a.bib
        Smith_2021_a.md

.. dropdown:: Example for institution author
    :open:
    :icon: info

    .. code-block:: none

        NOAA_2005_a.pdf
        EPA_1995_a.pdf


.. _files-labeling-dataset:

Dataset Scheme
---------------------------------------------

The ``dataset`` scheme is designed for structured data assets whose naming must capture provenance,
product family, spatial context, and temporal reference. It is particularly suitable for geospatial,
scientific, and observational datasets in which multiple dimensions of specificity are required for
clear identification and reproducibility.

The canonical representation of the dataset scheme is:

.. code-block:: none

    {source}_{collection}_{item}_{specs}_{extent}_{datetime}

It encodes six domains:

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Domain
     - Description

   * - ``source``
     - The data provider or originator. This may be an agency (e.g., ``USGS``, ``COPERNICUS``),
       a space agency mission (e.g., ``NASA``), or any authoritative institutional source.

   * - ``collection``
     - The name, code or id for dataset family, product line, or collection. Examples include
       satellite missions (``Landsat08``), model outputs, or named product groups.

   * - ``item``
     - The name, code or id for a self-contained data asset within the collection. Often corresponds to an individual file,
       granule, tile, or sub-product.

   * - ``specs``
     - An optional specification domain for additional qualifiers. Useful for encoding
       coordinate system, spatial or temporal resolution, algorithm variant, processing level,
       or any other descriptive modifier. May be left empty (e.g., ``x`` or ``o``) when obvious.

   * - ``extent``
     - A spatial reference describing the geographical scope of the data. May include bounding boxes,
       coordinate tuples, tile identifiers, region codes, administrative names (e.g., county or city),
       or other spatial identifiers. May be left empty (e.g., ``x`` or ``o``) when obvious.

   * - ``datetime``
     - A temporal reference marking the acquisition, validity, or observation period. Any timestamp or
       epoch is valid. May be left empty (e.g., ``x`` or ``o``) when obvious.


.. dropdown:: Example of raster tile labeling
    :open:
    :icon: info

    Here is shown a tile of the Copernicus DEM  collection stored in ``tif`` format and labeled in ``FLARE`` dataset scheme

    .. code-block:: none

        COPERNICUS_COPDEM_GLO30_DGTE_S030W051_20111008T182325.tif


.. dropdown:: Example of a time series table labeling
    :open:
    :icon: info

    Here is shown a time series from station ``A001`` of the Brazilian Meteorological Institute
    in ``txt`` format and labeled in ``FLARE`` dataset scheme.
    Note that extension is considered obvious from the metadata.

    .. code-block:: none

        INMET_AUTO_A001_T0_0_2000U2020.txt

    The same data but aggregated over the monthly time step would be:

    .. code-block:: none

        INMET_AUTO_A001_T0-M_0_2000U2020.txt

    The same data but aggregated over the yearly time step would be:

    .. code-block:: none

        INMET_AUTO_A001_T0-Y_0_2000U2020.txt

File Types and Themes
=============================================

``FLARE`` adopts and extends the ``BibLaTeX`` classification of entry types to support a unified
taxonomy for labeling files. The goal is to provide a structured and interoperable set of
“file themes” that align with bibliographic conventions while accommodating operational,
administrative, and research-oriented assets that fall outside the classical bibliographic scope.

.. seealso::

    Check out ``BibLaTeX`` documentation at https://ctan.org/pkg/biblatex

The taxonomy is divided into two groups:

1. **Bibliographic File Types**
   Directly compatible with standard ``BibLaTeX`` entry types.

2. **Extended File Types**
   Additional categories introduced by ``FLARE``.
   Most of these map to ``misc`` in ``BibLaTeX`` unless otherwise specified.

This structure allows FLARE labels to be both semantically expressive and compatible with citation
workflows when needed.

Bibliographic File Types
---------------------------------------------

These categories correspond directly to commonly used ``BibLaTeX`` entry types:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Type
     - Abstract
   * - ``report``
     - Technical or institutional reports.
   * - ``article``
     - Journal or magazine articles.
   * - ``inproceedings``
     - Conference proceedings papers.
   * - ``book``
     - Monographs, volumes, or edited books.
   * - ``legal``
     - Legal decisions, legislation summaries, legal opinions.
   * - ``legislation``
     - Formal legislative documents.
   * - ``dataset``
     - Publications that are datasets in the bibliographic sense.
   * - ``thesis``
     - Academic theses and dissertations.
   * - ``manual``
     - User guides, specifications, operational manuals.
   * - ``misc``
     - Generic documents that do not fit a more specific class.

Extended File Types
---------------------------------------------

These categories expand the ``BibLaTeX`` model to accommodate operational, administrative,
and research documentation. Unless otherwise stated, these are represented as ``misc`` in
``BibLaTeX``.

Accounting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Type
     - Abstract
   * - ``statement``
     - Bank account statements and financial extracts.
   * - ``invoice``
     - Invoices and billing documents.
   * - ``receipt``
     - Payment receipts and declarations.
   * - ``fiscal``
     - Fiscal documents, tax declarations, and revenue records.
   * - ``proof``
     - Proof-of-payment documents.

Administrative
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Type
     - Abstract
   * - ``contract``
     - Legal or informal agreements. Maps to ``legal`` in ``BibLaTeX``.
   * - ``proposal``
     - Technical or commercial proposals. Maps to ``legal`` in ``BibLaTeX``.
   * - ``paperwork``
     - General administrative documentation. Maps to ``misc`` in ``BibLaTeX``.
   * - ``ticket``
     - Transfer and flight tickets, or service tickets. Maps to ``misc`` in ``BibLaTeX``.

Research and Academic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Type
     - Abstract
   * - ``poster``
     - Research posters, infographics, and academic displays. Maps to ``inproceedings`` in ``BibLaTeX``.
   * - ``presentation``
     - Slide decks and conference presentations. Maps to ``misc`` in ``BibLaTeX``.

.. warning::

    CONTINUE HERE ``FLARE`` continues to support extension of this taxonomy.
    You may add new file themes under the appropriate group or introduce new groups as project needs evolve.


.. _files-categories:

File Categories
=============================================

.. _files-documents:

Documents
---------------------------------------------

Documents represent a broad class of files whose primary purpose is to organize and communicate human-readable information.
They range from reflowable digital publications to structured, fully editable office documents.
In the ``FLARE`` labeling system, document extensions play a critical role because they determine whether the content
is static (e.g., ``.pdf``) or editable (e.g., ``.docx``, ``.odt``, ``.xlsx``), as well as the underlying format
family (Open XML, OpenDocument Format, EPUB, etc.).

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Extension
     - Name
     - Abstract

   * - ``pdf``
     - Portable Document Format
     - Non-editable or semi-editable fixed-layout document format designed for reliable rendering across platforms; commonly used for reports, publications, and finalized documents.

   * - ``epub``
     - Electronic Publication
     - Reflowable digital book format based on XHTML/CSS; widely used for long-form content such as books and manuals.

   * - ``svg``
     - Scalable Vector Graphics
     - XML-based vector format for diagrams, illustrations, and technical graphics; resolution-independent and editable in text or vector editors.

   * - ``ai``
     - Adobe Illustrator Artwork
     - Proprietary vector-graphics format used for illustrations, logos, and design assets; supports layers, paths, and advanced styling.

   * - ``docx``
     - Microsoft Word Document (Open XML)
     - Editable, structured word-processing file format supporting text, styles, embedded media, and revision history.

   * - ``odt``
     - OpenDocument Text
     - Open-standard, editable word-processing format native to LibreOffice and other ODF-compatible editors.

   * - ``xlsx``
     - Microsoft Excel Workbook (Open XML)
     - Editable spreadsheet format using tabular structures, formulas, chart definitions, and embedded metadata.

   * - ``ods``
     - OpenDocument Spreadsheet
     - Open-standard spreadsheet format used by LibreOffice; supports formulas, styles, and structured data.

   * - ``pptx``
     - Microsoft PowerPoint Presentation (Open XML)
     - Editable slide-based presentation format supporting layouts, animations, embedded media, and templates.

   * - ``odp``
     - OpenDocument Presentation
     - Open-standard presentation format used by LibreOffice; compatible with open-source office environments.


.. _files-images:

Images
---------------------------------------------

Images encompass raster files whose primary purpose is to represent visual or spatial information in a pixel-based structure.
Depending on the format, images may be optimized for human perception (photographs, graphics) or for analytical processing (scientific rasters, georeferenced grids).
The presence and richness of metadata—such as EXIF tags or geospatial references—significantly affect how such files should be labeled and managed in the ``FLARE`` system.

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Extension
     - Name
     - Abstract

   * - ``jpg``
     - Joint Photographic Experts Group Short Variant
     - Lossy-compressed raster image format widely used for photographs; supports EXIF metadata such as timestamps, camera parameters, and geolocation.

   * - ``png``
     - Portable Network Graphics
     - Lossless raster image format supporting transparency (alpha channels); commonly used for diagrams, web graphics, and high-quality figures.

   * - ``gif``
     - Graphics Interchange Format
     - Indexed-color raster format supporting simple animation; limited color depth but efficient for small graphical assets.

   * - ``tif``
     - Tagged Image File Format
     - Flexible raster container supporting multiple compression schemes; includes metadata tags and is common in professional imaging and scientific datasets.

   * - ``bmp``
     - Bitmap Image
     - Uncompressed raster format with simple structure; primarily encountered in legacy systems or specialized workflows.

   * - ``webp``
     - WebP Image
     - Modern image format supporting both lossy and lossless compression, animations, and alpha channels; optimized for web delivery.

.. _files-datasets:

Datasets
---------------------------------------------

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Extension
     - Name
     - Abstract

   * - ``csv``
     - Comma-Separated Values
     - Plain-text tabular data format with delimited fields; widely used for interoperability but limited metadata support.

   * - ``txt``
     - Tabular Text File
     - Plain-text dataset encoded with tab or custom delimiters; flexible but with no native schema or typing.

   * - ``geojson``
     - GeoJSON
     - JSON-based format for geospatial vector data; supports geometries, properties, and coordinate reference metadata.

   * - ``xml``
     - Extensible Markup Language
     - Hierarchical markup for structured data interchange; widely used in configuration, metadata, and document formats.

   * - ``parquet``
     - Apache Parquet
     - Columnar, compressed dataset format optimized for analytical workloads; supports schema evolution and efficient querying.

   * - ``nc``
     - NetCDF
     - Multidimensional scientific data format with extensive metadata capabilities; used for atmospheric, oceanographic, and raster datasets.

   * - ``tif``
     - GeoTIFF Raster Dataset
     - Georeferenced raster format embedding coordinate reference systems and geospatial metadata; simultaneously an Image and Dataset.

   * - ``gpkg``
     - GeoPackage
     - SQLite-based, open-standard geospatial dataset container storing vector layers, raster tiles, and metadata in a single file.

   * - ``shp``
     - ESRI Shapefile
     - Legacy geospatial vector format requiring multiple companion files; stores geometries and attribute tables.

   * - ``kml``
     - Keyhole Markup Language
     - XML-based geospatial vector format used for map features, paths, and annotations; commonly used in web mapping and Google Earth.

   * - ``sqlite``
     - SQLite Database
     - File-based relational database storing tables, indexes, and arbitrary data structures; used for embedded or small-scale data storage.

.. _files-markup:

Markup
---------------------------------------------

Markup files define structure, formatting rules, or semantic annotations for text-based artifacts.
They are human-readable, usually plain text, and frequently used for documentation, web content, data serialization,
or academic references. Although they contain no executable logic, they often support rich rendering pipelines
and metadata systems that influence downstream applications.

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Extension
     - Name
     - Abstract

   * - ``md``
     - Markdown Document
     - Lightweight markup for structured text; commonly used for README files, documentation, and content pipelines.

   * - ``rst``
     - reStructuredText
     - Rich, extensible markup for technical documentation; native format for Sphinx (Python library).

   * - ``tex``
     - TeX File
     - Typesetting language used for scientific papers, reports, books, and mathematical documents.

   * - ``bib``
     - BibTeX Bibliography
     - Plain-text structured references used in LaTeX ecosystems; stores citations and bibliographic metadata.

   * - ``html``
     - HyperText Markup Language
     - Defines the structure and presentation of web documents; rendered by browsers and supports multimedia embedding.

   * - ``xml``
     - Extensible Markup Language
     - Hierarchical markup for structured data interchange; widely used in configuration, metadata, and document formats.

   * - ``json``
     - JavaScript Object Notation
     - Human-readable structured data interchange format supporting nested objects and arrays; suitable for hierarchical datasets.

   * - ``yaml``
     - Yet Another Markup Language
     - Human-friendly configuration format using indentation for structure; used in workflows, orchestration, and settings.

   * - ``toml``
     - Tom's Obvious, Minimal Language
     - Strongly typed, minimal configuration format used in packaging, environments, and application metadata.


.. _files-code:

Source Code
---------------------------------------------

Source code files contain executable instructions written in programming or scripting languages.
They express computational logic, automation routines, workflows, or analytical steps.
Although typically stored as plain text, their semantics depend on interpreters, compilers, and runtime environments.
These file are “active” assets: they initiate behavior, transformations, or computations when executed.

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Extension
     - Name
     - Abstract

   * - ``py``
     - Python File
     - Script or module executed by the Python interpreter for automation, analysis, or application logic.

   * - ``ipynb``
     - Jupyter Notebook
     - Interactive document mixing code, outputs, and metadata; used for exploratory computing.

   * - ``sh``
     - Shell Script
     - Unix shell commands for automation and environment setup, executed by Bash or related shells.

   * - ``bat``
     - Windows Batch Script
     - Command script for Windows environments; used for automation, file operations, and workflows.

   * - ``js``
     - JavaScript File
     - Script executed by browsers or Node.js; used for web applications or automation.