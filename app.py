from flask import Flask , render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy 


app = Flask (__name__ ) 


app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Patient(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    PatientNames = db.Column(db.String(200))
    DoctorNames = db.Column(db.String(200))
    Age = db.Column(db.String(20))
    Gender = db.Column(db.String(20))
    Test = db.Column(db.String(200))
    Result = db.Column(db.String(250))
    MedicalImaging = db.Column(db.String(200))

    

@app.route('/allpatient',methods=['GET','POST'])
def get():
     if request.method == "GET":
        patients = Patient.query.all()
        patient = Patient(PatientNames='',DoctorNames='',Age='',Gender='',Test='',Result='',MedicalImaging='')
        pagename ='allpatient'
        
        return render_template('allpatient.html',pagename=pagename,patients=patients,patient=patient)
     else:
         PatientNames = request.form['PatientNames']
         DoctorNames = request.form['DoctorNames']
         Age = request.form['Age']
         Gender = request.form['Gender']
         Test = request.form['Test']
         Result = request.form['Result']
         MedicalImaging = request.form['MedicalImaging']
        
         patient = Patient(PatientNames= PatientNames,DoctorNames=DoctorNames,Age=Age,Gender=Gender,Test=Test,Result=Result,MedicalImaging=MedicalImaging)
         db.session.add(patient)
         db.session.commit()
         return redirect('/allpatient')
   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/allpatient')
def allpatient():
    return render_template('allpatient.html')

@app.route('/update')
def update():
    return render_template('update.html')
    

if __name__ == '__main__' :
    app.run(debug=True)