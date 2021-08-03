import unittest

from numpy import CLIP
import api
import main


class Test(unittest.TestCase):

    def test_get_count(self):
        client = api.API_CLIENT()
        self.assertEqual(client.get_ticket_count(), 100)

        client.close()


if __name__ == '__main__':
    unittest.main()
