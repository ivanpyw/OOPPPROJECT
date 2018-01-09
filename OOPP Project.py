from flask import Flask, redirect, url_for, request, flash, session, render_template
from wtforms import Form, StringField, PasswordField
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('stop-78245-firebase-adminsdk-jqcbt-032e64dc12.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://stop-78245.firebaseio.com/'

})

root = db.reference()
app = Flask(__name__)

class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')

class registerform(Form):
    username = StringField('Username')
    password = PasswordField('Password')


@app.route('/')
def Home():
    return render_template("index.html")


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/afterstafflogin/')
def afterstafflogin():
    return render_template('afterstafflogin.html')

@app.route('/bill/')
def Bill():
    return render_template('bills.html')

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/Monitoring/')
def ward():
    return render_template("Monitoring.html")

@app.route('/Forms/')
def elements():
    return render_template("elements.html")

@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/services/')
def services():
    return render_template("services.html")

@app.route('/left-sidebar/')
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route('/Purchase/')
def right_sidebar():
    return render_template("right-sidebar.html")

@app.route('/request/')
def patientrequest():
    return render_template('form.html')

@app.route("/register/")
def registering():
    return render_template("register.html")

@app.route("/symptom/")
def symptom():
    return render_template("symptoms.html")

@app.route('/needhelp/')
def needhelp():

    if request.method == 'POST':
        patient_id = 'P00001'
        ward = 'A'
        bed_no = 'A1'
        requests = ['Water', 'Food']

        r = Request(patient_id, bed_no, ward, requests)

    return render_template('form.html')

@app.route('/aftersubmitbill/')
def aftersubmitbill():
    return render_template("aftersubmitbill.html")
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    print(request.method)

    if request.method == 'POST' and form.validate():
        username = request.form["username"]
        password = request.form["password"]
        ifUserExists = root.child('messages').order_by_child('username').equal_to(username).get()
        for k, v in ifUserExists.items():
            print(k, v)
            # print(sha256_crypt.encrypt(password))
            print(v['username'])
            print(v['password'])



            if username == v['username'] and password == v['password']:
                session['logged_in'] = True
                session['username'] = username
                #after login u go this page
                return redirect(url_for('afterstafflogin'))
            else:
                error = 'Invalid login'
                flash(error, 'danger')
                return render_template('login.html', form=form)
    else:
        return render_template('login.html', form = form)

        # if username == '0000' and password == 'pass' or username == '1111' and password =='p':
        #     # print('pass')
        #     return render_template('afterstafflogin.html')

    return render_template('login.html', form=form)



# @app.route('/login/', methods=['GET','POST'])
# def do_admin_login():
#     form = LoginForm(request.form)
#     if request.method == 'POST' and form.validate():
#         # request.form['password'] == 'password123' and request.form['username'] == 'ayuyus'
#
#            # session['logged_in'] = True
#         return redirect(url_for('index'))
#
#             # flash('wrong password!')
#     return render_template('login.html', form = form)

            # def home():
            #     if not session.get('logged_in'):
            #         return render_template('login.html')
            #     else:
            #         return render_template('index.html')

# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     error = None

    # if request.method == 'POST':
    #     file = open("loginfile.txt", "r")
    #     for line in file:
    #         field = line.split(':')
    #         u = field[0]
    #         p = field[1]
    #     if request.form['username'] != u or request.form['password'] != 'admin':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return redirect(url_for('index'))
    # return render_template('login.html', error=error)

# def logIn():
#     cre = {}
#     with open("loginfile.txt","r") as file:
#         for line in file:
#             user, pwd = line.strip().split(':')
#             cre[user] = pwd
#             if cre[user] == pwd:
#                 return render_template("/index/")
#             else:
#                 print("Try again")
#                 return render_template("login.html")
    # file = open("loginfile.txt","r")
    # for line in file:
    #     field = line.split(":")
    #     u = field[0]
    #     p = field[1]
    #     if u != name:
    #         print("Wrong Username")
    #     elif p != passw:
    #         print("Wrong password")
    #     else:
    #         print(name,passw)
    # pass


if __name__ == '__main__':
    app.secret_key = '123'
    app.run(debug = True, port = '80')
