FROM fedora:25

ENV LANG C.utf8

RUN dnf -y install \
    gtk3 \
    python3-pyflakes \
    pygobject3 \
    python3-pytest \
    python3-gobject \
    python3-pep8 \
    which \
    xorg-x11-server-Xvfb

COPY . /app
WORKDIR /app
