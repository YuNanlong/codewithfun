from django import forms
from learn.models import Lesson, Submission

class SubmissionForm(forms.ModelForm):
    code = forms.CharField(widget=forms.Textarea)
        
    class Meta:
        model = Submission
        fields = ['code']
