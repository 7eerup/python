## Python 자동화 A to Z

### Python 가상 환경 설정
```bash
$ python -m venv .venv
```

### 가상 환경 활성화
```bash
$ source .venv/bin/activate
```

### 가상 환경 비활성화
```bash
$ deactivate
```

### pip 최신 릴리즈 설치 및 업그레이드
**[notice] A new release of pip is available: 23.2.1 -> 24.2**
```bash
$ pip install --upgrade pip
```
**[notice] Successfully installed pip-24.2**

### 설치 PKG 목록 확인
```bash
$ pip list
```

### PKG 설치
```zsh
$ pip install pkg_name
```

### requirements.txt 생성 (패키지 비전 포함)
```zsh
$ pip freeze > requirements.txt
```

### 다른 환경에서 동일 PKG 설치
```zsh
$ pip install -r requirements.txt
```

### Package Version Lists
```bash
Package Version
------- -------
pip     24.2
```

### Package 라이브러리 설치
```bash
$ pip install openpyxl==3.1.2 requests==2.31.0 selenium==4.12.0 webdriver_manager==4.0.0
```