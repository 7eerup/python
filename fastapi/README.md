## FastAPI
`Python`기반 고성능 웹 프레임워크

## Uvicorn
`Uvicorn은 ASGI(Application Server Gateway Interface) 서버`로, 비동기 `FastAPI 웹 프레임워크`와 함께 사용되는 서버

- ASGI 서버: Uvicorn은 ASGI 서버로, 비동기 프로토콜을 지원하는 FastAPI와 같은 프레임워크에서 성능을 극대화
- 고성능: HTTP 요청을 비동기로 처리하여 많은 요청을 동시에 처리할 수 있도록 하며, 특히 비동기 프레임워크에 최적화
- 다양한 프로토콜 지원: HTTP뿐 아니라 WebSocket과 같은 비동기 프로토콜을 지원
- 가벼움과 신속함: 경량 서버이기 때문에 빠르고 간단한 애플리케이션에 적합


### FastAPI Uvicorn 설치
```zsh
$ pip install fastapi uvicorn
```

### FastAPI와 Uvicorn을 함께 사용하는 이유
- FastAPI는 API를 설계하고 데이터 검증, 문서화 등의 기능을 수행
- Uvicorn은 FastAPI 애플리케이션을 실제로 서비스하기 위해 서버 역할

```zsh
$ all:
	uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

- main:app: main.py 파일에 정의된 FastAPI 애플리케이션 객체(app)를 가리킵니다.
- --reload: 코드 변경 시 서버가 자동으로 다시 시작되도록 하는 옵션으로, 개발 단계에서 유용