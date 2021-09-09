FROM python:3

ADD /src/v2bot.py /

RUN pip install discord


CMD [ "python", "./v2bot.py" ]
