from django import forms
from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        widgets = {
             'subject' : forms.TextInput(attrs={'placeholder':'제목 입력해라'}),
             'content' : forms.Textarea(attrs={'placeholder':'내용 입력해라'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }
        
        

    