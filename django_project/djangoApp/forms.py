from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label="your_name", max_length=100)

class MovieForm(forms.Form):
	movie = forms.CharField(label="movie_title", max_length=100)


