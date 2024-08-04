from flask import Flask,render_template,redirect,request
from main import predict_news,evaluation

app=Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('index.html')
@app.route('/main',methods=['GET','POST'])
def main():
    if request.method=='POST':
        text=request.form['text']
        result=predict_news(text)
        accuracy,classify=evaluation()
        if ' ' not in text:
            result='Not valid'
        return render_template('main.html',userinput=text,result=result,accuracy=accuracy)
    return render_template('main.html')

if __name__=='__main__':
    app.run(debug=True)