from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input('Please enter your username: ')

    if User.query.filter(User.username == username).count():
        print('This user already exists!')
        sys.exit(0)

    password1 = getpass('Please enter your password: ')
    password2 = getpass('Please repeat your password: ')
    if password1 != password2:
        print('Passwords don`t match!')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print(f'User with id {new_user.id} has been created')