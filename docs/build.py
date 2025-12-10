# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2025 The Project Authors
# See pyproject.toml for authors/maintainers.
# See LICENSE for license details.
"""
Sphinx Documentation Builder
----------------------------

A simple Python module to build Sphinx documentation and automatically
open the index.html in a web browser.

Features
--------
* Run Sphinx build command
* Automatically open index.html in default web browser
* Cross-platform support

Overview
--------
This module allows developers to quickly generate HTML documentation from
their Sphinx `.rst` or `.md` files and view the result without manually
navigating to the build folder.

Examples
--------

.. dropdown:: Build in silent mode
    :icon: code-square
    :open:

    .. code-block:: bash

        python -m docs.build

.. dropdown:: Build and open website locally
    :icon: code-square
    :open:

    .. code-block:: bash

        python -m docs.build

"""


# IMPORTS
# ***********************************************************************

# Native imports
# =======================================================================
import subprocess
import webbrowser
import glob, os
from pathlib import Path
import argparse


# External imports
# =======================================================================
import pandas as pd

# Project-level imports
# =======================================================================
# None required


# CONSTANTS
# ***********************************************************************

# CONSTANTS -- Project-level
# =======================================================================
DOCS_DIR = Path("docs")
BUILD_DIR = DOCS_DIR / "_build"
GENERATED_DIR = DOCS_DIR / "generated"
DOCS_DATA_DIR = DOCS_DIR / "data"
INDEX_FILE = BUILD_DIR / "index.html"

SRC_DIR = Path("src/flare/")
SRC_DATA_DIR = SRC_DIR / "data"

# Files
SRC_DATA_NAMES = SRC_DATA_DIR / "names.csv"

# FUNCTIONS
# ***********************************************************************


# FUNCTIONS -- Project-level
# =======================================================================
def build_docs(open_site=False):
    """
    Build Sphinx documentation and open the index.html file.

    This function runs the Sphinx build command with HTML output, then
    opens the generated index.html in the default web browser.
    """
    # Clean generated files
    delete_generated()
    # Run sphinx-build
    subprocess.run(
        ["sphinx-build", "-b", "html", str(DOCS_DIR), str(BUILD_DIR), "--write-all"],
        check=True,
    )

    # Open the generated index.html in the default web browser
    if open_site:
        webbrowser.open(INDEX_FILE.resolve().as_uri())
    print(f"Documentation built successfully! Open {INDEX_FILE}")


# FUNCTIONS -- Module-level
# =======================================================================
def delete_generated():
    """
    Delete all ``rst`` generated files prior to build.
    """
    ls_files = glob.glob(str(GENERATED_DIR / "*.rst"))
    if len(ls_files) == 0:
        pass
    else:
        for f in ls_files:
            print(f"deleted {f}")
            os.remove(f)
    return None


def parse_metadata_table():
    df = pd.read_csv(SRC_DATA_NAMES, sep=";")
    df = df.query("is_variation == 0 and core == 1 and theme == 'metadata'")
    df = df.sort_values(by="name", ascending=True)
    ls_cols = ["name", "alias", "title", "abstract"]
    df = df[ls_cols]
    df.columns = df.columns.str.capitalize()
    df.to_csv(DOCS_DATA_DIR / "metadata_core.csv", sep=";", index=False)
    return None


def parse_stats_table():
    df = pd.read_csv(SRC_DATA_NAMES, sep=";")
    df = df.query("is_variation == 0 and core == 1 and theme == 'statistics'")
    df = df.sort_values(by="name", ascending=True)
    ls_cols = ["name", "alias", "title", "abstract"]
    df = df[ls_cols]
    df.columns = df.columns.str.capitalize()
    df.to_csv(DOCS_DATA_DIR / "statistics_core.csv", sep=";", index=False)
    return None


# CLASSES
# ***********************************************************************
# No classes needed for this module


# SCRIPT
# ***********************************************************************
if __name__ == "__main__":

    # Handle parsing
    # ------------------------------------------------------------------
    parser = argparse.ArgumentParser(description="Build Sphinx HTML documentation.")

    parser.add_argument(
        "--open",
        "-o",
        action="store_true",
        default=False,
        help="Open index.html in the default browser after building.",
    )

    args = parser.parse_args()

    # parse tables
    # ------------------------------------------------------------------
    parse_metadata_table()
    parse_stats_table()

    # Call the builder
    # ------------------------------------------------------------------
    build_docs(open_site=args.open)
