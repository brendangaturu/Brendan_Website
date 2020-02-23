from django.test import SimpleTestCase
from django.urls import reverse


class HomePageViewTest(SimpleTestCase):

    def test_home_page_view_status_code(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


class ContactPageViewTest(SimpleTestCase):

    def test_contact_page_view_status_code(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact.html')


class ContentPageViewTest(SimpleTestCase):

    def test_contentwriting_page_view_status_code(self):
        resp = self.client.get('/contentwriting/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('contentwriting'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('contentwriting'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contentwriting.html')


class CreativePageViewTest(SimpleTestCase):

    def test_creativedesigns_page_view_status_code(self):
        resp = self.client.get('/creativedesigns/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('creativedesigns'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('creativedesigns'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'crativedesigns.html')


class MarketingPageViewTest(SimpleTestCase):

    def test_digitalmarketing_page_view_status_code(self):
        resp = self.client.get('/digitalmarketing/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('digitalmarketing'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('digitalmarketing'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'digitalmarketing.html')


class MobilePageViewTest(SimpleTestCase):

    def test_home_page_view_status_code(self):
        resp = self.client.get('/mobiledevelopment/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('mobiledevelopment'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('mobiledevelopment'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'mobiledevelopment.html')


class WebPageViewTest(SimpleTestCase):

    def test_webdesign_page_view_status_code(self):
        resp = self.client.get('/webdesign/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('webdesign'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('webdesign'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'webdesign.html')