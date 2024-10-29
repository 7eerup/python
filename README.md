## Python 자동화 A to Z

### Python 가상 환경 설정
```bash
$ python -m venv .venv
```

### virtualenv 적용
```bash
$ source .venv/bin/activate
```

### virtualenv 해제
```bash
$ deactivate
```

### pip 최신 릴리즈 설치 및 업그레이드
**[notice] A new release of pip is available: 23.2.1 -> 24.2**
```bash
$ pip install --upgrade pip
```
**[notice] Successfully installed pip-24.2**

### Package 확인
```bash
$ pip list
```

### Package Version Lists
```bash
Package Version
------- -------
pip     24.2
```

### Package 라이브러리 설치
```bash
pip install openpyxl==3.1.2 requests==2.31.0 selenium==4.12.0 webdriver_manager==4.0.0
```