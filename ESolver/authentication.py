from ESolver import app 

@app.route('/register',methods=['GET','POST'])
def register():
    return 'register'

@app.route('/login',methods=['GET','POST'])
def login():
    return 'login'


@app.route('/logout',methods=['GET','POST'])
def logout():
    return 'logout'

