from django import forms
from pybo.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        # widgets = {
        #     'subject' : forms.TextInput(attrs={'class':'form-control'}),
        #     'content' : forms.Textarea(attrs={'class':'form-contorl', 'row' : 10}),
        # }