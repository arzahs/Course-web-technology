from django.shortcuts import render
from django.http import HttpResponse
from qa.models import Question
from qa.helpers import pagination


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def get_all_questions(request, *args, **kwargs):
    questions = Question.objects.all()
    page = pagination(request, questions)
    return render(request, 'questions.html',{
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page
    })



def one_question(request, pk):
    question = Question.objects.get(id=pk)

    return render(request, 'question.html', {
        'question': question,
    })
