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

sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = "mintlemon-turkish-nlp"
author = "🌿 Mint & Lemon 🍋"
release = "2 - Pre-Alpha"
version = "latest"
html_title = project + " " + version
html_last_updated_fmt = "%b %d, %Y"

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


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "TODO/*"]

language = "English"

source_suffix = [".rst", ".md"]

# -- Options for HTML output -------------------------------------------------

html_static_path = ["_static"]

html_theme = "sphinx_book_theme"

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/Teknofest-Nane-Limon/mintlemon-turkish-nlp",
    "use_repository_button": True,
}

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "Teknofest-Nane-Limon",  # Username
    "github_repo": "mintlemon-turkish-nlp",  # Repo name
    "github_version": "main",  # Version
    "conf_py_path": "/docs/source",  # Path in the checkout to the docs root
}

# Below html_theme_options config depends on the theme.
html_logo = "_static/logo.png"

# -- Options for EPUB output
epub_show_urls = "footnote"
myst_enable_extensions = ["colon_fence"]