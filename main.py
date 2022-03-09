from flask import Flask, render_template, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import smtplib
import requests
import os
from data import Post

email_id = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
token = os.environ.get('TOKEN')
url = os.environ.get('URL')


def api():
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url=url, headers=headers).json()
    return response

# data = api()
data = [{'id': 766932, 'title': 'The Art of Functions', 'html': '<h3><p>A deep dive into the art of functions and when to use them.</p></h3>\n<hr>\n<h2>Section 2: Functions</h2>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/288/564/original/part_2.jpg?1632421783" />[/caption]\n<p><p>Wondering, what\'s up with this weird ancient art? Well, they help portray how civilization evolved much like how we learned to evolve our ways to talk to machines. Like us humans divided our society to do specific tasks say carpenters to work with wood, barbers to trim our hairs, similarly, we can ask machines to work specifically on something or take a specific action when some work is given. As an example imagine, when we wake up, we follow the below step - </p><p><strong>Get your bed done &gt; Brush your teeth &gt; Wash your face &gt; Dry your face</strong></p><p>For machines, these are described as functions. To understand what a function is imagine a set of instructions that needs to be done when something happens. </p><p>Now you might think why do we need to have functions? It\'s simple, however much we like to abuse <strong>Ctrl+C</strong> &amp; <strong>Ctrl+V </strong>it\'s not a good practice to have repeatable code. Instead, every time you have to do the same action, you can simply call the function to make it work. </p></p>\n<h2>Fundamentals of Functions</h2>\n<p><p>In Python, there are two kinds of functions -<strong> Built-in functions</strong> and <strong>User-defined functions</strong>. We will talk about Built-in functions in a later post. </p><p>Today, we will discuss the three kinds of <u>User-defined functions</u>, let\'s start with the basic one. To write any function we need to have a few important things in mind -</p><ol><li>A function should always start with <code>def</code> word</li><li>The <code>def</code> will be followed by the name of the function, recommended in all lower case</li><li>The name of the function is followed by a parenthesis and colon <code>():</code> , denoting the end of defining a function</li><li>Any lines inside the function should be indented to work under the function call.</li><li>Optional requirement, a docstring can be added right below the function.</li></ol><p>Here\'s how it would look like. 👇</p></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/289/911/original/Function__2301.png?1632427737" />[/caption]\n<p><p>Now the important takeaway from here is how a function when defined doesn\'t do anything, which means that it would be defined inside the variable <code>wake_up</code> when you run the file, however, you would need to call it to make sure it does what you have asked it to do. You can call it by writing the unique name of the function you have defined, followed by the parenthesis. </p><p>Here, I\'ve asked it to print<strong> <em>I woke up at 8 AM</em></strong></p></p>\n<p><p>Before we jump into understanding the other two types of functions and when to use them, we need to understand two important concepts:</p><ul><li><strong>Parameters</strong> - Parameters are something that your function can take and work with, inside the function. Think of it as a variable inside a function that can take inputs or can be optional too.</li><li><strong>Arguments</strong> - Arguments are the values that you would assign to your parameter when calling the function. Think of it as assigning a value to the pre-defined parameters. Arguments are again defined into two groups:</li></ul><ol><li><strong><em>Positional Arguments</em></strong> - Arguments that are called into functions based on the positions of the paraments.</li><li><strong><em>Keyword Arguments</em></strong> - Arguments that are called into functions using the same keyword that is used to define the parameters.</li></ol><p>As we have grasped the basic idea of Parameters and Arguments let\'s dive into the next type of function *<em>drum-roll* </em>-</p><h2><strong>Functions with inputs 👇</strong></h2></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/290/173/original/Function__2302.png?1632429172" />[/caption]\n<p><p>Here, we can see that <code>wake_up</code> has two parameters <code>time</code> &amp; <code>meridian</code>. You can see that <code>time </code>requires a value however <code>meridian </code>has a pre-assigned value of a string <code>\'AM\'</code>, which means that the meridian is optional for you to assign. Here\'s how you can call this function:</p><p><strong>Calling the function with only the required data</strong> - </p><ul><li><em><u>Positional argument:</u></em> <code>wake_up(12)</code>  --&gt; This will print <strong><em>I woke up at 12 AM</em></strong></li><li><em><u>Keyword argument:</u> </em><code>wake_up(time=12)</code>  --&gt; This will print <strong><em>I woke up at 12 AM</em></strong></li></ul><p><em>Here, the </em><code><em>12</em></code><em> gets assigned to the </em><code><em>time </em></code><em>variable whereas the </em><code><em>meridian </em></code><em>uses the </em><code><em>\'AM\'</em></code><em> as the default value.</em></p><p><strong>Calling the function with both data</strong> -</p><ul><li><em><u>Positional argument:</u> </em><code>wake_up(12, \'PM\')</code> --&gt; This will print <strong><em>I woke up at 12 PM</em></strong></li><li><em><u>Keyword argument:</u> </em><code>wake_up(meridian=\'PM\', time=12)</code> --&gt; This will print <strong><em>I woke up at 12 PM</em></strong></li></ul><p><em>Here, the </em><code><em>12</em></code><em> gets assigned to the </em><code><em>time</em></code><em> variable and the </em><code><em>meridian</em></code><em> gets assigned to the </em><code><em>\'PM\'</em></code><em> value. This is one of the benefits of using keyword variables as it doesn\'t require the position of arguments to match the position of parameters. </em></p><p><strong><u>Note:</u> </strong>Changing the positional argument <code>wake_up(\'PM\', 12)</code> would print --&gt; <strong><em>I woke up at PM 12</em></strong></p><h2><strong>Functions with inputs and outputs 👇</strong></h2></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/291/108/original/Function__2303.png?1632434550" />[/caption]\n<p><p>This is probably the most used kind of function and is really handy to work with. Almost every rule stays the same from when we defined the <strong>Fundamentals of Functions </strong>apart from the addition of one:</p><ol><li>As this gives us an output a command <code>return</code> is added at the end which allocates the output to a variable outside the function which can then be re-used.</li></ol><p><strong><u>Note:</u> </strong>Anything after the command <code>return</code> would be ignored by the console as the function would immediately end and allocate the value.</p><p><strong>Calling the function with positional argument - </strong></p><p><code>returned_value = add(2, 3)</code> --&gt; This doesn\'t print any value but instead allocated the variable <code>returned_value</code> with <code>5</code>. </p><p><em>Try this out and see, how the print statement is absolutely ignored by the console. </em></p><p><strong>Calling the function with keyword argument - </strong></p><p><code>returned_value = add(number1 = 6, number2 = 3)</code> --&gt; This too doesn\'t print any value but instead allocated the variable <code>returned_value</code> with <code>9</code>. </p></p>\n<h2>Conclusion</h2>\n<p><p>We have now understood the types of functions that we can write to help us talk to machines efficiently, without having to repeat ourselves. However, sometimes, we speak in languages our machines have a hard time understanding, those are bugs or errors in our code. </p><p>Here are a few common ones for you to catch: </p><ol><li>Missing an argument, if your function has parameters would pop a <code>TypeError</code></li><li>Writing a Keyword argument before a Positional argument would result in <code>SyntaxError</code></li><li>Any line of code after the return command on the same indentation level would be ignored.</li></ol><p>Here\'s an image that summarizes how functions are trigger and how they work. </p><ol><li><strong>The code starts execution from the arrow tail and follows its head</strong></li><li><strong>When it hits the star</strong></li><li><strong>It jumps to see the function under the name of </strong><code>sum</code></li><li><strong>Executes everything inside the function taking the arguments to replace the parameters</strong></li><li><strong>Hits the </strong><code>return </code><strong>statement</strong></li><li><strong>Allocates the value of the </strong><em>local variable</em><strong> </strong><code>num<strong> </strong></code><strong>to the </strong><em>global variable</em><strong> </strong><code>addition</code></li></ol></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/291/499/original/Params.PNG?1632437863" />[/caption]\n<p><p>That\'s it for this week, hope you were able to understand the types of functions and why they are used in day-to-day code. </p><p>We will discuss more on when to use which function and dive into the concept of variables from the Function with input and output more on the next issue. We would also discuss the utility of functions on later issues moving towards Classes.</p><p>I hope this message finds you in good health, see you next week!</p></p>\n', 'sent_at': '2021-09-23T23:16:41.420Z', 'description': '<p>A deep dive into the art of functions and when to use them.</p>', 'url': 'https://www.getrevue.co/profile/xSpace/issues/the-art-of-functions-766932', 'active': False}, {'id': 761019, 'title': 'The Start of Something Beautiful', 'html': '<h3><p>An introduction towards programming language and the underlying work of Import Statements.</p></h3>\n<hr>\n<h2>Preface</h2>\n<p><blockquote><strong><em>"In vain have you acquired knowledge if you have not imparted it to others."</em></strong></blockquote></p>\n<p><p>I\'ve been thinking since the start of time as to write <strong>Expected Space. </strong>Well, probably I\'m exaggerating a bit but here\'s to the<strong> first one.</strong></p></p>\n<h2>Chapter 1 : Language</h2>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/096/178/original/Anubis-Egyptian-Book-of-the-Dead.jpg?1631635524" />Art, Culture And Language[/caption]\n<p><blockquote><em>"For millions of years mankind lived just like the animals.</em></blockquote><blockquote><em>Then something happened which unleashed the power of our imagination,</em></blockquote><blockquote><em>We learned to talk."</em></blockquote><p><br></p><p>Quoting from the lines of <em>Pink Floyd</em>, it\'s simple to understand how communication has shaped our society, likely the single most important thing that has made civilizations stand. While we have created types of communication for us humans, since the age of machines we have learned to communicate with machines too, and surprisingly it spans back to the 40s.</p><p>I wanted to start with the history as to where do programming languages come from, as they help us understand why we are working with them. Plus it narrates a nice story on how far we have come. As we begin, today we will be discussing <strong>Import Statements.</strong> However, here\'s a quick look at what the first high-level language looked like.</p></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/100/168/original/hello_world_Plankuuul.png?1631652133" />Printing \'Hello World\' in Plankalkül[/caption]\n<p><p>Traumatizing, right? I agree we have come a long way from the above image to <code>print(\'Hello, world!\')</code>. </p><p>Let\'s begin!</p></p>\n<h2>Section 1: Imports in Python 🐍</h2>\n<p><p>To help us understand what and how imports work, let\'s assume we have a module (basically a sheet of code) named <code>dinosaur.py</code> that has</p><blockquote><code>&gt;&gt; type = 20 </code> [A variable]</blockquote><blockquote><code>&gt;&gt; def roar(name): </code> [A function <em>(Functions, in my next newsletter)</em>]</blockquote><blockquote><code>      return f\'{name} roars\'</code></blockquote><p>We can import this module in two different ways :</p><p><strong>Import statement 1: </strong></p><blockquote><code>&gt;&gt; import dinosaur</code></blockquote><p><strong>Import statement 2: </strong></p><blockquote><code>&gt;&gt; from dinosaur import roar</code></blockquote><p>Here are few general pointers for <strong>import </strong>-</p><ul><li>Imports are statements and not functions</li><li>Importing <code>dinosaur.py</code> creates a variable name <code>dinosaur </code>and also creates another variable <code>type</code> which is inside the <code>dinosaur.py</code> module</li><li>Importing creates a module object <em>(object can be defined as a blueprint)</em> and sets a variable (the name of the module) to point to that module object. <strong><em>[Defined in the 3rd point]</em></strong></li></ul><p>Running <strong>Import statement 1 </strong>executes the module line by line. So, when I call the statement :</p><ol><li>It defines the global variable <code>type </code>as an integer.</li><li>Defines the global variable <code>roar </code>as a function that takes one argument.&nbsp;</li><li>Then <code>import </code>defines a variable <code>dinosaur</code>, through whose attributes (<code>dinosaur.type</code> and <code>dinosaur.roar</code>) we can get to our variable and function.</li></ol><p>Running <strong>Import statement 2 </strong>executes the module but only by the respective variable <code>roar</code>. So, when I call the statement :</p><ol><li>It defines only the variable <code>roar</code> to be used inside the program.</li><li>It would not define a variable under the module name, so we would not have a variable named <code>dinosaur</code> anymore.</li></ol><p>There is one other rare way to import which should be avoided at all costs. </p><p><code>&gt;&gt; from dinosaur import *</code> [This causes to replace all variables in your local namespace]</p><p><strong>A namespace is the current *.py file we would be working on, or importing the statements to.</strong></p><p>Here\'s a picture to understand better how variables work inside namespaces when imported.</p></p>\n[caption align="alignnone" width="980"]<img alt="" src="https://s3.amazonaws.com/revue/items/images/011/101/230/original/Figma-namespace.PNG?1631657793" />An abstract idea on how imports work and namespaces[/caption]\n<h2>A Space about Expected Space</h2>\n<p><p>As this is the first issue, let me share what my plans are. I\'m sure they would be updated with time but here\'s my goal -</p><p>I hope to send this newsletter with the idea of <strong>breaking down the underlying concepts of complex topics as stories</strong> thrice a month. Additionally, I hope to <em>talk about growth, motivation, and something intricate </em>once a month.</p><blockquote>The underlying objective is to interact as one can only grow as we connect.</blockquote><p>If you have any interesting suggestions, feel free to connect with me on Twitter. I hope this message finds you in good health, see you next week!</p></p>\n', 'sent_at': '2021-09-15T18:13:39.704Z', 'description': '<p>An introduction towards programming language and the underlying work of Import Statements.</p>', 'url': 'https://www.getrevue.co/profile/xSpace/issues/the-start-of-something-beautiful-761019', 'active': False}]

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


@app.route("/download")
def download():
    full_path = 'static/images'
    file = "Snehangsu's Resume.pdf"
    return send_from_directory(full_path, file, as_attachment=True)


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
        if num == article.id:
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
