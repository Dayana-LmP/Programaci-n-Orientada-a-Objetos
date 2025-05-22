#Práctica 15: Flask
#Hola mundo en Flask 

from flask import Flask 
app=Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hello world!!!'

if __name__ =='__main__':
    app.run(debug=True)
    