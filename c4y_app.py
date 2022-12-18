import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

st.title('Credit 4 You')
st.write('Demo-App zur Evaluation des Klassifikationsalgorithmus zur Risikobeurteilung von Konsumkrediten')

PATH_MODEL = os.path.join('models', 'clfn.joblib')

@st.cache
def load_model(path_model):
    return joblib.load(path_model)

num_features = ['Alter', 'Kreditbetrag', 'Laufzeit']

cat_features = [('Geschlecht', ['männlich', 'weiblich']),
                ('Arbeitsstelle',['hohe Qualifikation',
                                  'mittlere Qualifikation',
                                  'niedrige Qualifikation - permanent',
                                  'niedrige Qualifikation - temporär']),
                ('Wohnsituation', ['Eigentum', 'Miete', 'kostenlos']),
                ('Sparkonto', ['gering', 'hoch', 'mittel', 'sehr hoch', 'nan']),
                ('Lohnkonto', ['gering', 'hoch', 'mittel', 'nan']),
                ('Verwendungszweck',['Ausbildung','Fahrzeug','Ferien/andere',
                                     'Geschäft','Haushaltsgeräte','Unterhalt',
                                     'Unterhaltungselektronik','Wohnungsreinrichtung'])]

clf = load_model(PATH_MODEL)

st.header('Eingabe-Formular')

options = [st.selectbox(feat, cats) for feat, cats in cat_features]

numbers = [st.number_input(feat) for feat in num_features]

input_data = {feat: options[i] for i, (feat, _) in enumerate(cat_features)}
for i, feat in enumerate(num_features):
    input_data[feat]=numbers[i]

#st.write('The current input is ', str(input_data))
    
pred = clf.predict(pd.DataFrame.from_records([input_data]))[0]

map_out = {0:'SCHLECHT', 1:'GUT'}

st.header('Risiko-Beurteilung')

st.write('Resultierende Risiko-Klassifizierung: ', map_out[pred])
