from django import forms
from polls.models import Output

class OutputForm(forms.Form):
	price = forms.CharField()
	asin = forms.CharField()
	rank = forms.CharField()
	link = forms.CharField()
	List = forms.CharField()
	brand = forms.CharField()
	cpu = forms.CharField()
	date = forms.CharField()
	screen = forms.CharField()
	ram = forms.CharField()
	Type = forms.CharField()
	model = forms.CharField()
	os = forms.CharField()
	DVD = forms.CharField()
	keyboard = forms.CharField()
	security = forms.CharField()
	vc = forms.CharField()
	upc = forms.CharField()
	sku = forms.CharField()
	office = forms.CharField()