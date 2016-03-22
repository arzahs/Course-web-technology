from django.shortcuts import render, Http404
from django.http import HttpResponse
from qa.models import Question, Answer
from qa.helpers import pagination
from qa.forms import AskForm, AnswerForm, RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout

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
        form = AnswerForm(initial={'question': pk})
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
            'answers': answers,
            'form': form
        })


def add_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            #получить url на перенаправление к станице запроса и переправить
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'add_question.html', {
        'form': form
    })


@require_POST
def add_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_absolute_url()
            return HttpResponseRedirect(url)
        else:
            try:
                form = AnswerForm()
                url = '/question/%s/' % request.POST['question']
                return HttpResponseRedirect(url)
            except:
                return render("200")


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #осуществить вход
            user = form.save()
            if user.is_active:
                login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {
        'form': form
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')

    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form
    })


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
