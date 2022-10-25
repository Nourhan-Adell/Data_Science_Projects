
import pickle
import streamlit as st
import os
import pathlib
from pychorus import find_and_output_chorus 


def prepare_to_model(trained_file, d_datafram, d, model):
    prediction = model.predict(d_dataframe, d)

    return "The song will Hit ^^" if prediction == 1 else "The song will not Hit.."
    

def main():
    # front end elements of the web page 
    html_temp = """
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Reviewer ML App</h1> 
    </div> 
    """
    model_name = 'model.pkl'
    #vectorizer_name = 'tfidf_vectorizer.pk'
    with open(model_name, 'rb') as f:
        loaded_model = pickle.load(f)
    # with open(vectorizer_name, 'rb') as f:
    #     loaded_vect = pickle.load(f)

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    # # following lines create boxes in which user can enter data required to make prediction 
    # review = st.text_area('Review',("paste your review here"))
    # result =""

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prepare_to_model(d_dataframe, d, loaded_model) 
        st.success('Your review is {}'.format(result))
        print(result)
if __name__=='__main__': 
    main()