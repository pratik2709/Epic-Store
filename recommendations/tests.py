from django.test import TestCase, Client


# Create your tests here.
from django.urls import reverse


class CreateNewPuppyTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_recommendations(self):
        response = self.client.get(
            reverse('get_post_puppies'),
            content_type='application/json'
        )
