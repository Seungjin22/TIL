# Django 월말평가



```python 
# get_object_or_404를 사용할 때는 받아오는 모델이 뒤 괄호 안에 들어감
article = get_object_or_404(Article, pk=article_pk)
```



```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
```

유저가 좋아한 게시글들 전부 다

user.articles_set

이게 유저가 쓴 게시글들 전부 다

user.articles_set 이랑 겹치니까

related_name = "like_articles"라고 설정해서

user.like_articles 라고 구분해주기

```python
근데 왜?
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```







```python
# models.py / accounts
class User(AbstractUser):
    followers = 
```



```python
# settings.py

# default: AUTH_USER_MODEL = 'auth.User'
# AUTH_USER_MODEL = '앱이름.모델이름'
AUTH_USER_MODEL = 'accounts.User'

```

