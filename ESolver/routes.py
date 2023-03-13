from ESolver import app
from flask import render_template,request,flash


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/linear',methods=['GET','POST'])
def linear():
    if request.method == 'POST':
        flash(f'You have selected {request.form.get("num_of_equations")}','success')
        print(request.form.get('num_of_equations'))

    return render_template('linear.html',equation_name="Abonea_Linear")

@app.route('/nonlinear',methods=['GET','POST'])
def nonlinear():
    return render_template('nonlinear.html')


@app.route('/linear/<int:num>',methods=['GET','POST'])
def linear_dunamic(num):
    return render_template('linear.html',equation_name="Abonea_Linear",num=num, items=[1,23,5,4])