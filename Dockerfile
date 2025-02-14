FROM python:3.10


WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --upgrade

COPY . .

RUN wget  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || true
RUN apt update
RUN apt -f install -y


CMD ["pytest", "-v"]