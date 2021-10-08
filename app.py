import pickle
from flask import Flask, render_template, request

#Global Variables
app=Flask(__name__)
loadedModel = pickle.load(open('Model.pkl','rb'))

#routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    alcohol=request.form['alcohol']
    sulphates =request.form['sulphates']
    citric_acid =request.form['citric_acid'] 
    fixed_acidity=request.form['fixed_acidity']
    pH=request.form['pH']
    residual_sugar=request.form['residual_sugar']
    chlorides=request.form['chlorides']

    prediction = loadedModel.predict([[alcohol,sulphates,citric_acid,fixed_acidity,pH,residual_sugar,chlorides]])
     
    if prediction[0]==3:
        prediction="WINE Quality is Noral Good"
    elif prediction[0] == 4:
       prediction="WINE Quality is Good"
    elif prediction[0] == 5:
       prediction="WINE Quality is Very GOOD"
    elif prediction[0] == 6:
       prediction="WINE Quality is AWESOME"
    elif prediction[0] == 7:
       prediction="WINE Quality is Fantastic"
    else:
       prediction="wine good is not good"
    return render_template('index.html', api_output=prediction)

#main function
if __name__ == '__main__':
    app.run(debug=True)
