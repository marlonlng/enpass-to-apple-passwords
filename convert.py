import json
import csv

def extract_field(fields, field_type):
    # Extract a field value by type from the 'fields' list
    for field in fields:
        if field.get('type') == field_type:
            return field.get('value', '')
    return ''

def convert_enpass_json_to_csv(enpass_json_file, output_csv_file):
    # Open and load the Enpass JSON file
    with open(enpass_json_file, 'r', encoding='utf-8') as json_file:
        enpass_data = json.load(json_file)

    # Define the header for the CSV file
    csv_columns = ['Title', 'URL', 'Username', 'Password', 'Notes', 'OTPAuth']
    
    # Prepare the CSV file
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writeheader()

        # Iterate over each entry and write to CSV
        for item in enpass_data['items']:
            title = item.get('title', '')
            notes = item.get('note', '')
            fields = item.get('fields', [])

            username = extract_field(fields, 'username')
            password = extract_field(fields, 'password')
            url = extract_field(fields, 'url')
            otpauth = extract_field(fields, 'totp')

            # Fallback to email if username is empty
            if not username:
                username = extract_field(fields, 'email');

            writer.writerow({
                'Title': title,
                'URL': url,
                'Username': username,
                'Password': password,
                'Notes': notes,
                'OTPAuth': otpauth
            })

    print(f"Successfully converted {enpass_json_file} to {output_csv_file}.")

enpass_json_file = 'enpass_export.json'
output_csv_file = 'apple_passwords_import.csv'
convert_enpass_json_to_csv(enpass_json_file, output_csv_file)
