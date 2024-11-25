import unittest
from unittest.mock import patch

from alarm import add_ingot, get_ingot, empty


class TestMakeSqueak(unittest.TestCase):

    @patch('builtins.print')  # Патчим функцию print
    def test_add_ingot(self, mock_print):
        purse = {}
        updated_purse = add_ingot(purse)

        # Проверяем, что "SQUEAK" было напечатано
        mock_print.assert_called_once_with("SQUEAK")

    @patch('builtins.print')
    def test_get_ingot(self, mock_print):
        purse = {'gold_ingots': 2}
        updated_purse = get_ingot(purse)

        mock_print.assert_called_once_with("SQUEAK")

    @patch('builtins.print')
    def test_empty(self, mock_print):
        purse = {'gold_ingots': 5}
        updated_purse = empty(purse)

        mock_print.assert_called_once_with("SQUEAK")


if __name__ == '__main__':
    unittest.main()
