from flask import Flask, render_template, request, redirect
from main import predict_news, evaluation
from forfiles import pdf, txt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files.get('file')
        
        if file:
            if file.filename.endswith('.pdf'):
                text = pdf(file)
            elif file.filename.endswith('.txt'):
                text = txt(file)
            else:
                return render_template('main.html', result='Unsupported file type')
        else:
            text = request.form.get('text', '').strip()

        if isinstance(text, bytes):
            text = text.decode('utf-8')

        if ' ' not in text:
            result = 'Not valid'
        else:
            result = predict_news(text)
            accuracy, classify = evaluation()
            return render_template('main.html', userinput=text, result=result, accuracy=accuracy)

    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
