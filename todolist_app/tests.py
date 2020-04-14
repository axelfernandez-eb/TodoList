from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from todolist_app.models import Priority, Todo


class TestDjango(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

    def test_login(self):
        response = self.client.post('/login/',{'username': 'testuser', 'password': '12345'},follow=True)
        self.assertRedirects(response, "/")

    def test_create_todo(self):
        self.client.login(username='testuser', password='12345')
        priority = Priority.objects.create(name='Low', orders=1)
        response = self.client.post('/create/',
                                    {'title': 'testing',
                                     'description': 'wrongpass',
                                     'done': True,
                                     'priority': priority.id,
                                     }, follow=True)
        self.assertRedirects(response, "/view/1")

    def test_edit_todo(self):
        self.client.login(username='testuser', password='12345')
        priority = Priority.objects.create(name='Low', orders=1)
        self.client.post('/create/',
                                    {'title': 'testing',
                                     'description': 'wrongpass',
                                     'done': True,
                                     'priority': priority.id,
                                     }, follow=True)
        todo_id = max(Todo.objects.all().values_list("id"))[0]
        self.client.post(f'/edit/{todo_id}',
                                    {'title': 'testing',
                                     'description': 'This is the correct!',
                                     'done': True,
                                     'priority': priority.id,
                                     }, follow=True)
        self.assertEqual(Todo.objects.get(id = todo_id).description, "This is the correct!")

