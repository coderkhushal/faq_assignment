# faq/tests.py

from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="डjango क्या है?",
            question_bn="ডjango কি?"  
        )

    def test_translate_question(self):
        self.assertEqual(self.faq.translate_question('hi'), "डjango क्या है?")
        self.assertEqual(self.faq.translate_question('bn'), "ডjango কি?")  