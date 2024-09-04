## 1. Django Form

### Form 생성하는 법
- **Form**: Django의 `forms.Form` 클래스를 상속받아 정의합니다.
- 예제:
  ```python
  from django import forms

  class MyForm(forms.Form):
      name = forms.CharField(max_length=100)
      email = forms.EmailField()
  ```

### Widgets
- **Widgets**: Form 필드의 HTML 표현을 정의합니다.
- 예제:
  ```python
  class MyForm(forms.Form):
      name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
      email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
  ```

### CreationForm
- **CreationForm**: 사용자 생성 폼은 `UserCreationForm` 클래스를 사용합니다. Django의 기본 `User` 모델을 위한 폼입니다.
- 예제:
  ```python
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib.auth.models import User

  class MyUserCreationForm(UserCreationForm):
      class Meta:
          model = User
          fields = ['username', 'email']
  ```

### AuthenticationForm
- **AuthenticationForm**: 사용자 로그인 폼은 `AuthenticationForm`을 사용합니다.
- 예제:
  ```python
  from django.contrib.auth.forms import AuthenticationForm

  class MyAuthenticationForm(AuthenticationForm):
      pass
  ```

### is_valid()
- **is_valid()**: 폼의 유효성을 검사합니다. 폼 데이터가 유효한 경우 `True`를 반환합니다.
- 예제:
  ```python
  form = MyForm(request.POST)
  if form.is_valid():
      # process the data
      pass
  ```

## 2. Django ORM

### ORM 이란?
- **ORM (Object-Relational Mapping)**: 객체와 데이터베이스 테이블 간의 매핑을 제공하여 데이터베이스 쿼리를 파이썬 객체처럼 사용할 수 있게 합니다.

### Django ORM 의 특징
- Django ORM은 **쿼리셋**을 사용하여 데이터베이스 조작을 추상화합니다.
- SQL을 직접 작성하지 않고도 데이터베이스 작업을 수행할 수 있습니다.

### Django ORM 의 기본적인 사용방법

#### objects
- **objects**: 기본 매니저, 모델 인스턴스와 쿼리셋 작업을 수행합니다.
- 예제:
  ```python
  from myapp.models import MyModel
  objects = MyModel.objects.all()
  ```

#### filter
- **filter()**: 조건에 맞는 레코드를 반환합니다.
- 예제:
  ```python
  MyModel.objects.filter(name='John')
  ```

#### get
- **get()**: 조건에 맞는 단일 레코드를 반환합니다. (존재하지 않거나 여러 개일 경우 예외 발생)
- 예제:
  ```python
  MyModel.objects.get(id=1)
  ```

#### order_by
- **order_by()**: 결과를 정렬합니다.
- 예제:
  ```python
  MyModel.objects.all().order_by('name')
  ```

#### create
- **create()**: 새로운 레코드를 생성합니다.
- 예제:
  ```python
  MyModel.objects.create(name='John', age=30)
  ```

#### delete
- **delete()**: 레코드를 삭제합니다.
- 예제:
  ```python
  obj = MyModel.objects.get(id=1)
  obj.delete()
  ```

#### update
- **update()**: 필드 값을 업데이트합니다.
- 예제:
  ```python
  MyModel.objects.filter(id=1).update(name='Jane')
  ```

#### get_object_or_404
- **get_object_or_404()**: 객체를 조회하고, 객체가 없으면 404 오류를 발생시킵니다.
- 예제:
  ```python
  from django.shortcuts import get_object_or_404
  obj = get_object_or_404(MyModel, id=1)
  ```

## 3. Django Auth

### Django UserModel

#### accounts
- **accounts**: 기본 사용자 인증을 위한 기본 모델과 뷰를 제공합니다.

#### Custom UserModel
- **AbstractUser**: 기본 `User` 모델을 상속받아 사용자 정의 필드를 추가할 수 있습니다.
- **AbstractBaseUser**: 사용자 모델의 기본 기능만을 제공하며, 완전히 사용자 정의 모델을 구현할 때 사용합니다.
- **PermissionMixin**: 권한 관련 기능을 제공합니다.
- **BaseUserManager**: 사용자 생성과 관련된 로직을 커스터마이징할 때 사용합니다.
- **UserManager**: 사용자 모델의 기본 매니저입니다.

