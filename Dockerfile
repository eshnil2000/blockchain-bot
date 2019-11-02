# docker build -t eshnil2000/blockchain_bot .
#docker run -d -p 5001:5000 eshnil2000/blockchain_bot

FROM python:3

WORKDIR /usr/src/app

# Bundle app source
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "env", "FLASK_APP=main.py", "flask", "run" ,"--host", "0.0.0.0"]