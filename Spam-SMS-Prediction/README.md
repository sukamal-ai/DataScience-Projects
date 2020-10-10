# SPAM SMS PREDICTION

<p> Goal: Build an application (end to end) that predicts if an SMS is spam or not </p>

## EDA and Preprocessing

<p>Wordcloud plot for spam sms</p>

<img src="plots/wc1.png">

<p> Highly used words in spam sms are - FREE, text, call, txt etc.

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

<p> Saved the model in a file using pickle library </p>
<p> Developed a web application using Flask API </p>

<img src="plots/app.png">

<p> Containarized the application using Docker </p>



