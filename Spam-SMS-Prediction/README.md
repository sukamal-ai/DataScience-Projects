# SPAM SMS PREDICTION

<p> Goal: Build an application (end to end) that predicts if an SMS is spam or not </p>

## EDA and Preprocessing

<p>Wordcloud plot for spam sms</p>

<img src="plots/wc1.png">

<p> Highly used words in spam sms are - <b>FREE, text, call, txt etc.</b></p>

<p>Wordcloud plot for non-spam sms</p>

<img src="plots/wc2.png">

## Text preprocessing

<p> Stopwords and punctuation removal using <b>nltk</b> library </p>
<p> Text vectorization using <b>TFIDF-Vectorizer</b> </p>

## Model
<p> Decision Tree </p>

<img src="plots/report.png">

<p> Precision for spam sms is 0.92, that means very few non-spam sms have been predicted as spam sms. Recall is 0.79, that means out of all actual spam sms, 79% have been predicted as spam accurately. </p>

## Deploying model

<p> Saved the model in a file using the <b>pickle library</b> </p>
<p> Developed a web application using the <b>Flask API</b> </p>

<img src="plots/app.png">

<p> Containarized the application using <b>Docker</b> </p>

```FROM python:3.6-slim

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
```




