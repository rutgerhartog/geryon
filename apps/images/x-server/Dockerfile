ARG ALPINE_VERSION="3.15"

FROM alpine:${ALPINE_VERSION} AS main 

ENV DISPLAY :1

RUN apk add -U \
    dbus-x11 \
    xvfb 

EXPOSE 6001

CMD "Xvfb ${DISPLAY} -ac -listen tcp"