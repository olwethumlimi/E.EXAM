from DataTier import Connection
import re,random
from flask import session,request

from itertools import groupby
from operator import itemgetter

connect =Connection()

# this is saying return 10 questions
# and the test will be out of 10
all_test_marks=3

class AppLoad:
        def __init__(self) -> None:
            pass
        def createDataBase(self):
            db_name='e_exam'
            connect.createDatabase(f"create database if not exists {db_name}",(db_name))

        def createQuestionTable(self):
            t='''
                CREATE TABLE IF NOT EXISTS questions (
                    id INT AUTO_INCREMENT  PRIMARY KEY,
                    module_name VARCHAR(255) NOT NULL,
                    course_name VARCHAR(255) NOT NULL,
                    year VARCHAR(255) NOT NULL,
                     semester VARCHAR(20) NOT NULL,
                    answer TEXT NOT NULL,
                    choice TEXT NOT NULL,
                    question TEXT NOT NULL,
                    tier VARCHAR(255) NOT NULL
                   
                    
                );
            '''
            connect.createTable(t)
    
        def createResultsTable(self):
            t='''
                CREATE TABLE IF NOT EXISTS results (
                    id INT AUTO_INCREMENT  PRIMARY KEY,
                    email VARCHAR(255) NOT NULL,
                    module_name VARCHAR(255) NOT NULL,
                    semester VARCHAR(255) NOT NULL,
                    year VARCHAR(255) NOT NULL,
                    mark  INT,
                    type VARCHAR(255) NOT NULL,
                    test_date VARCHAR(255) NOT NULL
                   

                );
            '''
            connect.createTable(t)

        def createUsers(self):
            t='''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT  PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    year VARCHAR(255) NOT NULL,
                    course_name VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    semester VARCHAR(20) NOT NULL
                );
            '''

            connect.createTable(t)

#minor event contain the smallest feature of the app
class miniorEvent:
    def __init__(self) -> None:
        pass

    def getFormData(self): return request.get_json(force=True)
    
    def set_user_semester_session(self,value):
        session["semester"]=value
    
    def clear_session(self):
        session.clear()
    
    def get_user_semester_session(self):
        return session.get("semester",None)
    
    def set_user_email_session(self,value):
        session["email"]=value

    def get_user_email_session(self):
        return session.get("email",None)

    def set_user_year_session(self,value):
        session["year"]=value

    def get_user_year_session(self):
        return session.get("year",None)

    def set_user_courseName_session(self,value):
        session["course"]=value

    def get_user_courseName_session(self):
        return session.get("course",None)

    def today_s_date(self):
        import datetime 
        # using now() to get current time 
        current_time = datetime.datetime.now() 
        date=str(current_time.day)+"-"+str(current_time.month)+"-"+str(current_time.year)
        return date
            

minior_event=miniorEvent()

