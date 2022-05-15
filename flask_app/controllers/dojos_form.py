from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo_form import Dojo

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/show/info')
    return redirect('/')

@app.route('/show/info')
def show_info():
    return render_template('show_info.html', dojo = Dojo.get_last_dojo())

