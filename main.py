from flask import Flask,render_template,request
import gen_content_openai
import extract_named_entities

app = Flask(__name__)


@app.route('/',methods =['GET','POST'])
def index():
    content = None
    entities = None
    if request.method == 'POST':
        text = request.form['text']
        content = gen_content_openai.gen_content(text)
        entities = extract_named_entities.extract(content)
    return render_template('index.html',title = 'Home',content=content,entities=entities)

if __name__ == '__main__':
    app.run(debug=True,port=1234)