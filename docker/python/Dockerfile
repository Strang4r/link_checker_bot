FROM python:3.10

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

RUN apt update && apt upgrade -y

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update -y
RUN apt-get -y install chromium-driver
RUN apt-get -y install google-chrome-stable
RUN apt-get --only-upgrade install google-chrome-stable
RUN apt-get -y install libicu-dev
RUN pip3 install --upgrade pip

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app/

CMD [ "python", "run.py"]

