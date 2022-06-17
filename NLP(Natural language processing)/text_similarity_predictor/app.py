import numpy as np
from flask import Flask, request, jsonify, render_template
import spacy

import pickle
nlp = spacy.load('en_core_web_md')

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    sentences = [x for x in request.form.values()]
    doc1 = nlp(sentences[0]) 
    doc2 = nlp(sentences[1])
    output = doc1.similarity(doc2)
    
    
    return render_template('index.html',prediction_text='The similarity score for the given sentences is : {} '.format(output))

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)