from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def go_to():
    if request.method == 'POST':
        if request == 'about_me':
            return redirect(url_for('home'))

    return render_template('terminal.html')

app.run(debug=True)