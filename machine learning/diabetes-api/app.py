#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('KNN Model.pkl', 'rb'))

#Routes

#Main function
if __name__ == '__main__':
    app.run(debug=True)