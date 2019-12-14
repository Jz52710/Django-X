from django.db import models

class Question(models.Model):
    class Meta:
        db_table = 'question'
        verbose_name = "问题"
        verbose_name_plural = "问题"

    question_text = models.CharField(max_length=200,verbose_name="问题")
    pub_date = models.DateTimeField(verbose_name='问题')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    class Meta:
        db_table = 'choice'
        verbose_name = "选项"
        verbose_name_plural = "选项"

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,verbose_name="选项")
    votes = models.IntegerField(default=0,verbose_name="投票")
    def __str__(self):
        return self.choice_text
