# Principles

Flare is based on a set of **core principles** that define how labels are created and interpreted.  
These principles ensure that labels are **robust, consistent, human-readable, and machine-actionable**.

## Summary

| Principle                | Rule                                                                       | Example                                  |
|--------------------------|---------------------------------------------------------------------------|------------------------------------------|
| Stand-alone information  | Labels must encode essential information                                  | `project_dataset_2025_v2`                |
| Text-based               | Only ASCII letters, numbers, `_`, and `-` allowed                         | `experiment_trial_01`                    |
| Hierarchy and separators | `_` = primary separator, `-` = secondary, character flags for edge cases | `temperature_36P5_celsius`               |
| Case-insensitive         | Casing has no effect; all labels are parsed as lowercase                  | `DATASET_V2` ≡ `dataset_v2` ≡ `Dataset_V2` |

> See the [Concepts](https://github.com/ipo-exe/flare/blob/main/docs/concepts.md) documentation.

---

These principles make Flare a **portable, consistent, and extensible system** for encoding information in text labels, supporting both human readability and automated processing.

---

## Stand-alone information

Labels must encode **stand-alone information** relevant for identification and retrieval.  
Even when metadata exists inside the asset (e.g., EXIF in images, metadata in PDFs, etc), the **label itself must carry enough descriptive information**.

- A label should be readable by a human without opening the file.  
- A script should be able to retrieve or filter assets **based only on the label**.  
- Labels reduce ambiguity by encoding essential descriptive elements (e.g., dataset, date, version, type).  
- File storage space for naming is used as a meaningful metadata channel.

---

## Text-based

Every label is a **plain text string** in [ASCII](https://www.ascii-code.com/) format, built from a restricted character set.  

- Allowed characters:  
  - **Letters**: `abcdefghijklmnopqrstuvxywz`  
  - **Numbers**: `0123456789`  
  - **Underscore:** `_`
  - **Hyphen**: `-`

- Prohibited characters:  
  - All other ASCII special characters (`. , : ; ! ? @ # $ % & * + = / \ | [ ] { } ( ) ^ ~ ' "`)  
  - Spaces and accented characters  
  - Non-ASCII characters  

This ensures **cross-platform portability** and avoids naming issues in operating systems, databases, and scripts.

---

## Hierarchy

Information in Flare is structured in a hierarchy of three levels:

1. **domain**: major level of information;
2. **subdomain**: minor level of information;
3. **component**: finer detail of information

Flare uses standard reserved characters for structuring information with separators and literal flags. This system ensures that labels are **unambiguous, consistent, and easy to parse**, while still allowing flexibility for specialized encodings. 

### Underscore

Underscore `_` is the **domain separator**. It is used to split the **domains of information** in the label.  
Example:  
```
{info1}_{info2}_{info3}_{info4}
```

### Hyphen

Hyphen `-` is the **subdomain separator**.  It applies only in specific cases, such as breaking down a domain into finer parts of **subdomains**. It is optional and sometimes prohibited (e.g., in database field names).  
Example:  
```
{info1}_{info2}_{info3a-info3b}_{info4}
```

### Flags
Reserved characters may act as **literal flags** when encoding certain information.  
  - These letters replace special characters that are otherwise prohibited.  
Example:  
  - `P` to encode decimals separator `.`.  
  - Other reserved letters may be defined for domain-specific conventions.  



---

## Case-insensitivity

Flare is a **case-insensitive system**.  

- A label is considered the **same**, regardless of whether it is written in lowercase, UPPERCASE, camelCase, or any other casing style.  
- Internally, Flare normalizes all labels to **lowercase** (snakecase) for retrieval, formatting, and automated processes.  
- Non-snakecase are optional for convencience (human-readability) sometimes prohibited (e.g., in database field names).
- Every unique label is therefore **case-insensitive** by definition.

Example (all equivalent in Flare):
```
Project_Dataset_2025
project_dataset_2025
PROJECT_DATASET_2025
Project_Dataset_Trial-Run_2025
```
