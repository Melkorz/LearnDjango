from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                # Берём из шаблона, где у нас прописано поле ввода
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                # Берём из шаблона, где у нас прописано поле ввода
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                # Берём из шаблона, где у нас прописано поле ввода
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "date": DateTimeInput(attrs={
                # Берём из шаблона, где у нас прописано поле ввода
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }
