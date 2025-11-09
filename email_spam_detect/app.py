import pickle
from flask import Flask,render_template,request
with open('email_spam_detect/counter.pkl','rb') as f1:
    cv=pickle.load(f1)
with open('email_spam_detect/model.pkl','rb') as f2 :
    model=pickle.load(f2)

def is_spam(text):
    
    v_text = cv.transform([text])
    
    
    pred = model.predict(v_text)[0]
    
    
    return "spam" if pred == 1 else "ham"

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home() :
    if request.method=='POST' :
        text=request.form['email_text']
        result=is_spam(text)
        return render_template('home.html',predict=result)
    return render_template('home.html')
app.run(debug=True)
