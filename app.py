from flask import Flask, render_template,request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def loginpage():
    return render_template('loginpage.html')

@app.route('/dashboard')
def manager():
    return render_template('manager.html')

@app.route('/dashboard1')
def employee():
    return render_template('employee.html')

@app.route('/addemployee')
def add_employee():
    return render_template('addemployee.html')

@app.route('/project_dashboard')
def project_dashboard():
    return render_template('project_dashboard.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
