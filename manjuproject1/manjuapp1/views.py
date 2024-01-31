from django.shortcuts import render

# Create your views here.

from manjuapp1 import forms
# Create your views here.
from django.http import HttpResponseRedirect

def thanks(request):
    return render(request, 'myapp/thanks.html')

def LibraryView(request):
    if request.method == 'POST':
        form = forms.LibraryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.LibraryForm()
    return render(request, 'myapp/data.html', {'form': form})