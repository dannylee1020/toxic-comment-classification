import streamlit as st
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import joblib

import config
from process import process_texts


tokenizer = joblib.load(config.FILE_DIR + config.TOKENIZER)


def prepare_text(text):
    text_clean = process_texts(text)
    text_word_sequences = tokenizer.texts_to_sequences(text_clean)
    input_text = pad_sequences(text_word_sequences, maxlen = config.MAX_SEQUENCE_LENGTH, padding = 'post')

    return input_text



def make_prediction(data):
    model = load_model(config.FILE_DIR + config.MODEL)
    y_pred = model.predict(data)

    return y_pred



def clean_results(result):
    result_dict = {0:'toxic', 1:'severe_toxic', 2:'obscene', 3: 'threat', 4:'insult', 5:'identity_hate'}
    clean_result = []
    probability = []
    final_results = []
    for i in result:
        for index, num in enumerate(i):
            if np.round(num) == 1:
                clean_result.append(result_dict[index])
                probability.append(num)

    for i in zip(clean_result,np.round(probability,3)):
        final_results.extend(i)

    return final_results



def run():
    st.title('Classifying toxic comments on the web')
    st.text('')
    st.subheader('Overview')
    st.markdown('Hate speech is most prevalent among internet communities where anonymity of identity is easily achieved. Threat of abuse and harrassment online not only limits users to freely express their opinions but in worst case ruin other lives as witnessed from celebrities. Efforts made into developing models to effectively catch hate comments will improve overall user experience and faciliate good conversations within internet communities, building better online culture')
    st.text('')

    input_text = []

    comment = st.text_input('Write your test comment!')
    input_text.append(comment)

    if st.button('Predict'):
        with st.spinner('Making prediction now...'):
            if input_text is not '':
                text = prepare_text(input_text)
                pred = make_prediction(text).astype(float)
            else:
                st.write(f"[INFO] No input test comment was given. Please write them")

        pred_clean = clean_results(pred)

        if len(pred_clean) == 0:
            st.success("This comment does not contain hate speech. Thanks for being nice!")
        else:
            st.success(f"Predicted probabilities and tags for this comment are")
            st.write(pred_clean)







if __name__ == '__main__':

    run()




