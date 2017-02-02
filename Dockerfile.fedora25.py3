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

CMD xvfb-run -a python3 -m pytest test.py && python3 -m pep8 --ignore=E402 test.py && python3 -m pyflakes test.py