class User:
    def __init__(self) -> None:
        # this regex used to validate email
        self.email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # save all errors here
        self.error={}
        # this is the course name
        self.courseList=["it"]

    def _ValidateEmail(self,email):
        error=self.error
        email=str(email).lower().rstrip()

        if(len(email)==0):
            error["email"]="email is required"
            

        if(len(email)<=5):
            if("email" not in error):
                error["email"]="email is too shot"
                

        if(len(email)>70):
            if("email" not in error):
                error["email"]="email is too shot"
                

        if(not re.match(self.email_regex, email)):
            if("email" not in error):
                error["email"]="enter a valid email"
        if("email" not in error):
              return email
                         
    def _ValidatePassword(self,password):
        error=self.error
        password=str(password)

        if(" " in password):
            error["password"]="no whitespace required"
            

        if(len(password)==0):
            if("password" not in error):
                error["password"]="password required"
                

        if(len(password)<6):
            if("password" not in error):
                error["password"]="password is too short minimum is 6"
                

        if(len(password)>12):
            if("password" not in error):
                error["password"]="password is too long maximum is 12"
                

        if("password" not in error):
           return  password

    def _ValidateName(self,name):
        error=self.error
        raw_name=str(name).lower()
        name=str(name).lower().rstrip()

        if(len(name)<3):
            error["name"]="name is too short"
            
        if(name.isdigit()):
            if("name" not in error):
                error["name"]="enter a valid name"
                

        if(len(name)>40):
            if("name" not in error):
                error["name"]="name is too long"
                

        if("name" not in error):
             return raw_name
        
    def _ValidateCourseName(self,course):
        error=self.error
        course=str(course).lower()

        if(course=="select course"):
            error["course"]="select course"
        
        if(not (course in self.courseList)):
            error["course"]="select course"


        if("course" not in error):
             return course

    def _ValidateYear(self,year):
        error=self.error
        year=str(year).rstrip()
        if(year=="select year"):
            if("year" not in error):
                error["year"]="select year"
        if(not year.isdigit()):
            if("year" not in error):
                error["year"]="select a valid year"

        
        if("year" not in error):
                return year

    def _ValidateSemster(self,semester):
        error=self.error
        semester=str(semester).rstrip()
        if(semester=="select semester"):
                error["semester"]="select semester"
        if(not semester.isdigit()):
            if("semester" not in error):
                error["semester"]="select a valid semester"

        
        if("semester" not in error):
                return semester

    def Login(self):
        self.error={}
        # validate all the user input
        form=minior_event.getFormData()

        email=self._ValidateEmail(form["email"])
        password=self._ValidatePassword(form["password"])
        
        # check for errors after validating
        if(len(self.error)>0):
                self.error["error"]="error"
                return self.error
        # check the user account if exist or not  
        sql="SELECT * from users WHERE email=%s AND password=%s"
        results=connect.fetchOne(sql,(email,password))
        # if returns empty result then
        if(results=={}):
            return {"program":"account not found","error":"error"}

        # get the user year from the db
        year=results["year"]
        course=results["course_name"]
        # set the user session to be active
        minior_event.set_user_email_session(email)
        minior_event.set_user_year_session(year)
        minior_event.set_user_courseName_session(course)

        # if all success the return status    
        return {"status":"success"}

    def Register(self):
        self.error={}

        form=minior_event.getFormData()
        email=form["email"]
        name=form["name"]
        password=form["password"]
        course=form["course"]
        year=form["year"]
        semester=form["semester"]
       
        
         # validate all the user input
        email=self._ValidateEmail(email)
        password=self._ValidatePassword(password)
        course=self._ValidateCourseName(course)
        name=self._ValidateName(name)
        year=self._ValidateYear(year)
        semester=self._ValidateSemster(semester)
        
        
         # check for errors after validating
        if(len(self.error)>0):
                self.error["error"]="error"
                return self.error

         # check the user account if exist or not , if not the register
        sql="SELECT email from users WHERE email=%s AND password=%s"
        results=connect.fetchOne(sql,(email,password))

        # if the len of results is >0 then , the use account exist
        if(len(results)>0):
            return {"program":"account already exist , please login","error":"error"}
   
        # if all success the in insert
        sql="INSERT INTO users(name,course_name,email,password,year,semester) VALUES(%s,%s,%s,%s,%s,%s)"
        connect.insert(sql,(name,course,email,password,year,semester))

        # set the user session to be active
        minior_event.set_user_email_session(email)
        minior_event.set_user_year_session(year)
        minior_event.set_user_courseName_session(course)

        # if all success the return status    
        return {"status":"success"}

    def UpdateSemester(self):
        self.error={}
        form=minior_event.getFormData()
        email=minior_event.get_user_email_session()
        semester=form["semester"]
        year=form["year"]
        print(form)
        
        semester=self._ValidateSemster(semester)
        year=self._ValidateYear(year)

    
         # check for errors after validating
        if(len(self.error)>0):
                self.error["error"]="error"
                return self.error
       

        sql="UPDATE users SET semester=%s , year=%s WHERE email=%s"
        connect.update(sql,(semester,year,email))

        return {"status":"success"}

    def _semester_year(self):
        email=minior_event.get_user_email_session()
        sql="SELECT * from users WHERE email=%s"
        results=connect.fetchOne(sql,(email))
        return results["year"]

    #get the user current semesterr        
    def _semester_semester(self):
        email=minior_event.get_user_email_session()
        sql="SELECT * from users WHERE email=%s"
        results=connect.fetchOne(sql,(email))
        return results["semester"]
         
    # get the user course names
    def CourseNames(self):
        year=self._semester_year()
        semester=self._semester_semester()
        sql="SELECT DISTINCT module_name ,year,semester   FROM questions WHERE year=%s AND semester=%s"
        results=connect.fetchAll(sql,(year,semester))
        return results

    #get the user questions and randomize them
    def getQuestions(self):
        data=minior_event.getFormData()
        module_name=data["module_name"]
        semester=self._semester_semester()
        year =self._semester_year()
        
        checkCompulsory=self.check_written_compulsory(module_name)
        # get the condition and the current tier
        condition=checkCompulsory[0]
        tier=checkCompulsory[1]
                # we get the questions base on the user tier

        
        # not written the comp
        if(condition==False):
            sql=" SELECT  * FROM questions WHERE (year=%s AND semester=%s AND  module_name=%s) and (tier=%s OR tier=%s OR tier=%s)"
            results=connect.fetchAll(sql,(year,semester,module_name,"1","2","3"))

            if results==[]:
                 return results
            
            # we randomize the array
            random.shuffle(results)
            # here we check if results is more than the all_test_marks which is = to the score
            if(len(results)>all_test_marks):
                # and get the total number of questions
                res=results[:all_test_marks]
                return res
            return results
        else:
            sql=" SELECT  * FROM questions WHERE year=%s AND semester=%s AND  module_name=%s AND tier=%s"
            results=connect.fetchAll(sql,(year,semester,module_name,tier))
            if results==[]:
                 return results

            # we randomize the array
            random.shuffle(results)
             # here we check if results is more than the all_test_marks which is = to the score
            if(len(results)>all_test_marks):

                # and get the total number of questions
                res=results[:all_test_marks]
                return res

            return results

    def get_All_Written(self):
        email=minior_event.get_user_email_session()
        year=self._semester_year()
        semester=self._semester_semester()
        # check if written the compulsory
        sql=" SELECT DISTINCT *  FROM results WHERE  email=%s AND year=%s AND semester=%s "
        results=connect.fetchAll(sql,(email,year,semester))
        
        if(results==[]): return []
        # this sort the object by name like
        # coursename
                #items
                #items
        # coursename
                #items
                #items
        results=sorted(results,key=itemgetter("module_name"))
        arr=groupby(results,key=itemgetter("module_name"))

        obj=[]
        for k,v in arr:
            # we reverse the array so that we can display the latest
            latest=list(v)[::-1]
            obj.append([k,latest])

        return obj
    
    def check_written_compulsory(self,module_name):
        email=minior_event.get_user_email_session()

        sql="SELECT DISTINCT module_name ,mark FROM results WHERE  module_name=%s AND email=%s AND type=%s"
        results=connect.fetchOne(sql,(module_name,email,"compulsory"))
        # make the  compulsory for the first time
        if(results=={}):
            return [False,"compulsory"]
        else:
            email=minior_event.get_user_email_session()
            mark=results["mark"]

            # check the user qualify for the second tier
            sql2="SELECT * FROM `results` WHERE  mark>=50 AND mark<=74 AND type<>'compulsory' AND email=%s"
            tier2=len(connect.fetchAll(sql2,(email)))

            # check the user qualify for the third tier
            sql3="SELECT * FROM `results` WHERE  mark>74 AND type<>'compulsory' AND email=%s"
            tier3=len(connect.fetchAll(sql3,(email)))

            
            # the user did pass more than 5 test then we move to the next tier
            


            # user database rows marks not >=5  then use the marks to assign the tier
            
            if(tier3>=5):
                 return [True,"3"]
            elif mark>=75:
                return [True,"3"]
            elif(tier2>=5):
                 return [True,"2"]
            elif mark>=50 and mark<=74:
                 return [True,"2"]
            else:
                return [True,"1"]
   
    # calculate the user marks in percent
    def _calculatePercent(self,data,semester,year,module_name):
        # calulating marks
        score=0
        for key in data.keys():
            id=str(key)
            # get the user answer
            choosen=str(data[key]).lower()
            # get the selected question on the db
            sql=" SELECT answer FROM questions WHERE year=%s AND semester=%s AND  module_name=%s AND id=%s"
            results=connect.fetchOne(sql,(year,semester,module_name,id))
            # check if we have a question
            if results!=[]:
                # get the db answer
                answer=str(results["answer"]).lower()
                # check if this two answers match
                if(answer==choosen):
                    score=score+1
        # all test marks is variable that control the marks score
        return (score/all_test_marks)*100

    def save_marks(self):

        data=minior_event.getFormData()
        module_name=data["module_name"]
        semester=self._semester_semester()
        year =self._semester_year()
        email=minior_event.get_user_email_session()
        date_time=minior_event.today_s_date()
        # remove the module from the dictinary since i was using it to track the module
        #then we gonna be left with answers ids , to generate the score
        data.pop("module_name",None)

        # check if written the compulsory
        sql=" SELECT  * FROM results WHERE  module_name=%s AND email=%s AND type=%s"
        results=connect.fetchOne(sql,(module_name,email,"compulsory"))
        # make the  compulsory for the first time
        if(results=={}):
            # calulate ther user marks
            score=self._calculatePercent(data,semester,year,module_name)
            #add the type compulsory after writting the main test
            sql=" INSERT INTO results(email,module_name,type,semester,year,mark,test_date) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            connect.insert(sql,(email,module_name,"compulsory",semester,year,score,date_time))
            return {"status":"success"}

       
        # calulate ther user marks
        score=self._calculatePercent(data,semester,year,module_name)
         # if written the main test then we add type written for the other tests
        sql=" INSERT INTO results(email,module_name,type,semester,year,mark,test_date) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        connect.insert(sql,(email,module_name,"written",semester,year,score,date_time))
        

        return  {"status":"success"}
    
        
    
                





