import re
import warnings
from typing import List
from pathlib import Path
from ._builtin import DeasciifierBuiltin, NormBuiltin
import pandas as pd

ST_WR_PATH = str(Path(__file__).parent.parent / "data/stop_words.txt")

class Normalizer:
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
        'Dünya'
        """
        text = re.sub(r'\s*#\w+', '', text) # remove hashtags
        text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-zğüşıöçĞÜŞİÖÇ0-9 \t])|(\w+:\/\/\S+)|^rt|http.+?", '', text) # punctuations removed except #,@

        return text.strip()

    @staticmethod
    def remove_accent_marks(text: str) -> str:
        """
        Removes accent marks from the given string.

        Parameters
        ----------
        text : str
            Input text.

        Returns
        -------
        text : str
            Text stripped from accent marks.

        Example:
        --------
        >>> from mintlemon import Normalizer
        >>> Normalizer.remove_accent_marks("merhâbâ")
        'merhaba'
        """
        accent_marks = {
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
        for mark, letter in accent_marks.items():
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
    def normalize_turkish_chars(text):
        """
        Normalize Turkish characters in the given text.

        Parameters
        ----------
        text : str
            The text to be normalized.

        Returns
        -------
        str
            The normalized text with Turkish characters replaced by their ASCII equivalents.

        Examples
        --------
        >>> normalize_turkish_chars("Bir gün İstanbul'da çay içtik.")
        'Bir gun Istanbul\'da cay ictik.'

        >>> normalize_turkish_chars("Gazi Üniversitesi'ne hoş geldiniz.")
        'Gazi Universitesi\'ne hos geldiniz.'
        """
        translationTable = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
        result = text.translate(translationTable)
        return result

    @staticmethod
    def remove_numbers(text):
        """
        Removes numerical expressions from a given text.

        This function removes all numerical expressions from a given text, including
        integers, decimals, and signed integers/decimals.

        Parameters
        ----------
        text : str
            The text to remove numerical expressions from

        Returns
        -------
        cleaned_text : str
            The cleaned text without any numerical expressions

        Example
        -------
        >>> text = "Bu cümle 12.34 ile başlıyor ve 56 ile bitiyor. 2,5 +3,5 -3,4 ile ilgili bir şeyler söyleyebiliriz."
        >>> remove_numbers(text)
        'Bu cümle ile başlıyor ve ile bitiyor. ile ilgili bir şeyler söyleyebiliriz.'
        """
        return re.sub(r"(?<!\d)[-+]?\d*\.?\d+(?!\d)\s*", "", text)

    @staticmethod
    def remove_more_space(text: str) -> str:
        """
        Removes extra spaces from the given text.

        Parameters
        ----------
        text : str
            The text to remove extra spaces from.

        Returns
        -------
        str
            The cleaned text without extra spaces.

        Example
        -------
        >>> text = "Ahmet Selam,  Nerelerdeydin? Seni ÇOOOOK      ÖZLEDİK!!!"
        >>> remove_more_space(text)
        'Ahmet Selam, Nerelerdeydin? Seni ÇOOOOK ÖZLEDİK!!!'
        """
        return " ".join(text.split())

    def drop_empty_values(df, column_text) -> pd.DataFrame:
        """
        Drop the rows from the given dataframe where the specified column_text is empty.

        Parameters
        ----------
        df : pandas.DataFrame
            The dataframe to be processed
        column_text : str
            The name of the column to be checked for empty values

        Returns
        -------
        pandas.DataFrame
            The cleaned dataframe without the rows containing empty column_text values

        Example
        -------
        >>> data = {'id': [1, 2, 3, 4, 5],
                    'name': ['Şeyma', 'Murat', 'Elif', 'Tarık Kaan', 'Erdinç'],
                    'text': ['Bilgisayar Mühendisi', 'Doç. Dr', '', 'Yazılım Mühendisi', '']}
        >>> df = pd.DataFrame(data)
        >>> cleaned_df = drop_empty_values(df, 'text')
        >>> cleaned_df

        id      name             text
        0   1   Şeyma      Bilgisayar Mühendisi
        2   3   Murat      Doç. Dr
        3   4   Tarık Kaan Yazılım Mühendisi
        """
        cleaned_df = df[df[column_text] != ""]

        return cleaned_df

    @staticmethod
    def remove_stopwords(text: str, stop_words_file: str = ST_WR_PATH) -> str:
        """
        Removes stop words from the given text.

        Parameters
        ----------
        text : str
            The text to remove stop words from.
        stop_words_file : str
            The path to the file containing the stop words. Default is the path defined in the library.

        Returns
        -------
        str
            The cleaned text without stop words.

        Example
        -------
        >>> text = "Bu cümledeki bazı gereksiz kelimeleri çıkarmak istiyorum."
        >>> remove_stopwords(text)
        'cümledeki gereksiz kelimeleri çıkarmak istiyorum.'
        """
        with open(stop_words_file, "r", encoding="utf-8") as f:
            stop_words = set(f.read().split())

        cleaned_text = " ".join(
            word for word in text.split() if word.lower() not in stop_words
        )

        return cleaned_text
