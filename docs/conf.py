# =====================================================
# SPHINX CONFIG
# =====================================================
# For the full list of built-in
# configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# =====================================================
# REPO LAYOUT
# =====================================================
import os
import sys
"""  
for flat layout    
myrepo/  
├──myrepo/  
│   ├── __init__.py  
│   └── module1.py  
└── docs/  
use >> sys.path.insert(0, os.path.abspath(".."))  

for src layout  
myrepo/  
├── src/  
│   └── myrepo/  
│        ├── __init__.py  
│        └── module1.py  
└── docs/   
use >> sys.path.insert(0, os.path.abspath("../src"))  
"""
# sys.path.insert(0, os.path.abspath("..")) # flat layout
sys.path.insert(0, os.path.abspath("../src"))  # src layout

# =====================================================
# REPO PROJECT INFO
# =====================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'flare'
copyright = '2025, Iporã Possantti'
author = 'Iporã Possantti'
release = '0.0.1'

# =====================================================
# GENERAL CONFIGS
# =====================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Extensions
extensions = [
    # built-in extensions
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    # extra extensions
    # -- nice copy button for codeblocks
    'sphinx_copybutton'  # `python -m pip install sphinx-copybutton`
]

# Ignore external dependencies
autodoc_mock_imports = [
    'numpy',
    'pandas',
    # ... keep adding as new dependencies arise
]

autodoc_member_order = 'bysource'

# Exclude the __dict__, __weakref__, and __module__ attributes from being documented
exclude_members = [
    '__dict__',
    '__weakref__',
    '__module__',
    '__str__'
]
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
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]

# =====================================================
# HTML AND THEMES
# =====================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
"""  
Some options for themes  

Built-in:  
>> html_theme = "classic"  
>> html_theme = "alabaster"  
>> html_theme = "bizstyle"  

External (requires installation): 

# by: `python -m pip install sphinx-rtd-theme`   
>> html_theme = "sphinx_rtd_theme" 

# by: `python -m pip install furo`
>> html_theme = "furo"  

# by: `python -m pip install pydata-sphinx-theme`  
>> html_theme = "pydata_sphinx_theme" 

"""
html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']