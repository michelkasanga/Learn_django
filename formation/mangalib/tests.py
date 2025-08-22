from django.test import TestCase

class MangalibTests(TestCase):

    def test_example(self):
        self.assertEqual(1 + 1, 2)
    
class AuthorModelTests(TestCase):

    def test_author_creation(self):
        from .models import Author
        author = Author.objects.create(name="Test Author")
        self.assertEqual(author.name, "Test Author")
