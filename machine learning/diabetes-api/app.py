#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('KNN Model.pkl', 'rb'))

#www.google.co.in/prediction

#Routes
@app.route('/')
def home():
    return render_template('diabetes.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    glucose = int(request.form['glucose'])
    bmi = int(request.form['bmi'])
    age = int(request.form['age'])

    prediction = loadedModel.predict([[glucose, bmi, age]])[0]

    if prediction == 0:
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"

    return render_template('diabetes.html', output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True)