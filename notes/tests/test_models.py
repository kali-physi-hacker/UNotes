from django.test import TestCase
from django.db import IntegrityError

from notes.models import Note


class NoteTest(TestCase):
	def setUp(self):
		self.note_data = {
			"title": "Sunday Church",
			"content": "Today's Service is learning to pray"
		}

	def test_model_creation(self):
		"""
		Tests that Note instance is created when required fields are passed
		returns:
		"""
		note = Note.objects.create(**self.note_data)
		for field in self.note_data:
			self.assertEqual(eval(f"note.{field}"), self.note_data.get(field))
		
		self.assertTrue(hasattr(note, "date_created"))
		self.assertEqual(Note.objects.count(), 1)

	def test_model_creation_fails_missing_fields(self):
		"""
		Tests that Note can not be created without a title
		returns:
		"""
		# Missing title
		data = self.note_data.copy()
		del data["title"]
		
		with self.assertRaises(IntegrityError):
			Note.objects.create(**data)
		
		self.assertEqual(Note.objects.count(), 0)


		# Missing content
		data = self.note_data.copy()
		del data["content"]

		with self.assertRaises(IntegrityError):
			Note.objects.create(**data)

		self.assertEqual(Note.objects.count(), 0)
