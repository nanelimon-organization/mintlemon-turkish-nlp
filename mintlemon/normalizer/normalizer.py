import re
import warnings
from typing import List, Optional, Dict, Set, Union
from pathlib import Path
from ._builtin import DeasciifierBuiltin, NormBuiltin
import pandas as pd

ST_WR_PATH = str(Path(__file__).parent.parent / "data/stop_words.txt")

class Normalizer:
    
    STOP_WORDS = None
        
    @staticmethod
    def lower_case(text: str) -> str:
        """
        Converts a string of text to lowercase for Turkish language.

        This function handles all Turkish characters which are not handled properly by python lower() method,
        e.g., "İ" -> "i", "I" -> "ı", "Ğ" -> "ğ", "Ü" -> "ü", "Ö" -> "ö", "Ş" -> "ş", "Ç" -> "ç".

        Parameters
        ----------
        text : str
            Input text.

        Returns
        -------
        output : str
            Text in lowercase form.

        Example:
        --------
        >>> from mintlemon import Normalizer
        >>> Normalizer.lower_case("Ex: İIĞÜÖŞÇ")
        'ex: iığüöşç'
        """
        turkish_lowercase_dict = {
            "İ": "i",
            "I": "ı",
            "Ğ": "ğ",
            "Ü": "ü",
            "Ö": "ö",
            "Ş": "ş",
            "Ç": "ç",
        }
        for k, v in turkish_lowercase_dict.items():
            text = text.replace(k, v)
        return text.lower()

    @staticmethod
    def remove_punctuations(text: str) -> str:
        """
        Removes punctuations (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) from the given string.
        This function removes all the punctuation characters from the given text.
        
        Parameters
        ----------
        text : str
            Input text.

        Returns
        -------
        output : str
            Text stripped from punctuations.
            
        Example:
        --------
        >>> from mintlemon import Normalizer
        >>> Normalizer.remove_punctuations("#Merhaba, Dünya! ! # $ % &'()*+,-./:; <= >?@ [\]^_`{|}~) ")
        'Merhaba Dünya'
        """
        text = re.sub(r"[^\w\sğüşıöçĞÜŞİÖÇ.,']", "", text)  
        text = re.sub(r"\s+", " ", text) 
        return text.strip()  

    @staticmethod
    def remove_accent_marks(text: str, accent_mapping: Optional[Dict[str, str]] = None) -> str:
        """
        Removes accent marks from the given string.

        Parameters
        ----------
        text : str
            Input text.

        accent_mapping: dict, optional
            A dictionary mapping accented characters to their unaccented equivalents.
            If not provided, a default mapping for some common accents in Turkish will be used.

        Returns
        -------
        text : str
            Text stripped from accent marks.

        Example:
        --------
        >>> from mintlemon import Normalizer
        >>> Normalizer.remove_accent_marks("merhâbâ")
        'merhaba'

        >>> accent_mapping = {"ä": "a", "ö": "o", "ü": "u"}
        >>> Normalizer.remove_accent_marks("früchtë", accent_mapping)
        'fruchte'
        """
        if accent_mapping is None:
            accent_mapping = {
                "â": "a",
                "ô": "o",
                "î": "i",
                "ê": "e",
                "û": "u",
                "Â": "A",
                "Ô": "O",
                "Î": "İ",
                "Ê": "E",
                "Û": "U",
            }

        for mark, letter in accent_mapping.items():
            text = text.replace(mark, letter)
        return text

    @staticmethod
    def convert_text_numbers(text):
        """
        Convert numbers in a text to words in Turkish language

        This function converts numbers in a given text to words in Turkish language.
        The function uses regular expressions to find and extract numbers in the text,
        and then uses the number_to_word function to convert the numbers to words.
        If the number is too large, a warning is issued. If the decimal number is represented by a period,
        a warning is issued. (because in Turkish language decimal number is represented by comma.)
        The last text where numbers were converted to words is returned.

        Parameters
        ----------
        text : str
            The text containing numbers to be converted to words

        Returns
        -------
        text : str
            The text with the numbers converted to words in Turkish language

        Example:
        --------
        >>> from mintlemon import Normalizer
        >>> Normalizer.convert_text_numbers("Evi 1000000 TL Değerinde! Çok güzel bir evi var ama 3,5 ay boyunca satamamışlar...")
        'Evi bir milyon TL Değerinde! Çok güzel bir evi var ama üç virgül beş ay boyunca satamamışlar...
        """
        def convert_number(match):
            number = float(match.group(0).replace(",", "."))
            if number >= 1e21:
                return warnings.warn(
                    "The number is too big to convert it to words in Turkish language."
                )
            elif number == int(number):
                return NormBuiltin.number_to_word(number=int(number))
            else:
                return warnings.warn(
                    "In Turkish language, decimal numbers are expressed with commas."
                )

        return re.sub(
            r"[-+]?\d*.\d+|\d+", convert_number, text.replace(",", " virgül ")
        ).lstrip()

    @staticmethod
    def deasciify(input: List[str]) -> List[str]:
        """
        Deasciifies the given text for Turkish.

        Parameters
        ----------
        input : List[str]
            List of input str.

        Returns
        -------
        result : List[str]
            The converted Turkish string.

        Example:
        --------
        >>> from mintlemon import Normalizer
        >>> Normalizer().deasciify("O sirada bahcede cıcekleri kokluyorduk. Hersey bahcıvanın islik calmasiyla yasandi...")
        'O sırada bahçede çiçekleri kokluyorduk. Herşey bahçıvanın ıslık çalmasıyla yaşandı...'
        """
        deasciifier = DeasciifierBuiltin(input)
        result = deasciifier.convert_to_turkish()
        return result

    @staticmethod
    def normalize_chars(text, translation_table=None):
        """
        Normalize characters in the given text based on the provided translation table.

        Parameters
        ----------
        text : str
            The text to be normalized.

        translation_table : dict or str.maketrans, optional
            The translation table that defines the mapping of characters to be replaced.
            If not provided, it defaults to the mapping of Turkish characters to their ASCII equivalents.

        Returns
        -------
        str
            The normalized text with characters replaced based on the translation table.

        Examples
        --------
        Default Turkish normalization:
        >>> normalize_chars("Bir gün İstanbul'da çay içtik.")
        'Bir gun Istanbul'da cay ictik.'

        >>> normalize_chars("Gazi Üniversitesi'ne hoş geldiniz.")
        'Gazi Universitesi'ne hos geldiniz.'

        Custom translation for Azerbaijani language:
        >>> azerbaijani_table = str.maketrans("ƏəĞğÇçŞşÜüÖöİı", "AaGgCcSsUuOoIi")
        >>> normalize_chars("Mən Ağcabədi şəhərində yaşayıram.", azerbaijani_table)
        'Men Agcabedi seherinde yasayiram.'
        """
        if translation_table is None:
            translation_table = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")

        result = text.translate(translation_table)
        return result

    @staticmethod
    def remove_numbers(text, remove_signed=True, remove_decimal=True):
        """
        Removes numerical expressions from a given text.

        This function removes all numerical expressions from a given text, including
        integers, decimals, and signed integers/decimals based on the parameters.

        Parameters
        ----------
        text : str
            The text to remove numerical expressions from

        remove_signed : bool, optional
            Whether to remove signed integers/decimals from the text.
            By default, it is set to True.

        remove_decimal : bool, optional
            Whether to remove decimal numbers from the text.
            By default, it is set to True.

        Returns
        -------
        cleaned_text : str
            The cleaned text without any numerical expressions

        Example
        -------
        >>> from mintlemon import Normalizer
        >>> normalize = Normalizer()
        >>> text = "Bu cümle 12.34 ile başlıyor ve 56 ile bitiyor. 2,5 +3,5 -3,4 ile ilgili bir şeyler söyleyebiliriz."
        >>> normalize.remove_numbers(text)
        'Bu cümle ile başlıyor ve ile bitiyor. İle ilgili bir şeyler söyleyebiliriz.'
        """
        if remove_signed and remove_decimal:
            pattern = r"(?<!\d)[-+]?\d*\.?\d+(?!\d)"
        elif remove_signed:
            pattern = r"(?<!\d)[-+]?\d+(?!\d)"
        elif remove_decimal:
            pattern = r"\d*\.?\d+"
        else:
            pattern = r"\d+"

        cleaned_text = re.sub(pattern, "", text)

        cleaned_text = re.sub(r"\s*,\s*", " ", cleaned_text)
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)

        cleaned_text = re.sub(r"^,", "", cleaned_text).strip()

        return cleaned_text

    @classmethod
    def remove_stopwords(cls, text: str, stopwords: Union[Set[str], List[str]] = None) -> str:
        """
        Removes stop words from the given text.

        Parameters
        ----------
        text : str
            The input text.
        stopwords : Union[Set[str], List[str]], optional
            A set or list of words to remove from the text.
            If not provided, it defaults to the stop words loaded from the file.

        Returns
        -------
        str
            The cleaned text with stop words removed.

        Examples
        --------
        >>> from mintlemon import Normalizer

        # Example 1: Using default stop words list
        text = "Bu bir örnek cümle, gereksiz kelimeleri çıkarmak istiyorum."
        cleaned_text = Normalizer.remove_stopwords(text)
        print(cleaned_text)
        # Output: "örnek cümle, gereksiz kelimeleri çıkarmak."

        # Example 2: Providing custom stop words list
        custom_stopwords = ["bir", "gereksiz"]
        cleaned_text = Normalizer.remove_stopwords(text, stopwords=custom_stopwords)
        print(cleaned_text)
        # Output: "Bu örnek cümle, kelimeleri çıkarmak."
        """
        if stopwords is None:
            cls.load_stopwords(ST_WR_PATH)
            stopwords = cls.STOP_WORDS
        elif isinstance(stopwords, list):
            stopwords = set(stopwords)

        cleaned_text = " ".join(word for word in text.split() if word.lower() not in stopwords)
        return cleaned_text

    @classmethod
    def load_stopwords(cls, stop_words_source: Union[str, Set[str], List[str]]) -> None:
        """
        Loads stop words from a file or a set/list of words.

        Parameters
        ----------
        stop_words_source : Union[str, Set[str], List[str]]
            The path to the file containing the stop words
            or a set/list of stop words.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If stop_words_source is not a valid type.

        Examples
        --------
        >>> from mintlemon import Normalizer

        # Example 1: Load stop words from file
        Normalizer.load_stopwords("stop_words.txt")

        # Example 2: Load stop words from a set
        stop_words_set = {"bu", "bir"}
        Normalizer.load_stopwords(stop_words_set)

        # Example 3: Load stop words from a list
        stop_words_list = ["bazı", "istiyorum"]
        Normalizer.load_stopwords(stop_words_list)
        """
        if isinstance(stop_words_source, str):
            with open(stop_words_source, "r", encoding="utf-8") as f:
                cls.STOP_WORDS = set(f.read().split())
        elif isinstance(stop_words_source, (set, list)):
            cls.STOP_WORDS = set(stop_words_source)
        else:
            raise ValueError(
                "stop_words_source must be a path to a file (str), a set of words (set), or a list of words (list)."
            )