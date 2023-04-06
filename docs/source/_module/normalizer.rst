Normalizer Module
==================

The Normalizer module is a collection of static methods that allow for the normalization of text in Turkish language. It includes methods for ``converting text to lowercase``, ``deasciify``, ``removing punctuation`` and ``accent marks`` and ``converting numbers to words``. The module utilizes a combination of built-in Python functions and regular expressions to achieve these normalizations. Each method takes in a string of text as an input and returns the normalized version of the text. The module also includes a built-in functions at ``_builtin module`` for converting numbers to words in Turkish language. Overall, this module is useful for preparing text for further processing, such as natural language understanding and machine learning tasks.

How the Normalizer Module Improves Text Preprocessing:
------------------------------------------------------

* **Advanced  Context-aware Replacements:** The class is able to replace specific characters at a given position, taking into account the context of the surrounding characters. This ensures that the resulting text is grammatically and semantically correct, and makes the text more natural and readable.
* **Flexibility:** The class can be easily integrated into various NLP tasks such as text classification, sentiment analysis and text summarization.
* **Language Specific:** The class is specifically designed to handle Turkish text, and is able to handle the unique characteristics and complexities of the language. This makes it more accurate and efficient compared to general-purpose normalization methods that do not take into account the specific language.


.. list-table::
   :widths: 30 80
   :header-rows: 1

   * - Function Name
     - Description
   * - ``convert_text_numbers(text: str) -> str``
     - Converts numbers in a text to words in Turkish language.
   * - ``deasciify(input: List[str]) -> List[str]``
     - Deasciifies the given text for Turkish.
   * - ``remove_punctuations(text: str) -> str``
     - Removes punctuations from the given string.
   * - ``remove_accent_marks(text: str) -> str``
     - Removes accent marks from the given string.
   * - ``lower_case(text: str) -> str``
     - Converts a string of text to lowercase for Turkish language.
   * - ``normalize_turkish_chars(text: str) -> str``
     - Normalizes Turkish characters in the given text.
   * - ``remove_more_space(text: str) -> str``
     - Removes extra spaces from the given text.
   * - ``remove_stopwords(text: str, stop_words_file: str) -> str``
     - Removes stop words from the given text.


.. autoclass:: mintlemon.normalizer.normalizer.Normalizer
   :members:
   :undoc-members: