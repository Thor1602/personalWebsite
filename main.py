# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, redirect, session, flash
import dbHelper
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/assets/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(import_name=__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/", methods=['GET', 'POST'])
def home():
    err = ''
    success = ''
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/blog", methods=['GET', 'POST'])
def blog():
    err = ''
    success = ''
    return render_template("blog.html")

@app.route("/projects", methods=['GET', 'POST'])
def projects():
    err = ''
    success = ''
    return render_template("projects.html")

@app.route("/tutorials", methods=['GET', 'POST'])
def tutorials():
    err = ''
    success = ''
    return render_template("tutorials.html")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    err = ''
    success = ''
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            # check if the post request has the file part
            print(request.form)
            if 'blogFile' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['blogFile']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], "blog_upload_" + filename))
                return redirect(url_for('admin', filename=filename))
        return render_template("admin.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    # if session.get('logged_in'):
    #     return redirect(url_for('admin'))
    if session.get('logged_in'):
        return redirect(url_for('admin'))
    if request.method == 'GET':
        return render_template('login.html')
    else:
        condition = False
        name = request.form['username']
        passw = request.form['password']

        try:
            user = dbHelper.User(name, passw, True)
            if user.check_user():
                session['logged_in'] = True
                if 'rememberMe' in request.form:
                    session.permanent = True
                else:
                    session.permanent = False
                return redirect(url_for('admin'))
            else:
                condition = True
                err = "Oops, the credentials don't match"
                return render_template('login.html', err=err, condition=condition)
        except:
            err = 'Something strange happened while trying to log in'
            return render_template('404.html', err=err, condition=condition)

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', err=e), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('404.html', err=e), 403

@app.errorhandler(410)
def page_gone(e):
    return render_template('404.html', err=e), 410

@app.errorhandler(500)
def internal_error(e):
    return render_template('404.html', err=e), 500

if __name__ == "__main__":
    app.secret_key = "HopKIdf78/*9*PO72xQ89Fg??"
    app.run(debug=True)




















