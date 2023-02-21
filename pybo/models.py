from django.db import models

class Question(models.Model):
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date = models.DateTimeField('작성일')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키 정의
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content