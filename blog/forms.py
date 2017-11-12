# -*- coding: utf-8 -*-
from django import forms
from .models import Post
from PIL import Image

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'title', 'text')