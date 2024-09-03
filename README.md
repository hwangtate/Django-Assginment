## 1. Django 프로젝트 세팅
### 1.1 가상환경 구축하는 방법 (with Poetry)
```commandline
poetry init
poetry shell
poetry add django
```
### 1.2 Django 설치 및 프로젝트 구성, 앱 세팅하는 방법
```commandline
django-admin startproject config .
python manage.py startapp myapp
```
```python
INSTALLED_APPS = [
    # 기존 앱들...
    'myapp',
]
```
### 1.3 templates 경로 지정하기
```python
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 나머지 설정...
    },
]
```
### 1.4 static 경로 지정하기
```python
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
### 1.5 media 경로 지정하기
```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
## 2. Database Model
### 2.1 데이터베이스 모델 정의하기
Django의 모델은 데이터베이스의 구조를 정의하는 클래스입니다. 
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
```
### 2.2 각 필드별 특징 정리하기
- CharField: 문자열을 저장하는 필드입니다. max_length로 최대 길이를 지정합니다.
- TextField: 긴 문자열을 저장하는 필드입니다. max_length가 없습니다.
- IntegerField: 정수를 저장하는 필드입니다.
- BooleanField: True/False 값을 저장하는 필드입니다.
- DateTimeField: 날짜와 시간을 저장하는 필드입니다.
- ForeignKey: 다른 모델과의 관계를 정의하는 필드입니다.
### 2.3 Migration에 대해서 정리하기
Migration은 모델의 변경사항을 데이터베이스에 반영하는 방법입니다. Migration을 생성하고 적용하는 기본 명령어는 다음과 같습니다:
```commandline
python manage.py makemigrations
python manage.py migrate
```
## 3. Jinja
### 3.1 Jinja 문법 정리하기
기본 Jinja 문법:

- 변수 출력: {{ 변수명 }}
- 필터 사용: {{ 변수명 | 필터명 }}
- 조건문:
```python
{% if 조건 %}
  조건이 참일 때
{% else %}
  조건이 거짓일 때
{% endif %}
```
- 반복문:
```python
{% for item in 리스트 %}
  {{ item }}
{% endfor %}
```
### 3.2 block 사용법
```python
{% block content %}
  여기에 내용이 들어갑니다.
{% endblock %}
```
### 3.3 extends 사용법
```python
{% extends 'base.html' %}
```
## 4. FBV(Function-Based View)
### 4.1 FBV란?
FBV(Function-Based View)는 Django에서 뷰를 함수형으로 정의하는 방식입니다. 함수형 뷰는 간단하고 직관적인 방식으로 특정 요청을 처리할 수 있습니다.
### 4.2 간단한 View 메소드 작성법
```python
#render
from django.shortcuts import render

def my_view(request):
    return render(request, 'my_template.html', {'key': 'value'})

#redirect
from django.shortcuts import redirect

def my_view(request):
    return redirect('some_view_name')
```
## 5. Urls
### 5.1 URL 엔드포인트란?
URL 엔드포인트는 사용자가 웹사이트에서 특정 페이지에 접근하기 위해 입력하는 URL의 끝부분을 의미합니다. Django에서는 URL 엔드포인트를 정의하여 특정 뷰에 연결할 수 있습니다.
### 5.2 urlpatterns
urlpatterns는 URL 패턴과 뷰를 매핑하는 목록입니다. urls.py 파일에서 정의됩니다
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
]
```
### 5.3 URL Include 개념 및 방법
큰 프로젝트에서는 URL 구조를 여러 앱으로 분리하여 관리할 수 있습니다. 이때 include를 사용하여 서브 URL 패턴을 포함할 수 있습니다.
```python
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
]
```
### 5.4 path
path 함수는 URL 패턴을 정의하고 이를 특정 뷰와 연결합니다. path 함수는 urlpatterns 리스트 안에서 사용됩니다.

### 5.5 include
include 함수는 다른 URL 패턴 모듈을 포함하는 데 사용됩니다. 보통 app/urls.py 파일을 메인 urls.py에 포함할 때 사용됩니다.