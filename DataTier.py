import pymysql.cursors

mydb =  pymysql.connect(
    host="localhost",
    user="root",
    password="",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = mydb.cursor()



class Connection:
    def __init__(self) -> None:
        self.mydb=mydb
        self.cursor=cursor

    def insert(self,sql,params=None):
        if(params==None):   
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql,params)
        self.mydb.commit()

    def createDatabase(self,sql,db_name):
        self.cursor.execute(sql)
        self.cursor.execute(f'use {db_name}')

    def createTable(self,sql):
        self.cursor.execute(sql)
       

    def update(self,sql,params=None):
        if(params==None):   
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql,params)
        self.mydb.commit()



    def fetchOne(self,sql,params=None):
        if(params==None):   
            self.cursor.execute(sql)
            res= self.cursor.fetchone()
            if res==None:
                return {}
            if res==():
                return {}
            if(len(res)==0):
                return {}
            return res
        else:
            self.cursor.execute(sql,params)
            res= self.cursor.fetchone()   
            if res==None:
                return {}
            if res==():
                return {}
            if(len(res)==0):
                return {}
            return res
        



    def fetchAll(self,sql,params=None):
        if(params==None):   
            self.cursor.execute(sql)
            res= self.cursor.fetchall()
            if res==None:
                return []
            if res==():
                return []
            if(len(res)==0):
                return []
            return res
        else:
            self.cursor.execute(sql,params)
            res= self.cursor.fetchall()
            if res==None:
                return []
            if res==():
                return []
            if(len(res)==0):
                return []
            return res
        


