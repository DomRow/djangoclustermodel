from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
# def num_check(val):
# 		if val != 0:
# 			raise ValidationError(
# 				_('%(val)s is too low'),
# 				params={'val':val},
# 				)

class ClusterForm(forms.Form):
	
	dataset = forms.ChoiceField(label=mark_safe("<strong>Dataset</strong>"),
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("ratings","IMDB - Movies"),("year","IMDB - Rating/Year"),("iris","Iris"),])
	#,("blobs","Blobs"),("crescents","Crescents"),("rings","Rings")

	algorithm = forms.ChoiceField(label=mark_safe("<strong>Algorithm</strong>"),
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("select","Select"),("kmeans","KMeans")])

	clusters = forms.ChoiceField(label=mark_safe("<strong>Clusters</strong>"),
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9")])

	numresults = forms.IntegerField(label=mark_safe("<strong>Number of Items</strong>"),
								required=True,
								max_value=10,
								help_text="Please pick a value")
								# validators=[MinValueValidator(0),MaxValueValidator(5200)])


	def clean(self):
		cleaned_data = self.cleaned_data
		if(self.cleaned_data.get('numresults') == ''):
			raise ValidationError(
				"Pick a higher number"
				)
		else:	
			return self.cleaned_data

	