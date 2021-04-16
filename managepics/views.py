from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import ImageForm

from .models import Pic

def index(request):
    pictures = Pic.objects.all()


    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'pics': pictures})

    form = ImageForm()
    return render(request, 'index.html', {'form': form, 'pics': pictures})
    