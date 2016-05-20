from django import forms
from .models import Articles
from django.forms import ModelForm

AUTHOR_NAME_CHOICES = [('Jimmy Liu', 'Jimmy Liu'), ('Ben Hanson', 'Ben Hanson')]

class DateInput(forms.widgets.TextInput):
	input_type='date'
   
class AddForm(forms.ModelForm):
	blog_author = forms.ChoiceField(label = "Author", choices = AUTHOR_NAME_CHOICES, required = True)
	blog_article = forms.CharField(label = "Article", required = True, widget=forms.Textarea)
	blog_date = forms.DateField(required = True, label = "Publish Date", widget=DateInput)
	blog_image = forms.CharField(required = True, label = "Image Link")
	blog_headline = forms.CharField(required = True, label = "Headline")
	class Meta: 
		model = Articles
		fields = ['blog_author', 'blog_article', 'blog_date', 'blog_image', 'blog_headline']



# controls form for searching through database
class Query(forms.Form):
	blog_author = forms.ChoiceField(choices = AUTHOR_NAME_CHOICES, label = "Author", required = False)
	blog_date = forms.DateField(label = "Publish Date", required = False, widget=DateInput)