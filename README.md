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

### 3.실행 방법

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

### 4.스크린샷


#### 3-1 Apk파일 업로드 및 리스트 확인
<img width="1503" alt="apklist" src="https://user-images.githubusercontent.com/35298140/208599122-030dd1e8-227f-4369-9528-29cfa26d859b.png">


#### 3-2 DexInfo 페이지에서 파일의 아이디를 넣고 Parse버튼 클릭
<img width="1502" alt="dexinfo_loading" src="https://user-images.githubusercontent.com/35298140/208599126-de73e938-e905-4a14-a255-8197b81f8174.png">


#### 3-3 DexInfo 페이지에서 파싱 결과 확인
<img width="1491" alt="dexinfo_parsed_result" src="https://user-images.githubusercontent.com/35298140/208599132-bc58ae7f-0574-4d36-b312-06dda0c1a09e.png">

---

