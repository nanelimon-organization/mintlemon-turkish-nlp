# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

# Add project directory to sys.path
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'mintlemon-turkish-nlp'
author = '🌿 Mint & Lemon 🍋'
version = 'latest'
release = '2 - Pre-Alpha'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
]
suppress_warnings = ['autosectionlabel.*']

# Napoleon settings
napoleon_numpy_docstring = True

# html_context configuration for GitHub edit link
html_context = {
    'display_github': True,
    'github_user': 'Teknofest-Nane-Limon',
    'github_repo': 'mintlemon-turkish-nlp',
    'github_version': 'main/docs/',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'TODO/*',
]

language = 'English'
source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------

html_static_path = ['_static']
html_theme = 'press'

#html_logo
html_logo = '_static/logo.png'
