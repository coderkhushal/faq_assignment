from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        queryset = self.get_queryset()
        for faq in queryset:
            faq.question = faq.translate_question(lang)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
