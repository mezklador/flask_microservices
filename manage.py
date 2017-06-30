# manage.py


import coverage
import unittest

from flask_script import Manager
from faker import Faker

#from project import app, db
from project import create_app, db
from project.api.models import User


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*'
    ]
)

COV.start()

app = create_app()
manager = Manager(app)
fake = Faker()


@manager.command
def recreate_db():
    """Recreates a db"""
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def test():
    """Runs the tests without any code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def seed_db():
    """Seed the db with fake infos."""
    for _ in range(10):
        name = fake.first_name()
        email = f"{name}@{fake.free_email_domain()}"
        db.session.add(User(username=name, email=email))

    db.session.commit()
    print("Seeding db with fake data: done.")


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
