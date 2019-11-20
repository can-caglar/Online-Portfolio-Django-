from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
	class Meta():
		model = Post
		fields = ("author","title", "text", "picture")

		widgets= {
			'text': forms.Textarea(attrs={'class':'editable'}),
		}

class CommentForm(forms.ModelForm):
	class Meta():
		model = Comment
		fields = ("author", "text")

		widgets= {
			'author': forms.TextInput(attrs={'class':'editable'}),
			'text': forms.Textarea(attrs={'class':'textinputclass'}),
		}
