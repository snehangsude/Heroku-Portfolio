from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import smtplib
import requests
import os
import json
from data import Post

email_id = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
token = os.environ.get('TOKEN')
url = os.environ.get('URL')


def api():
    headers = {'Authorization': f'Token {token}'}
    response = (json.loads(json.dumps(requests.get(url='https://www.getrevue.co/api/v2/issues',
                                                   headers=headers).text.strip('[]')))[:-15]) + "}"
    response = [eval(response)]
    return response


data = api()
all_posts = []
for item in data:
    post = Post(id_=item.get('id'), title=item.get('title'), description=item.get('description'),
                sent_at=item.get('sent_at'), html=item.get('html'))
    all_posts.append(post)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


class ContactForm(FlaskForm):
    name = StringField('How shall I address you?', validators=[DataRequired()])
    email = StringField('Where do I connect with you?', validators=[DataRequired()])
    subject = StringField('Which subject are you referring to?', validators=[DataRequired()])
    message = TextAreaField('What can I help you with?', validators=[DataRequired()])
    submit = SubmitField('Send Message')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/resume")
def resume():
    return render_template('resume.html')


@app.route("/projects")
def project():
    return render_template('projects.html')


@app.route("/blog")
def blog():
    return render_template('blog.html', data=all_posts)


@app.route("/blogpost/<int:num>")
def blogpost(num):
    requested_post = None
    for article in all_posts:
        if num == post.id:
            requested_post = article
    return render_template('post.html', post=requested_post)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        send_email(name=name, email=email, subject=subject, message=message)
    return render_template('contact.html', form=form)


def send_email(name, email, subject, message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=email_id, password=password)
        connection.sendmail(
            from_addr=email_id,
            to_addrs=email_id,
            msg=f"Subject: Website{subject}\n\nName:{name}\nEmail:{email}\nMessage:{message}")


if __name__ == '__main__':
    app.run(debug=True)
