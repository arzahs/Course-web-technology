from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    _user = User()
    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    _user = User()

    # def __init__(self, user, **kwargs):
    #     self._user = user
    #     super(AnswerForm, self).__init__(**kwargs)

    def save(self):
        answer = Answer()
        answer.author = self._user
        answer.text = self.cleaned_data['text']
        answer.question_id = self.cleaned_data['question']
        answer.save()
        return answer


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        user = authenticate(username=self.cleaned_data['username'],
                            password=self.cleaned_data['password'])
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error('username', u'Error input login or password')


    def save(self):
        user = authenticate(username=self.cleaned_data['username'],
                            password=self.cleaned_data['password'])
        return user