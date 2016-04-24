from django import forms
from django.core.exceptions import ValidationError

class ClusterForm(forms.Form):
	
	dataset = forms.ChoiceField(label="Dataset",
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("ratings","IMDB - Movies"),("actors","IMDB - Actors"),("iris","Iris"),("blobs","Blobs"),("crescents","Crescents"),("rings","Rings"),])

	algorithm = forms.ChoiceField(label="Algorithm",
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("select","Select"),("kmeans","KMeans")])

	clusters = forms.ChoiceField(label="Clusters",
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9")])

	numresults = forms.IntegerField(label="Number of Points",required=True)


	def clean(self):
		cleaned_data = self.cleaned_data
		if(self.cleaned_data.get('numresults') == ''):
			raise ValidationError(
				"Pick a higher number"
				)
		else:	
			return self.cleaned_data