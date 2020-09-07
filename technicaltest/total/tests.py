from django.test import TestCase

# Create your tests here.

from .serializers import TotalSerializer
from .models import Total

class TotalSerializer(TestCase):
    def test_model_field(self):

        test_total = TotalSerializer()

        for field_name in ['total'] :
            self.assertEqual(TotalSerializer.data[field_name], getattr(test_total, field_name))