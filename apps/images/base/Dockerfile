ARG ALPINE_VERSION="3.15"

FROM alpine:${ALPINE_VERSION} AS gitcloner

RUN apk add -U git

RUN git clone https://github.com/vinceliuice/Orchis-theme /tmp/orchis \
  && git clone https://github.com/vinceliuice/Tela-icon-theme /tmp/tela \
  && git clone https://github.com/vinceliuice/Vimix-cursors /tmp/vimix



FROM debian:stable-slim AS builder

COPY --from=gitcloner /tmp /tmp

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  libgtk-3-common \
  gnome-icon-theme \
  gnome-themes-extra \
  gtk2-engines-murrine \
  materia-gtk-theme \
  sassc

RUN bash /tmp/tela/install.sh \
  && bash /tmp/orchis/install.sh \
  && bash /tmp/vimix/install.sh


FROM alpine:${ALPINE_VERSION} AS main

COPY --from=builder /usr/share/themes /usr/share/themes
COPY --from=builder /usr/share/fonts /usr/share/fonts
COPY --from=builder /usr/share/icons /usr/share/icons

RUN apk add -U \
  dbus-x11 \
  font-noto
