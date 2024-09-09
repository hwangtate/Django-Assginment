### 1. **ImageField**

- **ImageField 특징과 사용법**
  - `ImageField`는 Django의 모델 필드 중 하나로, 이미지 파일을 저장할 때 사용됩니다.
  - 내부적으로 `FileField`를 상속받아 이미지 파일 검증 및 저장을 처리합니다.
  - 이미지를 업로드할 때 이미지를 자동으로 검증하고, 지정된 디렉토리에 이미지를 저장합니다.
  - 사용법:
    ```python
    from django.db import models

    class MyModel(models.Model):
        image = models.ImageField(upload_to='images/')
    ```
    - `upload_to` 파라미터를 통해 이미지가 저장될 디렉토리를 설정할 수 있습니다.

- **Pillow**
  - Python Imaging Library(PIL)의 포크로, 다양한 이미지 파일 형식을 처리할 수 있는 Python 라이브러리입니다.
  - Django에서 `ImageField`를 사용할 때 이미지를 처리하기 위해 Pillow가 필요합니다.
  - Pillow를 설치하면 JPEG, PNG, GIF 등 여러 포맷의 이미지를 Django 애플리케이션에서 처리할 수 있습니다.

- **django-cleanup**
  - Django 애플리케이션에서 파일을 자동으로 삭제해주는 라이브러리입니다.
  - `ImageField`나 `FileField`에서 새로운 파일을 업로드하거나 객체를 삭제할 때, 기존 파일을 자동으로 삭제해 주어 파일이 불필요하게 쌓이는 것을 방지합니다.
  - 설치 후 settings.py에 `django_cleanup`을 추가하여 사용합니다.

- **MEDIA_ROOT**
  - 업로드된 파일들이 저장될 디렉토리의 경로를 지정하는 설정입니다.
  - 보통 프로젝트의 settings.py 파일에서 설정합니다.
  - 예시:
    ```python
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

- **MEDIA_URL**
  - MEDIA_ROOT에 저장된 파일에 접근할 때 사용할 URL 경로를 지정합니다.
  - 브라우저에서 업로드된 파일에 접근할 때 사용됩니다.
  - 예시:
    ```python
    MEDIA_URL = '/media/'
    ```

### 2. **Django-summernote**

- **django-summernote란?**
  - Django에서 사용할 수 있는 WYSIWYG(What You See Is What You Get) 에디터입니다.
  - Summernote라는 오픈 소스 WYSIWYG 에디터를 Django에서 쉽게 사용할 수 있도록 해줍니다.
  
- **특징**
  - HTML 콘텐츠를 쉽게 편집할 수 있는 인터페이스를 제공합니다.
  - 이미지와 파일 업로드 기능이 내장되어 있어, 편리하게 이미지 삽입이 가능합니다.
  - 다양한 설정과 플러그인을 통해 에디터를 확장할 수 있습니다.

- **django-summernote 세팅**
  - 설치:
    ```sh
    pip install django-summernote
    ```
  - settings.py에 추가:
    ```python
    INSTALLED_APPS = [
        ...
        'django_summernote',
    ]

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    ```
  - urls.py에 추가:
    ```python
    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import path, include

    urlpatterns = [
        path('summernote/', include('django_summernote.urls')),
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

- **django-summernote 사용법**
  - 모델에 `SummernoteTextField`를 사용하거나, 기존 `TextField`를 `SummernoteModelAdmin`을 통해 관리할 수 있습니다.
  - 예시:
    ```python
    from django.db import models
    from django_summernote.fields import SummernoteTextField

    class MyModel(models.Model):
        content = SummernoteTextField()
    ```

### 3. **Django-extensions**

- **django-extensions란?**
  - Django 개발을 돕기 위한 다양한 유틸리티와 도구들을 제공하는 라이브러리입니다.
  
- **Python shell**
  - Django Extensions에서 제공하는 `shell_plus`는 Django의 기본 `shell`보다 더 강력한 Python 셸로, 프로젝트의 모든 모델과 설정을 자동으로 가져옵니다.
  
- **특징**
  - 다양한 기능을 포함하고 있으며, 특히 개발 및 디버깅에 유용한 기능들이 많습니다.
  - 예를 들면, `shell_plus`, `runserver_plus`, `graph_models` 등이 있습니다.

- **django-extensions 사용법**
  - 설치:
    ```sh
    pip install django-extensions
    ```
  - settings.py에 추가:
    ```python
    INSTALLED_APPS = [
        ...
        'django_extensions',
    ]
    ```
  - 주요 명령어 사용:
    ```sh
    python manage.py shell_plus
    python manage.py runserver_plus
    python manage.py graph_models -a -o myapp_models.png
    ```

### 4. **OAuth2**

- **OAuth2 정리하기**
  - OAuth 2.0은 사용자가 제3자 애플리케이션에 자신의 자원에 대한 접근 권한을 부여할 수 있는 권한 위임 프로토콜입니다.
  - 주로 소셜 로그인, API 인증 등에 사용되며, 토큰 기반 인증을 통해 사용자 데이터를 보호합니다.
  - OAuth2의 주요 요소:
    - **Resource Owner**: 자원을 소유한 사용자
    - **Client**: 자원에 접근하려는 애플리케이션
    - **Authorization Server**: 사용자 인증과 토큰 발급을 담당하는 서버
    - **Resource Server**: 보호된 자원에 접근을 허용하는 서버
    
- **Naver Social Login**
  - 네이버 로그인 절차 분석:
    - 사용자는 네이버 로그인 페이지로 리다이렉션됩니다.
    - 로그인 후 네이버는 인증 코드를 클라이언트 애플리케이션에 전달합니다.
    - 클라이언트 애플리케이션은 이 인증 코드를 사용하여 네이버의 토큰 엔드포인트에서 액세스 토큰을 요청합니다.
    - 액세스 토큰을 받은 후, 클라이언트 애플리케이션은 이 토큰을 사용해 네이버 API를 호출하여 사용자 정보를 가져옵니다.

  - **네이버 로그인 환경변수 설정하기**
    - 네이버 API 클라이언트 ID와 시크릿 키를 환경 변수로 설정합니다.
    - 예시:
      ```python
      NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
      NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
      ```

  - **네이버 로그인 기능 개발하기**
    - Django에서 네이버 소셜 로그인을 구현하려면, `django-allauth` 같은 라이브러리를 사용할 수 있습니다.
    - 설정 후, 사용자는 네이버 계정을 통해 로그인할 수 있습니다.

챗 지피티를 썼지만 읽긴했습니다 ㅎㅎ !!