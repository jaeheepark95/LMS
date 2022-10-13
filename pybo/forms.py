from django import forms
from django import forms
from pybo.models import Answer, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question    #사용할 모델
        fields = ['subject', 'content']     #form에서 사용할 모델의 속성
        # 부트스트랩 속성 적용
        # template을 {{form.as_p}}로 생성하지 않고 수동으로 만들경우, 필요하지 않음
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        # form을 그냥 사용하면, 각 속성이 Question model에 설정된대로 표시됨
        # 아래처럼 하면, 한글로 바꿀수 있음
        labels = {
            'subject': '제목',
            'content': '내용',
        }   
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }