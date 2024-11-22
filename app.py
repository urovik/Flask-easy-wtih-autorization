from flask import Flask,request,render_template
from database.db import create_user,get_all,get_name,del_all,db
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello world!"

@app.route('/user/<username>')
def user_profile(username):
    return f"Это профиль пользователя {username}"
#рассмотрим простейший пример обработки формы авторизации. 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        create_user(db,login=username,password=password)
        # проверка логина и пароля
        return "Вы зарегистрированы солнце"
    else:
        return render_template('login.html')
    
@app.route('/hello/<username>')
def index(username):
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 12:
        greeting = f'Доброе утро{username}'
    elif now.hour >= 12 and now.hour < 18:
        greeting = f'Добрый день{username}'
    elif now.hour >= 18 and now.hour < 24:
        greeting = f'Добрый вечер{username}'
    else:
        greeting = f'Доброй ночи{username}'
    return render_template('index.html', greeting=greeting)

@app.route('/task')
def task():
    tasks =["Поесть","помыть кота","Протереть пол"]
    return render_template("task.html",tasks=tasks)



if __name__ =="__main__":
    app.run(debug=True)