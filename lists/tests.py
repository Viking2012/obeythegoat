from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''
        This is a bit of an unwieldy way of testing that we use
        the right template. And all this faffing about with
        .decode(), and .strip() is distracting.

        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        '''
        # Instead of manually creating an HttpRequest and calling
        # the view function, we call this, passing it the URL we
        # want to test.
        response = self.client.get('/')
        # This test to see if we are using the right template
        self.assertTemplateUsed(response, 'home.html')
