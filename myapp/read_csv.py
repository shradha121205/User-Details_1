import csv

def read_csv(file_path):
    try:
        # Open the CSV file
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Use DictReader for named columns
            # Iterate through rows
            for row in reader:
                print(row)  # Print each row as a dictionary
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
if __name__ == "__main__":
    read_csv('C:\Users\shrad\OneDrive\Desktop\record\myapp\myapp\users\users.csv')  # Replace with the path to your file
