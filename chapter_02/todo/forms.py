from django import forms

from .models import Todo, Comment


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        exclude = ["author"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "message",
        ]
        labels = {
            "message": "내용",
        }
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 3,
                    "cols": 40,
                    "class": "form-control",
                    "placeholder": "댓글 내용을 입력해주세요.",
                }
            ),
        }
