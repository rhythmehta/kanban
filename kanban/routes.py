from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from kanban import app, db, bcrypt
from kanban.objects import Todo, User
from kanban.forms import register_form, login_form

# main kanban board page
@app.route("/", methods=['POST','GET'])#url
@login_required
def home():
    todo = Todo.query.filter_by(inprogress=False,completed=False, user_id=current_user.id).all()
    inprogress = Todo.query.filter_by(inprogress=True,completed=False, user_id=current_user.id).all()
    completed = Todo.query.filter_by(inprogress=True,completed=True, user_id=current_user.id).all()
    return render_template('home.html',todos=todo,dos=inprogress,dones=completed)

# adding new tasks
@app.route("/add",methods=['POST','GET'])#url
@login_required
def add_todo():
    title = request.form['title']
    desc = request.form['description']
    due = request.form['deadline']

    # check for non-empty input
    if title != '' and desc != '' and due != '':
        todo = Todo(title=title,desc=desc,due=datetime.strptime(due,'%Y-%m-%d'),user=current_user)
        db.session.add(todo)
        db.session.commit()
        flash(f'New task added: {todo.title}')
    else: flash(f"Invalid input")
    return redirect(url_for('home'))

# move task to To-Do
@app.route("/todo/<int:todo_id>")#url
def todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.inprogress = False
    todo.completed = False
    db.session.commit()
    flash(f"Task moved back to To-Do: {todo.title}")
    return redirect(url_for('home'))

# move task to In progress
@app.route("/do/<int:todo_id>")#url
def inprogress(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.inprogress = True
    todo.completed = False
    db.session.commit()
    flash(f"Task in progress: {todo.title}")
    return redirect(url_for('home'))

# mark task as completed
@app.route("/done/<int:todo_id>")#url
def completed(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.inprogress = True
    todo.completed = True
    db.session.commit()
    flash(f"Nice, task completed: {todo.title}")
    return redirect(url_for('home'))

# delete task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash(f"Deleted task: {todo.title}")
    return redirect(url_for('home'))

# new account creation
@app.route("/register",methods=['GET','POST'])
def register():
    form = register_form()
    if form.validate_on_submit():
        # storing hashed password value
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # update db
        db.session.add(user)
        db.session.commit()
        # alert
        flash(
            f'Your account has been created, {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

# login
@app.route("/login",methods=['GET','POST'])
def login():
    # check authentication
    if current_user.is_authenticated: return redirect(url_for('home'))
    form = login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # hashed password check
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else: flash(f'Please login again!')
    return render_template('login.html', title="Login", form=form)

# logout user
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))