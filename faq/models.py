# faq/models.py

from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def translate_question(self, lang):
        if lang == 'hi':
            return self.question_hi or self.question  # Fallback to original question
        elif lang == 'bn':
            return self.question_bn or self.question  # Fallback to original question
        return self.question  # Default to original question

    def __str__(self):
        return self.question