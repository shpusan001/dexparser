# Dexparser

## Info

### 1.개요

Apk 파일 내부에 DEX(Dalvik EXcutable format)파일이 존재한다. DEX파일은 클래스, 메소드, 필드, 타입, smali코드 등 소스코드에 대한 정보를 담고 있는 파일이다. DEX파일을 파싱하여 필요한 정보들을 추출하고 웹페이지에 시각화하여 APK파일 분석에 용이하게 한다.

---

### 2.기술 스택

#### 프론트엔드

```
언어: Javascript
라이브러리: React.js, Redux, Redux-saga, Bootstrap
```

#### 백엔드

```
언어: Python 3.10
FastAPI, Sqlite3, Pydantic
```

---

### 3.실행 방법 (Docker)

```
docker pull shpusan001/dexparser-server:0.11
docker pull shpusan001/dexparser-client:0.11

docker run shpusan001/dexparser-server:0.11
docker run shpusan001/dexparser-client:0.11

```

### 4.실행 방법 (소스파일)

사전 설치 필요 소프트웨어

```
python 3.10 버전 이상, pip 22.3.1 버전 이상, node.js v18.12.1 이상
```

파싱 서버

```bash
cd <프로젝트 경로>/server

pip install -r requirements.txt

uvicorn App:app --workers <실행할 프로세스 개수 [8개 권장]>
```

프론트 서버

```bash
cd <프로젝트 경로>/client

npm i

npm start
```

---

### 5.스크린샷

#### 5-1 파싱 서버에 연결
<img width="1720" alt="image" src="https://user-images.githubusercontent.com/35298140/210758487-0114d082-622f-4aa3-bb29-56db7a0c73e9.png">

#### 5-2 APK 파일 리스트 확인
<img width="1726" alt="image" src="https://user-images.githubusercontent.com/35298140/210758548-0e2c254c-9ff7-425f-a3d8-de526b2df1a4.png">

#### 5-3 파싱 요청
<img width="1726" alt="image" src="https://user-images.githubusercontent.com/35298140/210758646-7ea278ca-a717-4ab9-b9eb-310d38a36460.png">

#### 5-4 파싱 결과 출력
<img width="1724" alt="image" src="https://user-images.githubusercontent.com/35298140/210758705-37a857e7-00c0-4769-8a82-8754e471d7fe.png">

---
