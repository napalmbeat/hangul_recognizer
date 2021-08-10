import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
from PIL import Image
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, balanced_accuracy_score, precision_score, recall_score, matthews_corrcoef, f1_score, cohen_kappa_score
import base64


# Calculates performance metrics
def calc_metrics(input_data):
    Y_actual = input_data.iloc[:,0]
    Y_predicted = input_data.iloc[:,1]
    acc = accuracy_score(Y_actual, Y_predicted)
    balanced_accuracy = balanced_accuracy_score(Y_actual, Y_predicted)
    precision = precision_score(Y_actual, Y_predicted, average='weighted')
    recall = recall_score(Y_actual, Y_predicted, average='weighted')
    mcc = matthews_corrcoef(Y_actual, Y_predicted)
    f1 = f1_score(Y_actual, Y_predicted, average='weighted')
    cohen_kappa = cohen_kappa_score(Y_actual, Y_predicted)

    acc_series = pd.Series(acc, name='Accuracy')
    balanced_accuracy_series = pd.Series(balanced_accuracy, name='Balanced_Accuracy')
    precision_series = pd.Series(precision, name='Precision')
    recall_series = pd.Series(recall, name='Recall')
    mcc_series = pd.Series(mcc, name='MCC')
    f1_series = pd.Series(f1, name='F1')
    cohen_kappa_series = pd.Series(cohen_kappa, name='Cohen_Kappa')

    df = pd.concat( [acc_series, balanced_accuracy_series, precision_series,
                     recall_series, mcc_series, f1_series, cohen_kappa_series], axis=1 )
    return df

# Calculates confusion matrix
def calc_confusion_matrix(input_data):
    Y_actual = input_data.iloc[:,0]
    Y_predicted = input_data.iloc[:,1]
    confusion_matrix_array = confusion_matrix(Y_actual, Y_predicted)
    confusion_matrix_df = pd.DataFrame(confusion_matrix_array, columns=['Actual','Predicted'], index=['Actual','Predicted'])
    return confusion_matrix_df

# Load example data
def load_example_data():
    df = pd.read_csv('Y_example.csv')
    return df

# Download performance metrics
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="performance_metrics.csv">Download CSV File</a>'
    return href



def app():
    st.title('Hangul syllable recognizer')

    #st.write("This is the `Data` page of the multi-page app.")

    #st.write("The following is the DataFrame of the `iris` dataset.")

    # Sidebar - Header
    st.sidebar.header('Input panel')
    # st.sidebar.markdown("""""")

    # Sidebar panel - Upload input file
    uploaded_file = st.sidebar.file_uploader('Upload your handwriting file', type=['png', 'jpg', 'jpeg'])

    # Sidebar panel - Performance metrics
    # performance_metrics = ['Accuracy', 'Balanced_Accuracy', 'Precision', 'Recall','MCC', 'F1', 'Cohen_Kappa']
    # selected_metrics = st.sidebar.multiselect('Performance metrics', performance_metrics, performance_metrics)

    # Main panel
    image = Image.open('logo.png')

    if uploaded_file is not None:
        image2 = Image.open(uploaded_file)
        st.image(image2, width=200)
    else:
        st.info('Awaiting the upload of the input file.')
        if st.button('Use Example Data'):
            input_df = load_example_data()
            confusion_matrix_df = calc_confusion_matrix(input_df)
            metrics_df = calc_metrics(input_df)
            selected_metrics_df = metrics_df[selected_metrics]
            st.header('Input data')
            st.write(input_df)
            st.header('Confusion matrix')
            st.write(confusion_matrix_df)
            st.header('Performance metrics')
            st.write(selected_metrics_df)
            st.markdown(filedownload(selected_metrics_df), unsafe_allow_html=True)
