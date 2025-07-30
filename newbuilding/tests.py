from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from core.tests import TestDataMixin
from newbuilding.forms import NewBuildingsForm
from newbuilding.models import NewBuildings, NewBuildingsProjects


class NewBuildingsModelTest(TestDataMixin, TestCase):
    def test_newbuildings_model(self):
        self.assertEqual(self.newbuilding.title, "Example")
        self.assertEqual(self.newbuilding.bio, "Example")
        self.assertEqual(self.newbuilding.location, "Kyiv")
        self.assertEqual(self.newbuilding.district, "Obolon")
        self.assertEqual(self.newbuilding.metro_station, "Obolon")
        self.assertEqual(self.newbuilding.company_name, "Example")
        self.assertEqual(self.newbuilding.company_web, "https://test.com/")
        self.assertEqual(self.newbuilding.apartament_classes, "Econom")
        self.assertEqual(self.newbuilding.floors_variables, "1,3")
        self.assertEqual(self.newbuilding.ceiling_height, 2.8)
        self.assertEqual(self.newbuilding.apartament_count, 12)
        self.assertEqual(self.newbuilding.housing_condition, "Without renovation")
        self.assertEqual(self.newbuilding.parking_places, 12)
        self.assertEqual(self.newbuilding.rieltor, self.rieltor)

    def test_newbuildingsprojects_model(self):
        self.assertEqual(self.newbuilding_info.offer, self.newbuilding)
        self.assertEqual(self.newbuilding_info.apartament_type, "1-room")
        self.assertEqual(self.newbuilding_info.state, "Builded")
        self.assertEqual(self.newbuilding_info.price_per_sqrm, 11000)
        self.assertEqual(self.newbuilding_info.area, 22.2)
        self.assertEqual(self.newbuilding_info.solded, False)

    def test_newbuildings_model_str(self):
        self.assertEqual(str(self.newbuilding), "Example")

    def test_newbuildings_model_get_absolute_url(self):
        self.assertEqual(self.newbuilding.get_absolute_url(), "/newbuildings/example/")


class CreateNewBuildingsViewTest(TestDataMixin, TestCase):
    def setUp(self):
        super().setUp()
        NewBuildings.objects.all().delete()
        self.create_view_url = reverse("newbuilding:create")

    def test_create_newbuildings_view_get(self):
        self.client.force_login(self.rieltor)
        response = self.client.get(self.create_view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newbuildings/newbuildings_create.html")

    def test_create_newbuildings_view_post(self):
        self.client.force_login(self.rieltor)

        data = {
            "title": "Example",
            "bio": "Example",
            "location": "Kyiv",
            "district": "Obolon",
            "metro_station": "Obolon",
            "company_name": "Examle",
            "company_web": "https://test.com/",
            "apartament_classes": "Econom",
            "floors_variables": "1,3",
            "ceiling_height": 2.8,
            "apartament_count": 12,
            "housing_condition": "Without renovation",
            "parking_places": 12,
            "rieltor": self.rieltor,
        }

        response = self.client.post(self.create_view_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/newbuildings/example/")

    def test_create_newbuildings_view_post_invalid_data(self):
        self.client.force_login(self.rieltor)

        data = {}

        response = self.client.post(self.create_view_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newbuildings/newbuildings_create.html")


class DetailsNewBuildingsViewTest(TestDataMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.detail_newbuildings_view_url = reverse(
            "newbuilding:details", kwargs={"newbuilding_slug": self.newbuilding.slug}
        )

    def test_detail_newbuildings_view(self):
        response = self.client.get(self.detail_newbuildings_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newbuildings/newbuildings_details.html")
        self.assertEqual(response.context["project"], self.newbuilding)

    def test_detail_newbuildings_view_404(self):
        self.newbuilding.is_active = False
        self.newbuilding.save()

        response = self.client.get(self.detail_newbuildings_view_url)

        self.assertEqual(response.status_code, 404)

    def test_detail_newbuildings_view_forms(self):
        self.client.force_login(self.rieltor)
        response = self.client.get(self.detail_newbuildings_view_url)
        self.assertContains(response, "Example")

        self.assertIsInstance(response.context["newbuilding_form"], NewBuildingsForm)


class UpdateNewBuildingsViewTest(TestDataMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.update_newbuildings_view_url = reverse(
            "newbuilding:update", kwargs={"newbuilding_slug": self.newbuilding.slug}
        )

    def test_update_newbuildings_get(self):
        self.client.force_login(self.rieltor)
        response = self.client.get(self.update_newbuildings_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newbuildings/newbuildings_update.html")

    def test_update_newbuildings_post(self):
        self.client.force_login(self.rieltor)

        data = {
            "title": "Update title",
            "bio": "Update bio",
            "location": "Kyiv",
            "district": "Obolon",
            "metro_station": "Obolon",
            "company_name": "Examle",
            "company_web": "https://test.com/",
            "apartament_classes": "Econom",
            "floors_variables": "1,3",
            "ceiling_height": 2.8,
            "apartament_count": 12,
            "housing_condition": "Without renovation",
            "parking_places": 12,
            "rieltor": self.rieltor,
        }

        response = self.client.post(self.update_newbuildings_view_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "newbuilding:details",
                kwargs={"newbuilding_slug": self.newbuilding.slug},
            ),
        )
        update_newbuilding = NewBuildings.objects.get(pk=self.newbuilding.pk)
        self.assertEqual(update_newbuilding.title, "Update title")
        self.assertEqual(update_newbuilding.bio, "Update bio")
