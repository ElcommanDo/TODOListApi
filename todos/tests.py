from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoListTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Todo.objects.create(title='test', body='tets data')
    
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected = f'{todo.title}'
        self.assertEqual(expected, 'test')

    def test_body_contnet(self):
        todo = Todo.objects.get(id=1)
        expected = f'{todo.body}'
        self.assertEqual(expected, 'tets data')
    