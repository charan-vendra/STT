from django.shortcuts import render
from .forms import SpeechToTextForm

def index(request):
    return render(request, 'index.html', {'form': SpeechToTextForm()})
