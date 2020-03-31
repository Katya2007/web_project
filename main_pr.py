#from flask_ngrok import run_with_ngrok
from flask_login import login_user, LoginManager, logout_user
from data.register import RegisterForm
from flask import Flask, render_template, redirect
from data import db_session
from data.users import Pupil
from data.jobs import Jobs
from data.login import LoginForm

app = Flask(__name__)
#run_with_ngrok(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

def main():
    db_session.global_init("db/group_B.sqlite")

    @login_manager.user_loader
    def load_pupil(pupil_id):
        session = db_session.create_session()
        return session.query(Pupil).get(pupil_id)
    
    @app.route('/vivod', methods=['GET', 'POST'])
    def vivod():
        session = db_session.create_session()         
        news = session.query(Pupil).all()
        return render_template("index.html", a = True, b = False, news=news)
        
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            session = db_session.create_session()             
            if session.query(Pupil).filter(Pupil.email == form.email.data).first():
                return render_template('register.html', a = True, b = False, title='Регистрация ученика', form=form, message="Такой ученик  уже зарегистрирован")
            pupil = Pupil(
                surname=form.surname.data,
                name=form.name.data,
                email=form.email.data,
                telephone=form.telephone.data,
                class_=form.class_.data,
                )
            pupil.set_password(form.email.data)
            session.add(pupil)
            session.commit()           
            return redirect('/')
        return render_template('register.html', a = True, b = False, title='Регистрация ученика', form=form)
        
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/index', methods=['GET', 'POST'])
    def index():
        session = db_session.create_session()
        names = session.query(Pupil)
        return render_template('base.html', a = False, b = True, names=names)
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect("/")
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            user = session.query(Pupil).filter(Pupil.email == form.email.data).first()
            if user and user.check_password(form.email.data):
                login_user(user)
                jobs = session.query(Jobs).all()
                return render_template("jobs.html", a = True, b = False, jobs=jobs)                
                #return redirect("/")
            return render_template('login.html', a = True, b = False,
                                   message="Такого почтового адреса не зарегистрировано",
                                   form=form)
        return render_template('login.html', a = True, b = False, title='Авторизация ученика', form=form)    
    
    app.run(port=8050, host='127.0.0.1')

    #app.run()
if __name__ == '__main__':
    main()
    
        
        
        
        
