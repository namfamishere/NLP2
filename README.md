# Intro
BERT and other Transformer encoder architectures have been widly successful on a variety of tasks in NLP.

BERT models are usually pre-trained on a large corpus of text, then fine-tuned for specific tasks.

In this work, we fine-tuned BERT to perform sentiment analysis on the dataset of IMDB movie reviews and deployed the trained model using Flask.

# Requirements

`pytorch`

`Flask`

Download the dataset `IMDB movie reviews` from [here](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).

Download the pre-trained BERT `bert-base-cased` from [here](https://www.kaggle.com/datasets/abhishek/bert-base-uncased).

Place the dataset and pre-trained BERT in the directory `input/`.
# How to run

Run `python train.py` to train the model and then get the accuracy on the test set.

Run `python app.py` to deploy the trained model using Flask and do inference on new examples.
