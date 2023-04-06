Welcome to the documentation of Mint & Lemon Turkish NLP!
=========================================================
Mint Lemon Turkish NLP is a Python library designed for developers working on Turkish Natural Language Processing. This library includes various NLP tools such as tokenizer, stemmer, named entity recognizer, sentiment analyzer and more.

Mint Lemon Turkish NLP is an open-source software, and its source code is available on `Github <https://github.com/Teknofest-Nane-Limon/mintlemon-turkish-nlp>`_. The repository includes an issue tracker for bug reporting, feature requests, and more.

This documentation provides comprehensive information about the Mint Lemon Turkish NLP library. It covers all the features of the library, including installation instructions, usage guides, and examples. This documentation is designed to answer all your questions related to the Mint Lemon Turkish NLP library.

The source code for this documentation page is also available on `Github <https://github.com/Teknofest-Nane-Limon/mintlemon-turkish-nlp>`_ and can be edited by anyone. You can use the Github repository to ask questions, report bugs, or contribute to the library.

For more information on how to use Mint Lemon Turkish NLP, please see the `official documentation <https://mintlemon-turkish-nlp.readthedocs.io/en/latest/>`_.

- Mint Lemon Turkish NLP is available on `PyPI <https://pypi.org/project/mintlemon-turkish-nlp/>`_.

Installation and Setup
======================

Installation from Pip
---------------------
You can install mintlemon-turkish-nlp easily using the ``pip`` command in your terminal. Simply type the following command to install mintlemon-turkish-nlp:

.. code-block:: console

   $ pip install mintlemon-turkish-nlp

.. note:: The above command will install the latest version of mintlemon-turkish-nlp library on your system. Make sure you have internet connection and updated version of pip package manager.

Installation from Source
------------------------
If you prefer to install mintlemon-turkish-nlp from source, you can do so directly from the Github repository by running the following command:

.. code-block:: bash
    
    $   pip install git+https://github.com/Teknofest-Nane-Limon/mintlemon-turkish-nlp.git

- ``pip install -e.`` if you want to do an editable install (you can modify source files) of just the package itself.
- ``pip install -r requirements.txt`` if you want to install optional dependencies + dependencies used for development (e.g. unit testing).

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Getting Started

   _module/sentence_splitter
   _module/normalizer
   _module/normalizer.text_to_root_dtm_vec
   