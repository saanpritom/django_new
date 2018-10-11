from django import forms
from testapp.models import Topic, Webpage

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


class TopicModelForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields = '__all__'


class WebpageModelForm(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = '__all__'
