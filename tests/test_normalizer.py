import unittest

from mintlemon import Normalizer


class TestNormalizer(unittest.TestCase):
    """Tests for the Normalizer class methods"""

    def setUp(self):
        self.normalizer = Normalizer()
        self.text_low = "Ex: İIĞÜÖŞÇ"
        self.text_with_numbers = "2,5 kilgoram şeker ve 2 adet ekmek alabilir miyim?"
        self.text_with_punctuations = "!,,,Merhaba? Dünya!,,,"
        self.text_deasc = "O sirada bahcede cicekleri kokluyorduk. Hersey bahcivanin islik calmasiyla yasandi..."
        self.text_accent_marks = "merhâbâ"
        self.text_norm_turkish_chars = "Gazi Üniversitesi'ne hoş geldiniz."
        self.text_with_mixed_numbers = "Bu cümle 12.34 ile başlıyor ve 56 ile bitiyor. 2,5 +3,5 -3,4 ile ilgili bir şeyler söyleyebiliriz."

    def test_lower_case(self):
        """Test the lower_case() method"""
        self.assertEqual(self.normalizer.lower_case(self.text_low), "ex: iığüöşç")

    def test_remove_punctuations(self):
        """Test the remove_punctuations() method"""
        self.assertEqual(
            self.normalizer.remove_punctuations(self.text_with_punctuations),
            "Merhaba Dünya",
        )

    def test_remove_accent_marks(self):
        """Test the remove_accent_marks() method"""
        self.assertEqual(
            self.normalizer.remove_accent_marks(self.text_accent_marks), "merhaba"
        )

    def test_convert_text_numbers(self):
        """Test the convert_text_numbers() method"""
        self.assertEqual(
            self.normalizer.convert_text_numbers(self.text_with_numbers),
            "iki virgül beş kilgoram şeker ve iki adet ekmek alabilir miyim?",
        )

    def test_deasciify(self):
        """Test the deasciify() method"""
        self.assertEqual(
            self.normalizer.deasciify(self.text_deasc),
            "O sırada bahçede çiçekleri kokluyorduk. Herşey bahçıvanın ıslık çalmasıyla yaşandı...",
        )

    def test_normalize_turkish_chars(self):
        """Test the normalize_turkish_chars() method"""
        self.assertEqual(
            self.normalizer.normalize_turkish_chars(self.text_norm_turkish_chars),
            "Gazi Universitesi'ne hos geldiniz.",
        )

    def test_remove_numbers(self):
        """Test the remove_numbers() method"""
        self.assertEqual(
            self.normalizer.remove_numbers(self.text_with_mixed_numbers),
            "Bu cümle ile başlıyor ve ile bitiyor. ile ilgili bir şeyler söyleyebiliriz.",
        )
