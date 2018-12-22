FROM        python:3.6.7-slim

# 이 이미지의 운영체제(debian) 패키지 관리자 업데이트, 설치되어있는 패키지 업그레이드
RUN         apt -y update &&\
            apt -y dist-upgrade &&\
            # nginx - 웹 서버
            # supervisor - 프로세스 컨트롤 시스템
            # build-essential - uWSGI를 설치하기 위해 필요한 빌드용 패키지
            apt -y install nginx supervisor build-essential

# WSGI모듈 설치
RUN         pip3 install uwsgi

# 로컬의 requirements를 이미지의 /tmp/경로에 복사
COPY        ./requirements.txt  /tmp/requirements.txt
# /tmp/requirements.txt에 기록된 내용을 이미지에 설치
RUN         pip3 install -r /tmp/requirements.txt

# docker run으로 이 이미지를 사용해 컨테이너가 생성되었을 때, 자동으로 실행할 커맨드
# nginx를 daemon이 아닌, foreground상태로 실행
CMD         nginx -g 'daemon off;'
