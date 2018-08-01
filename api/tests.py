from __future__ import unicode_literals

import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from api.models import Occurence
from api.serializers import OccurenceSerializer
from api.views import OccurenceViewSet

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_occurence(author="", description="", position="", category="", status=""):
        if author != "" and description != "" and position != "" and category != "" and status != "":
            Occurence.objects.create(
                author=author,
                description=description,
                position=position,
                category=category,
                status=status
            )

    def setUp(self):
        self.create_occurence("Admin", "Occurence description", "POINT(12.12222 2.123)", "CONSTRUCTION", "Solved")
        self.create_occurence("Pedro", "Occurence description", "POINT(-2.6455652 3.7869)", "WEATHER_CONDITION", "To_be_validated")
        self.create_occurence("João", "Occurence description", "POINT(56.1232987 6.1123878)", "INCIDENT", "To_be_validated")
        self.create_occurence("Admin", "Occurence description", "POINT(-2.1287 56.1123568)", "CONSTRUCTION", "Validated")


class GetAllOccurencesTest(BaseViewTest):

    def test_get_all_occurences(self):
        """
        This tests if the occurences that were created in the setup
        are fetched when we make a GET request to our endpoint
        """
        response = self.client.get(
            reverse("occurence-list")
        )

        expected = Occurence.objects.all()
        serialized = OccurenceSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetOccurenceById(BaseViewTest):

    def test_get_occurence_by_id(self):
        """
        This tests if the occurence that we created in the setup
        is fetched when we make a GET request using the ID as a Uri param
        """
        occurence = Occurence.objects.get(author="Pedro")
        response = self.client.get(
            reverse("occurence-detail", args=[occurence.id])
        )

        expected = Occurence.objects.get(id=occurence.id)
        serialized = OccurenceSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_occurence_by_id(self):
        """
        This tests if when we make a GET request using an a Uri param
        an ID that doesn't exist we get a response code 404.
        """
        response = self.client.get(
            reverse('occurence-detail', args=[1012]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateOccurenceById(BaseViewTest):

    def test_update_occurence_by_id(self):
        """
        This tests if the occurence is updated when making a PATCH request
        """
        occurence = Occurence.objects.get(author="Pedro")
        payload = {
            "status": "Validated",
            "category": "INCIDENT"
        }
        response = self.client.patch(
            reverse("occurence-detail", args=[occurence.id]),
            data=json.dumps(payload),
            content_type='application/json'
        )

        expected = Occurence.objects.get(id=occurence.id)
        self.assertEqual('INCIDENT', expected.category)
        self.assertEqual('Validated', expected.status)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_occurence_by_id(self):
        """
        This tests if when we make a PATCH request with invalid payload
        we receive response code 400
        """
        occurence = Occurence.objects.get(author="Pedro")
        payload = {
            "status": 2
        }
        response = self.client.patch(
            reverse("occurence-detail", args=[occurence.id]),
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteOccurenceById(BaseViewTest):

    def test_delete_valid_occurence(self):
        """
        This tests if the occurence is delete when making a DELETE request
        """
        occurence = Occurence.objects.get(author="Pedro")
        response = self.client.delete(
            reverse("occurence-detail", args=[occurence.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_occurence(self):
        """
        This tests if when we make a DELETE request for a non existent occurence
        we receive response code 404
        """
        response = self.client.delete(
            reverse("occurence-detail", args=[1231])
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
