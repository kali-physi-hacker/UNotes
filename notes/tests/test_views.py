from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from notes.models import Note


class NoteListingTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.note_data = {"title": "Holiness", "content": "Abstinence from pornography is one way to be holy"}

        self.field_required_msg = "This field is required."

    def test_creation_success(self):
        """
		Tests that notes creation succeeds if not missing required fields
		returns:
		"""
        response = self.client.post(reverse("notes_lyric"), data=self.note_data)
        self.assertEqual(response.status_code, 201)
        for field in self.note_data:
            self.assertEqual(eval(f"response.json().get(field)"), self.note_data.get(field))

        self.assertEqual(Note.objects.count(), 1)

        # Model level
        note = Note.objects.first()
        for field in self.note_data:
            self.assertEqual(eval(f"note.{field}"), self.note_data.get(field))
        self.assertIn(response.json(), "date_created")

    def test_creation_failure(self):
        """
		Tests that notes creation fails and returns error response if missing 
		required fields
		"""
        # Missing title
        data = self.note_date.copy()
        del data["title"]
        response = self.client.post(reverse("notes_lyric"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["errors"]["title"][0], self.field_required_msg)

        self.assertEqual(Note.objects.count(), 0)

        # Missing content
        data = self.note_data.copy()
        del data["content"]
        response = self.client.post(reverse("notes_lyric"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["errors"]["title"][0], self.field_required_msg)

        self.assertEqual(Note.objects.count(), 0)
