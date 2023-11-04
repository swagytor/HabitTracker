from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email=input('email'),
            first_name=input('first_name'),
            last_name=input('last_name'),
            is_superuser=bool(input('is_superuser')),
            is_staff=bool(input('is_staff')),
            is_active=True
        )

        user.set_password('6002')
        user.save()