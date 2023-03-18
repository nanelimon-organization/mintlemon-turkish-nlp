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

sys.path.insert(0, os.path.abspath("../../"))

# -- Project information -----------------------------------------------------

project = "mintlemon-turkish-nlp"
copyright = "Nane & Limon"
author = "Nane & Limon"
release = "2 - Pre-Alpha"
version = "latest"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
]

suppress_warnings = ["autosectionlabel.*"]

# Napoleon settings
napoleon_numpy_docstring = True


# html_context configuration for GitHub edit link
html_context = {
    "display_github": True,
    "github_user": "Teknofest-Nane-Limon",
    "github_repo": "mintlemon-turkish-nlp",
    "github_version": "main/docs/"
}


templates_path = ["source/_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "TODO/*"]

language = "English"


# -- Options for HTML output -------------------------------------------------


html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

source_suffix = [".rst", ".md"]


# Below html_theme_options config depends on the theme.
html_logo = "_static/logo.png"

html_theme_options = {"logo_only": True, "display_version": True}

# -- Options for EPUB output
epub_show_urls = "footnote"
