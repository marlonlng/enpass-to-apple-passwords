# Enpass JSON to Apple Passwords Converter

This is a simple Python script that converts an **Enpass** password manager JSON export to a CSV file that can be imported into the **Apple Passwords** app.

## Features

-   Extracts key information (title, username, password, URL, notes, OTP) from the Enpass JSON file.
-   Automatically uses the `email` field if the `username` is missing.
-   Ensures proper handling of passwords that contain commas by quoting fields.

## Requirements

-   Python 3.x

## Usage

1. Export your data from Enpass as a JSON file.
2. Paste the exported JSON file into the project folder and rename it to `enpass_export.json`.
3. Run the following command to convert the JSON file to CSV.

### Command

```bash
python3 convert.py
```
