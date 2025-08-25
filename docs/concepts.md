# Concepts

Flare organizes its labeling system around a few **concepts** that define how labels are created, structured, and applied. Understanding these concepts helps users quickly grasp the logic of Flare and apply it consistently across files, fields, layers, code symbols, and variables. The main concepts include **Labels**, **Assets**, **Names**, and **Variables**, each with specific roles, structures, and rules that make labeling both human-readable and machine-actionable.

---

## Summary

| Concept        | Definition                                                                 | Key Features / Notes                                                                 |
|----------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Label**      | The primary identifier in Flare, a text string for naming an asset.       | Hierarchical; domains left-to-right; separators `_` and `-`; literal flags for compact info. |
| **Assets**      | Anything that can be labeled.                                             | Includes **Files**, **Fields**, **Layers**, and **Symbols**. Each has specific constraints on notation, extensions, and allowed characters. |
| **Files**       | Asset stored in filesystem, often with an extension.                      | Flexible labeling; extensions allowed; hyphens and subdomains permitted; e.g., `'usgs_landsat8_b01_brazil_20250607.tif'`. |
| **Fields**      | Columns in datasets or databases.                                         | Stricter notation: only ASCII letters, numbers, underscore; hyphens prohibited; e.g., `'population_mean'`. |
| **Layers**      | Intermediate assets: database tables, GIS layers, drawing layers.        | Restricted notation like fields; no extensions; hyphens discouraged. |
| **Symbols**     | Code identifiers: constants, functions, classes, and other objects.      | Follow hierarchical logic; hyphens prohibited; underscores used; snake_case recommended; e.g., `dc_files`. |
| **Names** | Predefined vocabulary for common variables, statistics, and domains. | Supports long and short mode; reduces ambiguity; improves consistency; e.g., `population` / `pop`, `sum`, `mean`. |
| **Variables**   | Data variables associated with topics, quantitative or qualitative.      | Can include suggested data types, compact modes with multipliers; ensures structured, machine-actionable encoding; e.g., `population` with multiplier for integer storage. |


---

## Labels

The core concept in Flare is the **label**. A label is a plain text string used to identify an **asset** in a way that is both human-readable and machine-actionable. Unlike metadata that sits inside a file, the label itself **encodes** essential descriptive information directly in the asset name. This makes labels stand-alone identifiers: they can be read without opening the file and can be used by scripts for filtering, indexing, or automation.

### Domain

Labels follow a **hierarchical structure**, where information is organized into ordered parts. Each part represents a **domain** of information and domains are always read from **left to right**, with the most important domain on the left and the least important on the right. This ordering principle applies at all levels of detail: from domains to **subdomains** and down to components.

```
{domain1}_{subdomain1-subdomain2}_{domain3}
```

### Separator

As mentioned in [principles](https://github.com/ipo-exe/flare/blob/main/docs/principles.md), domains are splitted by the **underscore** `_`, which is the top-level **separator**. Within a domain, subdomains may be further divided using the **hyphen** `-` when necessary (and allowed). This structured use of separators ensures that labels remain unambiguous and easy to parse. 

### Flags

**Literal flags** may add more structure to a label domain, also encoding information a compact way. For instance, in a domain of a [number](https://github.com/ipo-exe/flare/blob/main/docs/numbers.md), the letter `p` encodes the decimal separator of the integer and the fractional parts of a number:
```
'0P34' = 0.34
```

> See the [Flags](https://github.com/ipo-exe/flare/blob/main/docs/flags.md) documentation.

---

## Assets

In Flare, the term **asset** refers to anything that can be labeled. Assets are the objects of labeling: the things for which a label provides meaning. Because Flare is meant to be flexible and widely applicable, assets can take several forms inside the computer’s memory and storage.

### Files

The most obvious type of asset is the **file**. Files are the classic case: they live in the file system, they carry **extensions** (e.g., `.csv`, `.pdf`, `.png`) that indicate their structure, and they are usually the first candidates for labeling. File labels benefit from extensions because they add information about the internal format directly to the name. Within files, there can still be **subcategories** (for example, documents, images, datasets), and these may sometimes call for specialized labeling styles.

Example of labeling of a raster file:
```
'usgs_landsat8_b01_brazil_20250607.tif'
```

### Fields

Another important type of asset is the **field**. Fields are the **column names** of tables in a database or dataset. When working with complex databases, relational models, or analytical workflows, fields become central assets that must be labeled consistently. Unlike files, fields do not have extensions, and their notation is stricter. Hyphens are prohibited, and the recommended characters are limited to ASCII letters, numbers, and underscores. This ensures maximum compatibility across database systems.

Example of labeling of a table field:
```
'population_mean'
```

### Layers

Between files and fields, there is a large set of **intermediate assets**, which Flare refers to as **layers**. Layers can appear in different contexts: database schemas, database tables, GIS vector layers, or even drawing files that contain multiple stacked layers. They are not files in the filesystem, but they are not atomic fields either—they occupy the middle ground. Layers share the same restricted notation as fields: they do not carry extensions, and the use of hyphens is discouraged. Their labels must remain plain, unambiguous, and strictly ASCII-based.

### Symbols

Finally, Flare also applies to **symbols**, which are the identifiers used in code for static and dynamic structures in programming environments (constants, functions, classes, etc). While the exact naming rules for variables depend on the programming language, Flare provides a consistent approach to structuring variable names across contexts. Variables may follow the same hierarchical logic of domains and subdomains, allowing them to encode information in a structured way that remains human-readable and machine-actionable. Like fields, hyphens are not allowed in variables, as they are interpreted as subtraction operators in most languages. 

Example of labeling of a dictionary in Python:
```python
dc_files = {"a": "C:/report_2025.pdf"} 
```

---

## Names

Flare supports the use of **standard names** as a way to simplify and harmonize labeling. Standard names provide users with a predefined vocabulary for common domains and variables, so that they can label assets without constantly reinventing terms. This reduces ambiguity, saves time, and promotes consistency across projects.

A standard name is often used in contexts where certain terms occur repeatedly, such as **variables** in datasets or **statistics** applied to them. For example, population is a common variable in demographic studies. Flare can define `population` as a standard name, while also allowing a **short mode** like `pop` when brevity is required. In the same way, statistics can also be standardized: `sum`, `mean`, or `std` (for standard deviation) may be used consistently across labels.

Standard names therefore support both **long mode** (descriptive and explicit) and **short mode** (compact and space-saving). Both forms are valid within Flare, as long as they remain unambiguous within the labeling context.

Variable:  
  - `population` → long mode  
  - `pop` → short mode  

Statistics:  
  - `sum`, `mean`, `std`  
  - Combined: `pop_2010_mean`  

---

## Variables

Variables are a central concept in Flare, and standard names play a key role in making them consistent and easily interpretable. Each variable is associated with a **topic**, which represents the kind of information it carries, whether **quantitative** (numeric measures) or **qualitative** (categorical information). Standard names can include suggested **data types** for storing the variable in fields or files, ensuring that datasets are created and encoded consistently across projects. 

Flare also allows **compact modes for data types**: for example, numeric values can be stored as integers together with a **multiplier**. The multiplier enables efficient storage while preserving the actual value range, since the stored integer can be divided by the multiplier to reconstruct the original value. This approach provides a structured and standardized way to encode variables, making them machine-actionable while maintaining clarity and portability in labels.
