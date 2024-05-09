from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='Bravo', email='bravo@example.com', password='secret', age=33)
        user.save()
        self.stdout.write(f'{user}')