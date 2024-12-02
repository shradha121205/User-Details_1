import csv
from myapp.models import User

def import_to_db(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            print("CSV Headers:", reader.fieldnames)  # Debugging line
            for row in reader:
                print(row)  # Debugging line
                try:
                    User.objects.create(
                        user_id=int(row['user_id']),
                        name=row['name'],
                        nationality=row['nationality'],
                        city=row['city'],
                        latitude=float(row['latitude']),
                        longitude=float(row['longitude']),
                        gender=row['gender'],
                        ethnic_group=row['ethnic_group'],
                        age=row['age']
                        english_grade=row['english_grade']
                        math_grade=float(row['math_grade']),
                        science_grade=row['sicence_grade']
                        language_grade=float(row['language_grade']),
                        portfolio_rating=int(row['portfolio_rating']),
                        cover_letter_rating=int(row['cover_letter_rating']),
                        ref_letter_rating=int(row['ref_letter_rating']),
                    )
                except Exception as e:
                    print(f"Error creating user: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
