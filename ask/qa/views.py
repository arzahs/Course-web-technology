from django.shortcuts import render, Http404
from django.http import HttpResponse
from qa.models import Question, Answer
from qa.helpers import pagination


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def get_all_questions(request, *args, **kwargs):
    questions = Question.objects.order_by('-added_at')
    page = pagination(request, questions)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page
    })


def get_popular_questions(request, *args, **kwargs):
    questions = Question.objects.order_by('-rating')
    page = pagination(request, questions)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page
    })


def one_question(request, pk):
    try:
        q = Question.objects.get(id=pk)
    except:
        raise Http404
    try:
        answers = Answer.objects.filter(question=q)
    except:
        answers = None
    return render(request, 'question.html', {
        'question': q,
        'answers': answers

    })
