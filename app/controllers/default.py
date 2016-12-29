from flask import render_template, flash, url_for, redirect
from app import app, db, lm, mail
from flask_login import login_user,logout_user, login_required, current_user
from flask_mail import Message

from app.models.forms import LoginForm, RegisterForm, TwitForm
from app.models.tables import User, Follow, Post

@lm.user_loader
def user_loader(id):
    return User.query.get(id);

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,name=form.name.data,email=form.email.data)
        user.generate_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registered !!")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# @app.route("/d",methods=["GET","POST","DELETE"])
# def d():
#     for i in range(1,6):
#         u = Post.query.get(i)
#         db.session.delete(u)
#         db.session.commit()

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash("Login Valido")
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('dashboard'))
        else:
            flash("Login Inválido")

    elif form.errors:
        print(form.errors)
    return render_template('login.html',form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/dashboard", methods=["GET","POST"])
@login_required
def dashboard():
    form = TwitForm()
    if form.validate_on_submit():
        new_twit = Post(content=form.content.data,user_id=current_user.id)
        db.session.add(new_twit)
        db.session.commit()
    following = Follow.query.filter_by(follower_id=current_user.id).all()
    twits = []
    for follow in following:
        t = Post.query.filter_by(user_id=follow.user_id).all()
        twits.extend(t)

    my_t = Post.query.filter_by(user_id=current_user.id).all()
    twits.extend(my_t)

    return render_template('dashboard.html',twits=twits[::-1], form=form)

@app.route("/twitero/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    twits = Post.query.filter_by(user_id=user.id).all()
    if current_user.id!=user.id:
        following = Follow.query.filter_by(user_id=user.id, follower_id=current_user.id).first()
    else:
        following = None
    return render_template('profile.html',user=user,twits=twits[::-1],following=following)

@app.route("/follow/<int:id>")
@login_required
def follow(id):
    u = User.query.get(id)
    f = Follow(id,current_user.id)
    db.session.add(f)
    db.session.commit()

    msg = Message("New Follower!!", sender=app.config["MAIL_USERNAME"],recipients=[u.email])
    msg.body = "You have new follower: @{0}".format(current_user.username)
    mail.send(msg)

    return redirect(url_for('profile', username=u.username))


@app.route("/unfollow/<int:id>")
@login_required
def unfollow(id):
    u = User.query.get(id)
    f = Follow.query.filter_by(user_id=u.id,follower_id=current_user.id).first()
    db.session.delete(f)
    db.session.commit()
    return redirect(url_for('profile', username=u.username))