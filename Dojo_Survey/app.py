from flask import Flask, render_template, request, redirect, session

app = Flask (__name__)
app.secret_key = "stop"

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/user', methods =['POST'])
def index_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')

    
@app.route('/delete')
def delete():
    session.clear()
    return render_template('/')



if __name__ == '__main__':
    app.run(debug = True, port = 5001)