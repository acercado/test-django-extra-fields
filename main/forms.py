from django import forms
from .models import Contest

class Contest_Form(forms.ModelForm):

    class Meta:
        model = Contest
        fields = ('contest_name', 'points',)

class Contest_Form_Addendum(Contest_Form):

    description = forms.CharField(max_length=100)

    class Meta(Contest_Form.Meta):
        fields = Contest_Form.Meta.fields + ('description',)
