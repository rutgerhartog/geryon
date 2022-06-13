ARG ALPINE_VERSION="3.15"

FROM alpine:${ALPINE_VERSION}

ARG USERNAME="user"
ARG PASSWORD="user"


RUN apk add -U \
    awesome \
    dbus-x11 \
    sudo \
    xorg-server \
    xorgxrdp \
    xrdp

ENV DISPLAY=:10.0

RUN echo -e "#!/bin/ash\nawesome" > /etc/xrdp/startwm.sh
RUN echo "allowed_users = anybody" > /etc/X11/Xwrapper.config 

COPY sesman.ini /etc/xrdp/sesman.ini 

RUN adduser \  
    -D \
    -g "" \
    -u 1000 \
    -s /bin/ash \
    ${USERNAME} \
    && echo "${USERNAME}:${PASSWORD}" | chpasswd \
    && echo "${USERNAME} ALL = (ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && chown -R "${USERNAME}" /var/log \
    && chown -R "${USERNAME}" /etc/xrdp 



EXPOSE 3389 

COPY init /usr/local/bin/init 

RUN chmod +x /usr/local/bin/init 

USER 1000

WORKDIR /home/user

CMD ["init"]