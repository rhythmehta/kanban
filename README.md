# Kanban Board
###### To help you improve productivity, break down big tasks into smaller tractable components and visualize them on this project management tool. 

Launch App: https://cs162-kanban.herokuapp.com/

Keywords: Python, Flask, SQL, WTForms, HTML, CSS, bcrypt, Heroku;

Features:
- [x] Signup/Login with password encryption
- [x] Add Task (including Task Title, Task Description, Due Date)
- [x] Delete or Move Tasks in Kanban Board
- [x] Responsive web design, compatible with PC/Mobile

Features coming soon:
- [x] Forgot/Reset password
- [x] Create multiple kanban boards (for work, school, etc.)
- [x] and more... 

# Run locally
1. Clone repo
2. Load Terminal from root directory, and type following commands
3. Create and activate virtual environment
```console
name@Desktop/kanban ~ % python3 -m venv .venv
name@Desktop/kanban ~ % source .venv/bin/activate
```
4. Install dependencies
```console
(.venv) name@Desktop/kanban ~ % pip install -r requirements.txt
```
5. Launch app
```console
(.venv) name@Desktop/kanban ~ % flask run
```
6. Open http://127.0.0.1:5000/ in browser

# UI Screenshots

## Loaded Kanban Board
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/40776621/160268006-bc5396e3-51ff-467a-be3c-d474c85d7927.png">

## Empty Kanban Board
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/40776621/160267518-05dac883-7d3a-4353-938e-624fcb93e3a7.png">

# Features

## + Signup - Create a new account
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/40776621/160268291-0fdfc534-9ea0-4cbd-a761-b92cd4f9fa2e.png">

## + Login to existing account
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/40776621/160268282-4338dae8-14f5-47e2-b766-0b62d126ac9b.png">

## + Add New Task (Title + Description + Due Date)
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/40776621/160267551-9941551c-fd31-49e0-b1ea-70d305f3c288.png">

## + Hover on double-arrow symbol for options to move task to another column or delete
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/40776621/160267584-84d43ca8-01dd-424d-8af4-7d9a4c141342.png">

## + Hover over task title to read task description on a pop-up
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/40776621/160267649-f177d4b0-335c-4bd6-8bfd-97a5332a9993.png">

# SQL Database

## Users
![image](https://user-images.githubusercontent.com/40776621/161510739-004296f5-286a-4c93-957a-0bb261a68538.png)

## Tasks
![image](https://user-images.githubusercontent.com/40776621/161511442-260ef371-a8e2-4674-af36-595b50b7eb31.png)

# References
- Marcelomd. (2014). flask-wtf-login-example. Retreived from https://github.com/marcelomd/flask-wtf-login-example
- Pretty Printed YouTube Channel. (2017). "Creating a Todo List App With Flask and Flask-SQLAlchemy". Retreived from https://youtu.be/4kD-GRF5VPs and https://github.com/PrettyPrinted/youtube_video_code/tree/master/2017/09/27/Creating%20a%20Todo%20List%20App%20With%20Flask%20and%20Flask-SQLAlchemy
- Pretty Printed YouTube Channel. (2017). "Build a User Login System With Flask-Login, Flask-WTForms, Flask-Bootstrap, and Flask-SQLAlchemy". Retreived from https://youtu.be/8aTnmsDMldY and https://github.com/PrettyPrinted/youtube_video_code/tree/master/2017/09/27/Creating%20a%20Todo%20List%20App%20With%20Flask%20and%20Flask-SQLAlchemy
- Rithm School. Password Hashing with Bcrypt in Flask. Retreived from https://www.rithmschool.com/courses/intermediate-flask/hashing-passwords-flask
