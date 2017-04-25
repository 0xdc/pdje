from django.test import TestCase

# Create your tests here.
from passlib.hash import sha512_crypt

from .models import *

class UserTestCase(TestCase):
    def test_password_gets_hashed(self):
        user = User()

        user.name = "valid@email.address"
        password = "un-crypted password"
        user.password = password

        user.save()

        self.assertTrue(sha512_crypt.identify(user.password))
        self.assertTrue(sha512_crypt.verify(password, user.password))

    def test_password_entered_hashed(self):
        user = User()
        user.name = "valid@email.address"

        password = "un-crypted password"

        user.password = sha512_crypt.hash(password)
        before = user.password

        user.save()

        self.assertEquals(before, user.password)