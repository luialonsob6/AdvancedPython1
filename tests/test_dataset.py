"""
Test loading of the dataset
"""

import unittest
from Scripts.Base_line_script import load_dataset


class TestDataset(unittest.TestCase):
    """
    Class to test the dataset input in different ways
    """

    def setUp(self):  # The setUp function allows us to ... preguntar Chat GPT
        """
        Path to dataset
        """
        self.path = "Datasets/BooksDatasetClean.csdsfsadv"

    def test_extension_fail(self):
        """
        Test for the extension of the dataset
        """
        with self.assertRaises(TypeError):
            load_dataset(self.path)
