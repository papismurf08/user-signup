from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])

def index():

    username = ''
    email = ''
    username_error = ''
    password_error = ''
    password_verify_error = ''
    email_error = ''
    title = 'User-Signup'

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        password_verify = request.form['password_verify']
        email = request.form['email']

        for i in username:

            if i.isspace():
                username_error = "Username Can't Contain Spaces."
                username = ''

            elif (len(username) < 3) or (len(username) > 20):
                username_error = 'Username Needs to be 3-20 Characters Long.'
                username = ''

        if not username:
            username_error = 'Not a Valid Username'
            username = ''

        for i in password:

            if i.isspace():
                password_error = "Password Can't Contain Spaces."

            elif (len(password) < 3) or (len(password) > 20):
                password_error = "Password Must be 3-20 Characters Long Without Spaces."

        if not len(password):
            password_error = 'Not a Valid Password'

        if password != password_verify:
            password_verify_error = 'Passwords do not Match.'

        if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = 'This is not a Valid Email.'
            email = ''

        if (not username_error) and (not password_error) and (not password_verify_error) and (not email_error):
            return redirect('/welcome?username={0}'.format(username))

    return render_template('index.html', title=title, username=username, email=email,
                           username_error=username_error, password_error=password_error,
                           password_verify_error=password_verify_error, email_error=email_error)


@app.route('/welcome')
def welcome():
    title = "Welcome"
    username = request.args.get('username')
    return render_template('welcome.html', title=title, username=username)


if __name__ == '__main__':
    app.run()