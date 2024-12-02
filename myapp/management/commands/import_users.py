import csv
from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = 'Imports user data from a CSV file into the User model'

    def add_arguments(self, parser):
        # Argument for CSV file path
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        # Get the CSV file path from the arguments
        csv_file = kwargs['csv_file']

        try:
            # Open the CSV file and read its contents
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Create or update the User record in the database
                    user_data = {
                        'user_id': row['user_id'],
                        'name': row['name'],
                        'nationality': row['nationality'],
                        'city': row['city'],
                        'latitude': row['latitude'],
                        'longitude': row['longitude'],
                        'gender': row['gender'],
                        'ethnic_group': row['ethnic_group'],
                        'math_grade': row['math_grade'],
                        'language_grade': row['language_grade'],
                        'portfolio_rating': row['portfolio_rating'],
                        'cover_letter_rating': row['cover_letter_rating'],
                        'ref_letter_rating': row['ref_letter_rating'],
                    }
                    
                    # Insert the record into the User table
                    user, created = User.objects.update_or_create(
                        user_id=row['user_id'], defaults=user_data
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Successfully added user {user.name}"))
                    else:
                        self.stdout.write(self.style.SUCCESS(f"Successfully updated user {user.name}"))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {csv_file}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
