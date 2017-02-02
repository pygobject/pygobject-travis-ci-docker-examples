FROM debian:jessie-backports

ENV LANG C.UTF-8

RUN apt-get update && apt-get install --no-install-recommends -y \
    gir1.2-gtk-3.0 \
    python3-pep8 \
    pyflakes3 \
    python3-gi \
    python3-gi-cairo \
    python3-pytest \
    xauth \
    xvfb

COPY . /app
WORKDIR /app

CMD xvfb-run -a python3 -m pytest test.py && python3 -m pep8 test.py && python3 -m pyflakes test.py
