# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, redirect, session
app = Flask(import_name=__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET', 'POST'])
def home():
    err = ''
    success = ''
    return render_template("index.html")

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

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    err = ''
    success = ''
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return render_template("index.html")



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




















