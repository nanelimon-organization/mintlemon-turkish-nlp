==================
Normalizer Module
==================

The Normalizer module is a collection of static methods that allow for the normalization of text in Turkish language. It includes methods for ``converting text to lowercase``, ``deasciify``, ``removing punctuation`` and ``accent marks`` and ``converting numbers to words``. The module utilizes a combination of built-in Python functions and regular expressions to achieve these normalizations. Each method takes in a string of text as an input and returns the normalized version of the text. The module also includes a built-in functions at ``_builtin module`` for converting numbers to words in Turkish language. Overall, this module is useful for preparing text for further processing, such as natural language understanding and machine learning tasks.

* **Advanced  Context-aware Replacements:** The class is able to replace specific characters at a given position, taking into account the context of the surrounding characters. This ensures that the resulting text is grammatically and semantically correct, and makes the text more natural and readable.
* **Flexibility:** The class can be easily integrated into various NLP tasks such as text classification, sentiment analysis and text summarization.
* **Language Specific:** The class is specifically designed to handle Turkish text, and is able to handle the unique characteristics and complexities of the language. This makes it more accurate and efficient compared to general-purpose normalization methods that do not take into account the specific language.

.. autoclass:: mintlemon.normalizer.normalizer.Normalizer
   :members: