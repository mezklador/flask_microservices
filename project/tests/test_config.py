# project/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from project import app


class TestDevConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevConfig')
        return app

    def test_app_is_dev(self):
        self.assertTrue(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://me:me@localhost:5432/users_dev'        
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://me:me@localhost:5432/users_test'
        )


class TestProdConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProdConfig')
        return app

    def test_app_is_prod(self):
        self.assertTrue(app.config['SECRET_KEY'] is 'my_precious')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
