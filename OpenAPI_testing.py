import unittest, sys, inspect
import twitter_auth
import authentication_keys
import salesforce_manager


class TestTwitterIntegration(unittest.TestCase):
    def test_auth_connection(self):
        self.assertTrue(inspect.ismodule(twitter_auth), msg="twitter_auth file was not found. Keys are needed in that file")

        self.assertTrue(hasattr(twitter_auth, 'api'), msg="api(twitter) could not be loaded. Maybe a wrong token or key")

        id = twitter_auth.api.me()._json['id']
        self.assertEqual(id._json['id'], 863804439945244672, msg="Error retrieving the twitter ID from account")

    def test_support_current_json_structure(self):
        pass

    def test_streaming_tweet(self):
        pass

    def test_creating_tweet(self):
        pass

    def test_reading_tweet(self):
        pass

    def test_deleting_tweet(self):
        pass



class TestSalesForceAPIs(unittest.TestCase):

    def test_auth_connection(self):
        self.assertTrue(inspect.ismodule(authentication_keys), msg="authentication_keys file was not found. Keys are needed in that file")

        self.assertTrue(hasattr(twitter_auth, 'api'), msg="api(twitter) could not be loaded. Maybe a wrong token or key")

        id = twitter_auth.api.me()._json['id']
        self.assertEqual(id._json['id'], 863804439945244672, msg="Error retrieving the twitter ID from account")

        pass

    def test_available_openapi(self):
        # https://eu11.salesforce.com/services/apexrest/openAPI/troubleTicket
        pass

    def test_split(self):
        pass

    def test_class_trouble_ticket(self):
        ticket1 = salesforce_manager.TroubleTicket({'twitterHandle': 'user', 'reason': 'reason', 'description': 'description',
                                                    'location': {'latitude': 5.5, 'longitude': 7, 'place': 'Nowhere'}})
        ticket2 = salesforce_manager.TroubleTicket({'twitterHandle': 'user', 'reason': 'reason', 'description': 'description',
                                                    'location': {'latitude': 5.5, 'longitude': 7, 'place': 'Nowhere'}})
        self.assertTrue(ticket1.equal(ticket1))
        self.assertTrue(ticket1.equal(ticket2))
        self.assertTrue(ticket2.equal(ticket1))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule( sys.modules['OpenAPI_testing'] )
    unittest.TextTestRunner().run( suite )