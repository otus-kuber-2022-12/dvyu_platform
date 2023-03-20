FROM alpine

RUN  apk update && \
     apk add --no-cache python3 py3-pip shadow && \
     pip install console ra requests Flask && \
     groupadd -g 1001 test && \
     useradd -m --no-log-init -u 1001 -s /bin/sh -g test test

ADD  ./app /app
ADD  ./web.py /

ENTRYPOINT ["python", "/web.py"]

USER test
