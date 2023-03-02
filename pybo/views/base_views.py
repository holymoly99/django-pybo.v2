from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator
from django.db.models import Q, Count

def index(request):
    """pybo 목록 출력"""
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어 
    so = request.GET.get('so', 'recent') # 정렬기준

# 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate( #annotate = 동적 추가 속성 정의
        num_voter=Count('voter')).order_by('-num_voter', '-create_date') # 추천이 가장 많은 순
    elif so == 'popular':
        question_list = Question.objects.annotate(
        num_answer=Count('answer')).order_by('-num_answer', '-create_date') # 답변이 가장 많은 순
    else: # recent
        question_list = Question.objects.order_by('-create_date')

    #조회
    # question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목검색
            Q(content__icontains=kw) | # 내용검색
            Q(author__username__icontains=kw) | # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이검색
        ).distinct()

    # 페이징 처리    
    paginator = Paginator(question_list, 10) # 페이지당 글 10개씩 출력
    page_obj = paginator.get_page(page)
    context = {"question_list": page_obj, 'page': page, 'kw': kw, 'so': so}
    
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question =  get_object_or_404(Question, pk=question_id)

    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)