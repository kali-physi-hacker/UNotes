from django.test import TestCase

from notes.serializers import NoteSerializer
from notes.models import Note


class NoteSerializerTest(TestCase):
    def setUp(self):
        self.note_data = {"title": "1st Church Service In March", "content": "Holiness is staying away from porn"}

    def test_validation_success(self):
        """
		Tests that serializer.is_valid() is True if required fields and 
		serializer.save() --> Saves note
		returns:
		"""
        serializer = NoteSerializer(data=self.note_data)

        self.assertTrue(serializer.is_valid())
        serializer_note = serializer.save()
        for field in self.note_data:
            self.assertEqual(eval(f"serializer_note.{field}"), self.note_data.get(field))

        self.assertTrue(hasattr(serializer_note, "date_created"))

        # Assert For model level
        model_note = Note.objects.first()
        for field in self.note_data:
            self.assertEqual(eval(f"model_note.{field}"), self.note_data.get(field))

        self.assertEqual(serializer_note, model_note)

    def test_validation_failure(self):
        """
		Tests thata serializer.is_valid() if missing fields
		returns:
		"""
        # missing title
        data = self.note_data.copy()
        del data["title"]

        serializer = NoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(AssertionError):
            serializer.save()

        self.assertEqual(Note.objects.count(), 0)

        data = self.note_data.copy()
        del data["content"]

        serializer = NoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(AssertionError):
            serializer.save()

        self.assertEqual(Note.objects.count(), 0)
