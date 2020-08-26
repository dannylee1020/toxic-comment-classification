# Identifying abusive comments

## Project Overview
Hate speech is most prevalent among internet communities where anonymity of identity is easily achieved. Threat of abuse and harrassment online not only limits users to freely express their opinions but in worst case ruin other lives as witnessed from celebrities. Efforts made into developing models to effectively catch hate comments will improve overall user experience and faciliate good conversations within internet communities, building better online culture

## Model Overview
For this project, I am using GloVe embedding with one layer of bidirectional LSTM followed by fully connected layer for prediction. There were other great ideas as to how to go about modeling, 1D ConvNet + LSTM and traditional ML techniques like SVM for example. But I am sticking with deep learning approach. One thing to note is that this dataset seems to be prone to overfitting. Even slight complexity to the model showed signs of overfitting. The model was trained using google colab's GPU. For more details about model building, refer to .ipynb notebook
<br>
<br>
<br>
<img src="https://github.com/dannylee1020/toxic-comment-classification/blob/master/files/toxic_model_structure.png" width="480" height="300">

## Run with Docker
launch the streamlit app with docker:

		`docker build -t dannylee1020/toxic-comment .
		`docker run -p 8501:8501 dannylee1020/toxic-comment:latest

then visit [localhost:8501](https://localhost:8501) to view the app


## Reference
[Kaggle](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/overview)
