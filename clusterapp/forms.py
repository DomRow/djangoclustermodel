from django import forms

class ClusterForm(forms.Form):
	dataset = forms.ChoiceField(label="Dataset",
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("imdb","IMDB - Ratings"),("iris","Iris"),("blobs","Blobs"),("crescents","Crescents"),("rings","Rings"),])

	algorithm = forms.ChoiceField(label="Algorithm",
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("kmeans","KMeans")])

	clusters = forms.ChoiceField(label="Clusters",
								initial="",
								widget=forms.Select(),
								required=True,
								choices=[("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9")])

	numresults = forms.IntegerField(label="Number of Points"
								,required=True)

	iterations = forms.IntegerField(label="Number of Iterations"
								,required=True)