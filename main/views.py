from django.views.generic import ListView

from main.models import TestModel


class TestView(ListView):
    model = TestModel
    template_name = "main/index.html"
    context_object_name = "tests"