### Authenticate()
- **authenticate()**: 사용자를 인증합니다. 유효한 사용자 정보를 제공받으면 사용자 인스턴스를 반환합니다.
- 예제:
  ```python
  from django.contrib.auth import authenticate
  user = authenticate(username='john', password='secret')
  ```

### Login()
- **login()**: 인증된 사용자를 로그인합니다.
- 예제:
  ```python
  from django.contrib.auth import login
  login(request, user)
  ```

### Logout()
- **logout()**: 현재 사용자를 로그아웃합니다.
- 예제:
  ```python
  from django.contrib.auth import logout
  logout(request)
  ```

### login_required 데코레이터 함수
- **login_required**: 로그인된 사용자만 접근할 수 있도록 제한합니다.
- 예제:
  ```python
  from django.contrib.auth.decorators import login_required

  @login_required
  def my_view(request):
      pass
  ```

## 4. CBV (Class-Based View)

### CBV 란?
- **CBV**: 클래스를 사용하여 뷰를 정의합니다. 코드의 재사용성과 확장성을 높입니다.

### View
- **View**: 기본 `View` 클래스를 상속받아 구현합니다.
- 예제:
  ```python
  from django.http import HttpResponse
  from django.views import View

  class MyView(View):
      def get(self, request):
          return HttpResponse('Hello, world!')
  ```

### Generic Views

#### CreateView
- **CreateView**: 객체 생성 폼을 처리합니다.
- 예제:
  ```python
  from django.views.generic.edit import CreateView
  from .models import MyModel

  class MyModelCreateView(CreateView):
      model = MyModel
      fields = ['name', 'description']
  ```

#### UpdateView
- **UpdateView**: 객체 수정 폼을 처리합니다.
- 예제:
  ```python
  from django.views.generic.edit import UpdateView
  from .models import MyModel

  class MyModelUpdateView(UpdateView):
      model = MyModel
      fields = ['name', 'description']
  ```

#### ListView
- **ListView**: 객체 목록을 표시합니다.
- 예제:
  ```python
  from django.views.generic.list import ListView
  from .models import MyModel

  class MyModelListView(ListView):
      model = MyModel
  ```

#### DetailView
- **DetailView**: 객체의 세부 정보를 표시합니다.
- 예제:
  ```python
  from django.views.generic.detail import DetailView
  from .models import MyModel

  class MyModelDetailView(DetailView):
      model = MyModel
  ```

#### DeleteView
- **DeleteView**: 객체 삭제를 처리합니다.
- 예제:
  ```python
  from django.views.generic.edit import DeleteView
  from .models import MyModel

  class MyModelDeleteView(DeleteView):
      model = MyModel
  ```

#### TemplateView
- **TemplateView**: 단순히 템플릿을 렌더링합니다.
- 예제:
  ```python
  from django.views.generic.base import TemplateView

  class MyTemplateView(TemplateView):
      template_name = 'my_template.html'
  ```

#### FormView
- **FormView**: 폼을 렌더링하고 처리합니다.
- 예제:
  ```python
  from django.views.generic.edit import FormView
  from .forms import MyForm

  class MyFormView(FormView):
      form_class = MyForm
      template_name = 'my_form.html'
      success_url = '/success/'
  ```

### request

#### user 가져오기
- **user**: 현재 요청의 사용자 정보를 가져옵니다.
- 예제:
  ```python
  def my_view(request):
      user = request.user
  ```

#### data 가져오기
- **data**: POST 데이터는 `request.POST`로, GET 데이터는 `request.GET`으로 가져옵니다.
- 예제:
  ```python
  def my_view(request):
      post_data = request.POST
      get_data = request.GET
  ```

#### URL 파라미터 (Path Parameter)
- **URL 파라미터**: URL 경로에 포함된 변수입니다. URLconf에서 정의합니다.
- 예제:
  ```python
  path('item/<int:id>/', ItemDetailView.as_view(), name='item_detail')
  ```

#### 쿼리 파라미터 (Query Parameter)
- **쿼리 파라미터**: URL 쿼리 문자열에 포함된 변수입니다.
- 예제:
  ```python
  def my_view(request):
