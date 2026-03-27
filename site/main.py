from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/my_projects')
def my_projects():
    return render_template('my_projects.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/web-pages')
def web_pages():
    return render_template('web_pages.html')

@app.route('/',methods=['GET','POST'])
def go_to():
    if request.method == 'POST':
        if request.form['command'] == 'about_me':
            return redirect(url_for('about_me'))
        elif request.form['command'] == 'my_projects':
            return redirect(url_for('my_projects'))

    return render_template('terminal.html')

app.run(debug=True)
