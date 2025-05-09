from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def get_data():
    return{"mensaje":"Hola desde Flask"}

def home():
    return render_template('index.html',
                           title='Dashboard',
                           data= get_data())
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '_main_':
    app.run(host = '0.0.0.0', port=5000)
    
