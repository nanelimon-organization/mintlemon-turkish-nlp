import os
from hunspell import Hunspell

class TurkishSpellChecker:
    """
    A class for spell checking and correction of Turkish texts using Hunspell.
    The default spell checking is based on the 'ours' dataset, which has been
    found to be more successful according to the comparison at:
    https://mukayese.tdd.ai/#/tasks/spellchecking

    Attributes
    ----------
    base_path : str
        The base directory path where the Hunspell data directories are located.
    hunspell_objects : dict
        A dictionary mapping checker types to Hunspell objects.

    Methods
    -------
    check_spelling(text, checker_type='ours')
        Checks and corrects the spelling of the text using the specified Hunspell object.
    """

    def __init__(self, data_dir='data'):
        """
        Initializes the TurkishSpellChecker class with the path to Hunspell data directories.

        Parameters
        ----------
        data_dir : str, optional
            The top directory where Hunspell's .aff and .dic files are located,
            relative to the current file. Defaults to 'data' directory within the
            current file's directory.
        """
        module_dir = os.path.dirname(__file__)
        project_dir = os.path.dirname(module_dir)
        self.base_path = os.path.join(project_dir, data_dir)
        self.hunspell_objects = {
            'ours': self._create_hunspell_object('ours'),
            'hrzafer': self._create_hunspell_object('hrzafer')
        }

    def _create_hunspell_object(self, directory):
        """
        Creates a Hunspell object using a specified subdirectory.

        Parameters
        ----------
        directory : str
            The subdirectory ('ours' or 'hrzafer') containing the Hunspell data files.

        Returns
        -------
        Hunspell
            An initialized Hunspell object for spell checking.
        """
        data_dir = os.path.join(self.base_path, directory)
        return Hunspell('tr_TR', hunspell_data_dir=data_dir)

    def _spell_check_with_hunspell(self, hunspell_obj, text):
        """
        Checks and corrects the spelling of a text using a given Hunspell object.

        Parameters
        ----------
        hunspell_obj : Hunspell
            The Hunspell object to use for spell checking.
        text : str
            The text to be spell checked.

        Returns
        -------
        str
            The corrected text after spell checking.
        """
        corrected_text = []
        for word in text.split():
            if not hunspell_obj.spell(word):
                suggestions = hunspell_obj.suggest(word)
                corrected_word = suggestions[0] if suggestions else word
                corrected_text.append(corrected_word)
            else:
                corrected_text.append(word)
        return ' '.join(corrected_text)

    def check_spelling(self, text, checker_type='ours'):
        """
        Checks and corrects the spelling of the text using the specified checker type.

        Parameters
        ----------
        text : str
            The text to be spell checked.
        checker_type : str, optional
            The type of checker to use ('ours' or 'hrzafer'). Defaults to 'ours', which is
            found to be more successful according to the source comparison.

        Returns
        -------
        str
            The corrected text after spell checking.

        Raises
        ------
        ValueError
            If an incorrect checker type is specified.
            
        Examples
        --------
        >>> from mintlemon.turkish_spellcheck import TurkishSpellChecker
        >>> spell_checker = TurkishSpellChecker()
        >>> sample_text = "Seni gördügümde çok mutlu oldum."
        >>> corrected_text_ours = spell_checker.check_spelling(sample_text)
        >>> corrected_text_hrzafer = spell_checker.check_spelling(sample_text, checker_type='hrzafer')
        'Seni gördüğümde çok mutlu oldum.'
        """
        if checker_type in self.hunspell_objects:
            return self._spell_check_with_hunspell(self.hunspell_objects[checker_type], text)
        else:
            raise ValueError("Incorrect checker type specified: should be 'ours' or 'hrzafer'.")
