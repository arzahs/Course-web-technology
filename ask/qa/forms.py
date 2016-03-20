from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        answer = Answer()
        answer.author_id = 1
        answer.text = self.cleaned_data['text']
        answer.question_id = self.cleaned_data['question']
        answer.save()
        return answer