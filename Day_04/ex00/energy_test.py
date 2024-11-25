import unittest

from energy import fix_wiring


class TestFixWiring(unittest.TestCase):

    def test_basic_case(self):
        cables = ['cable1', 'cable2', 'cable3']
        sockets = ['socket1', 'socket2', 'socket3']
        plugs = ['plug1', 'plug2', 'plug3']
        result = list(fix_wiring(cables, sockets, plugs))
        expected = [
            "plug cable1 into socket1 using plug1",
            "plug cable2 into socket2 using plug2",
            "plug cable3 into socket3 using plug3"
        ]
        self.assertEqual(result, expected)

    def test_weld(self):
        plugs = ['plug1', 'plug2']
        sockets = ['socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable1', 'cable2', 'cable3', 'cable4']
        result = list(fix_wiring(cables, sockets, plugs))
        expected = [
            "plug cable1 into socket1 using plug1",
            "plug cable2 into socket2 using plug2",
            "weld cable3 to socket3 without plug",
            "weld cable4 to socket4 without plug"
        ]
        self.assertEqual(result, expected)

    def test_with_none_and_non_strings(self):
        cables = ['cable2', 'cable1', False]
        sockets = [1, 'socket1', 'socket2', 'socket3', None]
        plugs = ['plugZ', None, 'plugY', 'plugX']
        result = list(fix_wiring(cables, sockets, plugs))
        expected = [
            "plug cable2 into socket1 using plugZ",
            "plug cable1 into socket2 using plugY"
        ]
        self.assertEqual(result, expected)

    def test_empty_inputs(self):
        cables = []
        sockets = []
        plugs = []
        result = list(fix_wiring(cables, sockets, plugs))
        expected = []
        self.assertEqual(result, expected)

    def test_more_sockets_than_cables(self):
        cables = ['cable1', 'cable2']
        sockets = ['socket1', 'socket2', 'socket3']
        plugs = ['plug1']
        result = list(fix_wiring(cables, sockets, plugs))
        expected = [
            "plug cable1 into socket1 using plug1",
            "weld cable2 to socket2 without plug"
        ]
        self.assertEqual(result, expected)

    def test_more_cables_than_sockets(self):
        cables = ['cable1', 'cable2', 'cable3']
        sockets = ['socket1']
        plugs = []
        result = list(fix_wiring(cables, sockets, plugs))
        expected = [
            "weld cable1 to socket1 without plug"
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
