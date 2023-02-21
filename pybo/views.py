# Response의 Body에 들어갈 html 문서 return (렌더링을 통해) : 
# 이를 위해 템플릿 파일, 템플릿 파일에서 사용할 변수 목록 필요 
# -> render() 호출 -> render는 Response Body html 리턴

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone

# Create your views here.

def index(request):
    """pybo 목록 출력"""
    question_list = Question.objects.order_by("-create_date")
    context = {'question_list' : question_list}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question =  get_object_or_404(Question, pk=question_id)

    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """pybo 답변등록"""
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
    create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)