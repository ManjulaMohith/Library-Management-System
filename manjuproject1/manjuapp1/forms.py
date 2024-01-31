from django import forms
from manjuapp1.models import Library
class LibraryForm(forms.ModelForm):
    class Meta:
        model =Library
        fields='__all__'