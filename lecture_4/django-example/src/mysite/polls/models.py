"""
Poll models
"""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Question model
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # pylint: disable=missing-docstring
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        Was any questions published recently (last day)

        :return: boolean
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    Choice model
    """
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)
    choice_text = models.CharField(
        max_length=200, verbose_name='Choice')
    votes = models.IntegerField(default=0)

    # pylint: disable=missing-docstring
    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    # pylint: disable=missing-docstring
    def __str__(self):
        return self.choice_text
