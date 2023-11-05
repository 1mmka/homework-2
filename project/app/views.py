from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from app.models import Files
from app.forms import FileUpload
from django.urls import reverse_lazy

# Create your views here.
class PrintedFile(ListView):
    model = Files
    context_object_name = 'files'
    template_name = 'new.html'

class NewFile(CreateView):
    model = Files
    form_class = FileUpload
    template_name = 'new.html'
    success_url = reverse_lazy('list_files')