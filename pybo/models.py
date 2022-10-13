from django.db import models
from django.contrib.auth.models import User


# model에서 null=True로 설정할 수 있음.
class Question(models.Model):
    subject = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True)   # blank는 form.is_valid() 실행시에 빈칸이어도 된다는 뜻
    voter = models.ManyToManyField(User, related_name='voter_question')
    
    def __str__(self):
        return self.subject
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    
    
    def __str__(self):
        return self.content
