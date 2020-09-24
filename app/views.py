from django.shortcuts import render
from app.models import File

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {'all_files': File.objects.all()})