from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if not Email.validator(request.form):
        return redirect('/')
    # email = Email.get_one_by_email(request.form)
    # if request.form['email'] == email.email:
    #     flash("the email address you entered is already being used, please use a different email")
    #     return redirect('/')
    flash("The email address you entered is a valid email address")
    Email.create(request.form)
    return redirect('/emails')

@app.route('/emails')
def all_emails():
    return render_template('emails.html', all_emails = Email.get_all())

@app.route('/delete/<int:email_id>')
def delete(email_id):
    Email.delete({"id": email_id})
    return redirect('/emails')