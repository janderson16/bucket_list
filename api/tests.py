from django.test import TestCase
from .models import Bucketlist

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_codel_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Buckelist.objects.count()
        self.bucketlist.save()
        new_count = Buckelist.objects.count()
        self.assertNotEqual(old_count, new_count)
