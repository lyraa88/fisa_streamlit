# docker build  -t  생성할이미지명:버전명  Dockerfile위치
#  docker run --name yeonji --rm -d -p 호스트포트:내부포트 생성된이미지
## streamlit을 도커 이미지로 작성해서 외부에서 배포한다면?
FROM python:3.12.11-bookworm

LABEL maintainer="eunsoo <lyra8@naver.com>"


# 디렉토리를 만들고 싶다면
WORKDIR /app
COPY . /app 

# 필요한 라이브러리 설치
# RUN은 빌드 시점에 특정 명령어를 실행하기 위한 키워드
RUN pip install -r requirements.txt


# 이 앱을 사용하는 사람이 너으 포트를 매핑할지
EXPOSE 8501


# run -> 실행
# CMD, ENTRYPOINT 는 빌드가 끝난 이미지를 컨테이너로 만들 때
# 내릴 명령어를 실행하는 키워드


CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true
