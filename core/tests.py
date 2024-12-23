from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newbuilding.models import NewBuildings, NewBuildingsProjects


class TestDataMixin:
    def setUp(self):
        self.rieltor = get_user_model().objects.create_user(
            username="rieltor",
            password="testpassword123",
            is_rieltor=True,
        )
        self.user = get_user_model().objects.create_user(
            first_name="Name",
            last_name="Surname",
            username="testuser",
            bio="My bio",
            birth_date="2024-03-12",
            password="testpassword123",
        )
        self.newbuilding = NewBuildings.objects.create(
            title="Example",
            slug="example",
            bio="Example",
            location="Kyiv",
            district="Obolon",
            metro_station="Obolon",
            company_name="Example",
            company_web="https://test.com/",
            apartament_classes="Econom",
            floors_variables="1,3",
            ceiling_height=2.8,
            apartament_count=12,
            housing_condition="Without renovation",
            parking_places=12,
            rieltor=self.rieltor,
        )
        self.newbuilding_info = NewBuildingsProjects.objects.create(
            offer=self.newbuilding,
            apartament_type="1-room",
            state="Builded",
            price_per_sqrm=11000,
            area=22.2,
            solded=False,
        )


class HomePageTest(TestCase):
    def test_home_page_get_redirect(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
