# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Handle project layout ---------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'flare'
copyright = '2025, Iporã Possantti'
author = 'Iporã Possantti'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    # mask here
    'sphinx_copybutton'
]

autodoc_mock_imports = [
    'numpy',
    'pandas',
]

autodoc_member_order = 'bysource'

# Exclude the __dict__, __weakref__, and __module__ attributes from being documented
exclude_members = ['__dict__', '__weakref__', '__module__', '__str__']

# Configure autodoc options
autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'private-members': True,
    'special-members': True,
    'show-inheritance': True,
    'exclude-members': ','.join(exclude_members)
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
