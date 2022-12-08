FROM python:3.8.12
# WORKDIR /
COPY requirements.txt 
RUN pip install -r requirements.txt
# COPY . /bot
CMD python bot.py
