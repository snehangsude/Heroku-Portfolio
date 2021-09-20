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
    response = (json.loads(json.dumps(requests.get(url=url, headers=headers).text.strip('[]')))[:-15]) + "}"
    response = [eval(response)]
    return response

data = api()

# data = [{'id': 761019, 'title': 'The Start of Something Beautiful', 'html': '<h3><p>An introduction towards programming language and the underlying work of Import Statements.</p></h3>\n<hr>\n<h2>Preface</h2>\n<p><blockquote><strong><em>"In vain have you acquired knowledge if you have not imparted it to others."</em></strong></blockquote></p>\n<p><p>I\'ve been thinking since the start of time as to write <strong>Expected Space. </strong>Well, probably I\'m exaggerating a bit but here\'s to the<strong> first one.</strong></p></p>\n<h2>Chapter 1 : Language</h2>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/096/178/original/Anubis-Egyptian-Book-of-the-Dead.jpg?1631635524" />Art, Culture And Language[/caption]\n<p><blockquote><em>"For millions of years mankind lived just like the animals.</em></blockquote><blockquote><em>Then something happened which unleashed the power of our imagination,</em></blockquote><blockquote><em>We learned to talk."</em></blockquote><p><br></p><p>Quoting from the lines of <em>Pink Floyd</em>, it\'s simple to understand how communication has shaped our society, likely the single most important thing that has made civilizations stand. While we have created types of communication for us humans, since the age of machines we have learned to communicate with machines too, and surprisingly it spans back to the 40s.</p><p>I wanted to start with the history as to where do programming languages come from, as they help us understand why we are working with them. Plus it narrates a nice story on how far we have come. As we begin, today we will be discussing <strong>Import Statements.</strong> However, here\'s a quick look at what the first high-level language looked like.</p></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/100/168/original/hello_world_Plankuuul.png?1631652133" />Printing \'Hello World\' in Plankalkül[/caption]\n<p><p>Traumatizing, right? I agree we have come a long way from the above image to <code>print(\'Hello, world!\')</code>. </p><p>Let\'s begin!</p></p>\n<h2>Section 1: Imports in Python 🐍</h2>\n<p><p>To help us understand what and how imports work, let\'s assume we have a module (basically a sheet of code) named <code>dinosaur.py</code> that has</p><blockquote><code>&gt;&gt; type = 20 </code> [A variable]</blockquote><blockquote><code>&gt;&gt; def roar(name): </code> [A function <em>(Functions, in my next newsletter)</em>]</blockquote><blockquote><code>      return f\'{name} roars\'</code></blockquote><p>We can import this module in two different ways :</p><p><strong>Import statement 1: </strong></p><blockquote><code>&gt;&gt; import dinosaur</code></blockquote><p><strong>Import statement 2: </strong></p><blockquote><code>&gt;&gt; from dinosaur import roar</code></blockquote><p>Here are few general pointers for <strong>import </strong>-</p><ul><li>Imports are statements and not functions</li><li>Importing <code>dinosaur.py</code> creates a variable name <code>dinosaur </code>and also creates another variable <code>type</code> which is inside the <code>dinosaur.py</code> module</li><li>Importing creates a module object <em>(object can be defined as a blueprint)</em> and sets a variable (the name of the module) to point to that module object. <strong><em>[Defined in the 3rd point]</em></strong></li></ul><p>Running <strong>Import statement 1 </strong>executes the module line by line. So, when I call the statement :</p><ol><li>It defines the global variable <code>type </code>as an integer.</li><li>Defines the global variable <code>roar </code>as a function that takes one argument.&nbsp;</li><li>Then <code>import </code>defines a variable <code>dinosaur</code>, through whose attributes (<code>dinosaur.type</code> and <code>dinosaur.roar</code>) we can get to our variable and function.</li></ol><p>Running <strong>Import statement 2 </strong>executes the module but only by the respective variable <code>roar</code>. So, when I call the statement :</p><ol><li>It defines only the variable <code>roar</code> to be used inside the program.</li><li>It would not define a variable under the module name, so we would not have a variable named <code>dinosaur</code> anymore.</li></ol><p>There is one other rare way to import which should be avoided at all costs. </p><p><code>&gt;&gt; from dinosaur import *</code> [This causes to replace all variables in your local namespace]</p><p><strong>A namespace is the current *.py file we would be working on, or importing the statements to.</strong></p><p>Here\'s a picture to understand better how variables work inside namespaces when imported.</p></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/101/230/original/Figma-namespace.PNG?1631657793" />An abstract idea on how imports work and namespaces[/caption]\n<h2>A Space about Expected Space</h2>\n<p><p>As this is the first issue, let me share what my plans are. I\'m sure they would be updated with time but here\'s my goal -</p><p>I hope to send this newsletter with the idea of <strong>breaking down the underlying concepts of complex topics as stories</strong> thrice a month. Additionally, I hope to <em>talk about growth, motivation, and something intricate </em>once a month.</p><blockquote>The underlying objective is to interact as one can only grow as we connect.</blockquote><p>If you have any interesting suggestions, feel free to connect with me on Twitter. I hope this message finds you in good health, see you next week!</p></p>\n', 'sent_at': '2021-09-15T18:13:39.704Z', 'description': '<p>An introduction towards programming language and the underlying work of Import Statements.</p>', 'url': 'https://www.getrevue.co/profile/xSpace/issues/the-start-of-something-beautiful-761019'}]

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
        return render_template('contact.html', form=form, msg=True)
    return render_template('contact.html', form=form, msg=False)


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
