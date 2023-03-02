from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from django.utils import timezone
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def question_create(request):
    """pybo 질문등록"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user # 로그인 사용자 정보로 설정
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
        
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """질문 수정"""
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('pybo:detail', question_id=question.id)
    
    if request.method == "POST":
        # 질문 수정을 위한 값 덮어쓰기
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now() # 수정 일시
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        #질문 수정 화면에 기존 제목, 내용 반영
        form = QuestionForm(instance=question)
        
    context = {"form": form}

    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')