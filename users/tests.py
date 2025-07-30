from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from core.tests import TestDataMixin

from .forms import LunUserForm
from .models import LunUser, RieltorWorkShedule


class UserModelTest(TestDataMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.profile_view_url = reverse(
            "users:profile", kwargs={"profile": self.user.username}
        )

    def test_user_model(self):
        self.assertEqual(self.user.first_name, "Name")
        self.assertEqual(self.user.last_name, "Surname")
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.bio, "My bio")
        self.assertEqual(self.user.birth_date, "2024-03-12")
        self.assertTrue(self.user.check_password("testpassword123"))

    def test_profile_page_get(self):
        self.client.force_login(self.user)
        response = self.client.get(self.profile_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/user_details.html")

        self.assertEqual(self.newbuilding_info.offer, self.newbuilding)
        self.assertEqual(self.newbuilding_info.apartament_type, "1-room")
        self.assertEqual(self.newbuilding_info.state, "Builded")
        self.assertEqual(self.newbuilding_info.price_per_sqrm, 11000)
        self.assertEqual(self.newbuilding_info.area, 22.2)
        self.assertEqual(self.newbuilding_info.solded, False)

        self.assertIsInstance(response.context["user_form"], LunUserForm)

    def test_update_profile_post(self):
        self.client.force_login(self.user)

        data = {
            "first_name": "Test",
            "last_name": "Test",
            "bio": "Test",
            "birth_date": "2022-09-09",
        }

        response = self.client.post(self.profile_view_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("users:profile", kwargs={"profile": self.user.username})
        )

        updated_profile = LunUser.objects.get(username=self.user.username)

        self.assertEqual(updated_profile.first_name, "Test")
        self.assertEqual(updated_profile.last_name, "Test")
        self.assertEqual(updated_profile.bio, "Test")
        self.assertEqual(updated_profile.birth_date.strftime("%Y-%m-%d"), "2022-09-09")
