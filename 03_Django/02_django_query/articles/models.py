from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10) # 제목 너무 길어지지 않도록
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'