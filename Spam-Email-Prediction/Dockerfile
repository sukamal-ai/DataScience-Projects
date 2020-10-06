FROM python:3.6-slim

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt
COPY ./app/app.py /api/app.py
COPY ./app/model.py /api/model.py
COPY ./app/model.pkl /api/model.pkl
COPY ./app/tfidf.pkl /api/tfidf.pkl
COPY ./app/templates/index.html /api/templates/index.html 

RUN pip3 install -r requirements.txt

RUN python -m nltk.downloader stopwords

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]