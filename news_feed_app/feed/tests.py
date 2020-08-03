from django.test import TestCase
from .models import *
from django.utils.timezone import now

# Create your tests here.
class NewsFeedTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='sports', selected=True)
        Category.objects.create(name='science', selected=False)

    def test_categories_were_saved_to_db(self):
        sports = Category.objects.get(name='sports')
        science = Category.objects.get(name='science')

        self.assertEqual(sports.selected, True)
        self.assertEqual(science.selected, False)