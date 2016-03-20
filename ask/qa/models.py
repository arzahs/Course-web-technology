from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    #RATING_CHOISES = (
    #   (1, 1),
    #    (2, 2),
    #   (3, 3),
    #    (4, 4),
    #   (5, 5)
    #)
    rating = models.IntegerField(default=1)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return u'%s' % ( self.title )

    def get_absolute_url(self):
        return '/question/%s/' % self.pk


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User)



#class Author(models.Model):
#class Like(models.Model):
