# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Geoguessr Async'
copyright = '2026, Antoine BLAISE'
author = 'Antoine BLAISE'
release = '2.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # Support for Google/NumPy style docstrings
    'sphinx.ext.intersphinx',  # Link to other projects' documentation
    'sphinx_autodoc_typehints',  # Type hints in documentation
    'sphinx.ext.autosummary',  # Generate autodoc summaries
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'basic'
html_static_path = ['_static']

# -- autodoc configuration -------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# -- Napoleon configuration -------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# -- Intersphinx configuration ------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'aiohttp': ('https://docs.aiohttp.org/en/stable/', None),
}

# -- Type hints configuration ------------------------------------------------
typehints_fully_qualified = False
always_document_param_types = True
