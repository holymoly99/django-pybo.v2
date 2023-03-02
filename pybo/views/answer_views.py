from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question, Answer
from django.utils import timezone
from ..forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """pybo 답변등록"""

    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST': # post 방식일 때
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # 로그인 사용자 정보로 설정
            answer.create_date = timezone.now()
            answer.question = question # Foreign Key
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else: # get 방식일 때
        form = QuestionForm()
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "수정권한이 없습니다")
        return redirect('pybo:detail', question_id=answer.question.id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
            
    context = {'answer' : answer, 'form' : form}

    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "삭제권한이 없습니다")
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)