from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import MySQLdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Contactus?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
db=SQLAlchemy(app)

class portfolio(db.Model):
        sno = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
        email = db.Column(db.String(50), nullable=False)
        phone = db.Column(db.String(12), nullable=False)
        message = db.Column(db.String(500), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/professional")
def professional():
    return render_template("professional.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'POST':
         name = request.form.get('name')
         email = request.form.get('email')
         phone = request.form.get('phone')
         message = request.form.get('message')
         new_portfolio = portfolio(name=name, email=email, phone=phone, message=message)
         db.session.add(new_portfolio)
         db.session.commit()
         return "Submit success"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)