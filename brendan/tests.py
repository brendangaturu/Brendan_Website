from django.test import SimpleTestCase
from django.urls import reverse


class HomePageViewTest(SimpleTestCase):

    def test_home_page_view_status_code(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)





