from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('joe', 'joe@daltons.com', 'joepassword')
        UserProfile.objects.create(
            user=user,
            bio="A salesman",
            phone="1234567890",
            birth_date="1981-12-03",
            gender="male"
        )

    def test_user_profile_str(self):
        user_profile = UserProfile.objects.get(user__username="Joe")
        self.assertEqual(str(user_profile), "joe")
