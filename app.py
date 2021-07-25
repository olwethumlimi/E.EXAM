from os import write
from flask import Flask,render_template,request,jsonify,redirect
import  secrets
from LogicTier import AppLoad, User,minior_event


load=AppLoad()
load.createDataBase()
load.createUsers()
load.createQuestionTable()
load.createResultsTable()
user=User()





app = Flask(__name__)
app.secret_key="123"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # cache clean up


@app.route("/updateSemester",methods=["post"])
def updateSemester():
    return  jsonify(user.UpdateSemester())
    

@app.route("/login",methods=["post"])
def Login():
    return  jsonify(user.Login())

@app.route("/register",methods=["post"])
def Register():
    return  jsonify(user.Register())

@app.route("/get-questions",methods=["post"])
def getQuestions():
    return  jsonify(user.getQuestions())



@app.route("/save-marks",methods=["post"])
def save_marks():
    return  jsonify(user.save_marks())



@app.route("/logout",methods=["get"])
def Logout():
    minior_event.clear_session()
    return   redirect("/") 

@app.route("/")
def index():
    if(minior_event.get_user_email_session()==None):
        return  render_template("index.html")
    return redirect("/home")

@app.route("/home")
def home():
    if(minior_event.get_user_email_session()==None):
        return  redirect("/") 

    courses=user.CourseNames()
    written=user.get_All_Written()
    check=user.check_written_compulsory
   
    return  render_template("home.html",data={"courses":courses,"written":written,"check":check})

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(e):
# defining function
  return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)