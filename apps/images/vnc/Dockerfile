ARG ALPINE_VERSION="3.15"

FROM alpine:${ALPINE_VERSION} AS main 

RUN apk add -U \
    dbus-x11 \
    x11vnc 

ENV DISPLAY :1 

CMD "x11vnc -display ${DISPLAY} -xkb -rfbport 5901 -noshm -noxrecord -noxfixes -noxdamage -forever -nopw"
