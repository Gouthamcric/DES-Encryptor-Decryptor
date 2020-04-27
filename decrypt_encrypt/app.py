from flask import Flask,request,render_template,jsonify
from encryption import *
from decryption import *
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process',methods= ['POST'])
def process():
      message = request.form['message']
      key = request.form['key']
      if(request.form['func']=="encryption"):
        output = encryption(message,key)
      else:
        output = decryption(message,key)
      return output

if __name__ == '__main__':
    app.run(debug=True)