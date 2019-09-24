FROM gliderlabs/alpine:latest
MAINTAINER DISHA <disha.r@altius.cc>
LABEL DESCRIPTION="Docker 10 days - Build image for the Docker-compose sample app."

ADD. / sampleapp
WORKDIR /sampleapp
RUN apk-install python \
    python-dev \
    py-pip &&\
    pip install -r requirements.txt
CMD ["python","app.py"]
