from django import forms
from recipe.models import Recipe, Element, Cooking, Detail


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe  # 사용할 모델
        fields = ['name', 'image', 'category', 'level', 'tool', 'duration']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'name': '레시피 이름',
            'image': '레시피 사진',
            'category': '카테고리',
            'level': '난이도',
            'tool': '조리 도구',
            'duration': '조리 시간',
        }
        
        
class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['ename', 'put', 'unit']
        labels = {
            'ename': '재료 이름',
            'put': '투입 용량',
            'unit': '용량 단위',
        }


class CookingForm(forms.ModelForm):
    class Meta:
        model = Cooking
        fields = ['process']
        labels = {
            'process': '조리 방법',
        }


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['score', 'content']
        labels = {
            'score': '평가',
            'content': '후기',
        }