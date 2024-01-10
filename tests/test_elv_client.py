import unittest
import logging
from src.elv_client import *

logging.basicConfig(level=logging.INFO)

TOK = 'atxsjc3xLSpRHaVXpVX5gW4LKfXPTiYo9EafDRfHCW6MZARK2pfyrvQ2RX1VdLqg2QrcMos6yw59RYaBYtP9qgSSHQE6QKADyg3H91Hz3ADQ2BkmVs6ZZCwfaN5CDK4SKe6NBnULtfWWimDtJveo8UW2tKABnuD5wmr9iedsnTy2R7VNKqFY8iHu2uiuN8kRd8HeoofXVh1psSvp1re1GTwS5rCefSvjTqeuuHZF6cSZecqjguVafNKFFoTELFfuwLKvP6ViG77e8FYRenW8sedX5XcCUfsHrdyKTfLrKAr1KYQVHiybF1ZJ8cMNUZadZw8WjCQkfuvqYXck5Nqfy6WwMG8SrDqFbhyCRmhyg53fUsqsCRiBmPi316V6nmyQL17eez6H6NVdyz8CEc8rco9jhpxbXyuyXj8PRe4w8HWybVvk1HwybZaAjvzAEjnpYuy49zSS2FCHfmHLs6kCjp5cFVHjxAtxdZyL4ruFBppk5JmnG4AgDfsmK7Ej83cXdLortZPDyDYPKigPFLGxCg4r1NaghYPNLzxYJ9fh7FhAUmeP8PvpUxcE'

class ElvClientTest(unittest.TestCase):
    def setUp(self):
        self.client = ElvClient("https://main.net955305.contentfabric.io/config", TOK)   

    def test_metadata(self):
        self.assertTrue(TOK != '', 'Auth token not set')
        meta = self.client.content_object_metadata(object_id='iq__44VReNyWedZ1hAACRDBF6TdrBXAE', metadata_subtree='/indexer/config/fabric')
        logging.info(meta)

    def test_search(self):
        self.assertTrue(TOK != '', 'Auth token not set')
        res = self.client.search(library_id='ilib31RD8PXrsdvSppy2p78LU3C9JdME', object_id='iq__2oENKiVcWj9PLnKjYupCw1wduUxj', query={"terms":"hello", "search_fields": ["f_speech_to_text"], "limit": 1})
        logging.info(res)

if __name__ == '__main__':
    unittest.main()