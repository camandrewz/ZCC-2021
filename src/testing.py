import unittest

from pandas.core.frame import DataFrame
import api
import main


class Test(unittest.TestCase):

    global client
    client = api.API_CLIENT()

    def test_get_count(self):
        self.assertEqual(client.get_ticket_count(), 100)
        self.assertNotEqual(client.get_ticket_count(), 0)

    def test_get_tickets(self):
        self.assertIsInstance(client.get_all_tickets(None), list)
        self.assertIsInstance(client.get_all_tickets("next"), list)
        self.assertIsInstance(client.get_all_tickets("next"), list)
        self.assertIsInstance(client.get_all_tickets("next"), list)
        self.assertEqual(client.get_all_tickets("next"), -1)
        self.assertIsInstance(client.get_all_tickets("prev"), list)

    def test_get_single_ticket(self):
        # This ticket exists
        self.assertIsInstance(client.get_ticket(125), dict)
        # This ticket does not exist
        self.assertIsInstance(client.get_ticket(12), dict)

    def test_command_handler(self):
        # Valid Commands
        self.assertEquals(main.handle_command("1", client), None)
        self.assertEquals(main.handle_command("3", client), None)

        # Invalid Commands
        self.assertEquals(main.handle_command("10", client), None)
        self.assertEquals(main.handle_command("-4", client), None)

    def test_get_tix_table(self):

        self.assertIsInstance(main.get_tix_table(client, None), DataFrame)
        self.assertIsInstance(main.get_tix_table(client, "next"), DataFrame)
        self.assertIsInstance(main.get_tix_table(client, "next"), DataFrame)
        self.assertIsInstance(main.get_tix_table(client, "next"), DataFrame)
        self.assertTrue(main.get_tix_table(client, "next").empty)
        self.assertIsInstance(main.get_tix_table(client, "prev"), DataFrame)

    client.close()


if __name__ == '__main__':
    unittest.main()
