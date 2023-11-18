
from  django import forms

from  mySite.models import Category
cats = Category.objects.all()
b = []
for cat in cats:
   b.append((cat.id, cat.title))
class AddArticle(forms.Form):
    title = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'title', 'placeholder': 'Заголовок статьи'}))
    description = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'description', 'placeholder': 'Описание статьи'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'row': 9, 'name': 'fulltext'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'name': 'image'}))
    category = forms.ChoiceField(choices=b)