FROM ghcr.io/rutgerhartog/geryon:base AS main 

RUN apk add -U \
    awesome \
    dbus-x11

ENV DISPLAY x-server:1 

CMD "awesome"