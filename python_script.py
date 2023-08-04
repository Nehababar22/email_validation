import re
import csv
from validate_email_address import validate_email


def validate_email(email):
    """
    Validates the format of an email address using a regular expression pattern.
         
    Returns:
        bool: True if the email address has a valid format, False otherwise.

    """
    pattern = r"^[a-zA-Z][a-zA-Z0-9._-]{1,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
    
    # re.match() to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


def main():
    """
    Read a CSV file containing email addresses, validate them, and write the results to another CSV file.
    """
    csv_file = input("Please Enter CSV file name: ")
    input_csv = f'{csv_file}' 
    output_csv = 'output.csv'
    email_status = []

    print("Processing over emails...\n")

    # Open and Read emails from the CSV file
    with open(input_csv, 'r') as file:
        reader = csv.DictReader(file)

        print("Email\t\tStatus")

        for row in reader:
            email = row['email_id']
            status = 'Verified' if validate_email(email) else 'Not Verified'
            
            verified_status = status if status == 'Verified' else ''
            not_verified_status = status if status == 'Not Verified' else ''
            email_status.append({'email_id': email, 'Verified emails': verified_status, 'Not verified emails': not_verified_status})
            
            print(f"{email}\t{status}")


    with open(output_csv, 'w', newline='') as file:
        fieldnames = ['email_id', 'Verified emails', 'Not verified emails']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(email_status)


if __name__ == "__main__":
    main()
    
