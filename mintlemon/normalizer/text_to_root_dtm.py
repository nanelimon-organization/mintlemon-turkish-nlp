import zeyrek
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from typing import Optional

nltk.download("punkt", quiet=True)

class TextRootDTMVectorizer:
    """
    Transform a DataFrame of text into a document-term matrix using word roots
    extracted by the Zeyrek morphological analyzer.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing the text data.
    column_name : str
        The name of the column containing the text data.

    Examples
    --------
    >>> import pandas as pd
    >>> from mintlemon import TextRootDTMVectorizer
    >>> df = pd.DataFrame({'text': ['bu bir örnek metindir', 'başka bir örnek metin']})
    >>> vectorizer = TextRootDTMVectorizer(df, 'text')
    >>> vectorizer.fit_transform()
    """

    def __init__(self, dataframe: pd.DataFrame, column_name: str) -> None:
        """
        Initialize TextRootDTMVectorizer instance.
        """
        self.dataframe = dataframe
        self.column_name = column_name
        self.analyzer = zeyrek.MorphAnalyzer()
        self.vectorizer = CountVectorizer()

    def _analyze_word(self, word: str) -> Optional[str]:
        """
        Analyze the given word and extract its root.

        Parameters
        ----------
        word : str
            The input word.

        Returns
        -------
        str or None
            The root of the input word or None if root could not be extracted.

        Examples
        --------
        >>> from mintlemon import TextRootDTMVectorizer
        >>> vectorizer = TextRootDTMVectorizer(None, None)
        # dummy initialization first arg is actually mandatory
        # but we don't need it here
        >>> vectorizer._analyze_word('kelimelerimiz')
        """
        analysis = self.analyzer.analyze(word)
        if len(analysis) > 0:
            root = analysis[0][0][1]
            return root
        else:
            return None

    def fit_transform(self) -> pd.DataFrame:
        """
        Fit and transform the data using the vectorizer.

        Returns
        -------
        pandas.DataFrame
            The transformed document-term matrix.

        Examples
        --------
        >>> import pandas as pd
        >>> from mintlemon import TextRootDTMVectorizer
        >>> df = pd.DataFrame({'text': ['bu bir örnek metindir', 'başka bir örnek metin']})
        >>> vectorizer = TextRootDTMVectorizer(df, 'text')
        >>> vectorizer.fit_transform()
        """
        processed_texts = []
        for text in self.dataframe[self.column_name]:
            words = nltk.word_tokenize(text)
            processed_words = []
            for word in words:
                root = self._analyze_word(word)
                if root:
                    processed_words.append(root)
            processed_texts.append(" ".join(processed_words))

        X = self.vectorizer.fit_transform(processed_texts)

        return pd.DataFrame(X.toarray(), columns=self.vectorizer.get_feature_names_out())
