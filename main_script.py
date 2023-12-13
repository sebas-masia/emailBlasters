# main_script.py

import os
import subprocess
import pandas as pd
from shutil import move
import logging

# Configure logging to write to a file
logging.basicConfig(filename='app_log.txt', level=logging.DEBUG)

def get_data_type(csv_path):
    # Read the first row of the CSV to determine the data type
    df = pd.read_csv(csv_path, nrows=1)
    first_column_name = df.columns[0]

    # Check if the first column name contains "Consignee" or "Shipper"
    if "Consignee" in first_column_name:
        return "Consignee"
    elif "Shipper" in first_column_name:
        return "Shipper"
    else:
        logging.error(f"Unsupported data type: {first_column_name}")
        return None

def move_to_processed(csv_path):
    # Move the processed file to a 'processed' directory
    processed_folder = "processed"
    os.makedirs(processed_folder, exist_ok=True)
    move(csv_path, os.path.join(processed_folder, os.path.basename(csv_path)))

def clean_and_verify_data(input_data_folder, data_type):
    # Specify the cleaning and verifying scripts based on the data type
    if data_type == "Consignee":
        cleaning_script = "scripts/cleanup_consignee.py"
        verifying_script = "scripts/verify_consignee.py"
    elif data_type == "Shipper":
        cleaning_script = "scripts/cleanup_shipper.py"
        verifying_script = "scripts/verify_shipper.py"
    else:
        logging.error(f"Unsupported data type: {data_type}")
        return

    # Get the list of CSV files in the input data folder
    csv_files = [f for f in os.listdir(input_data_folder) if f.endswith(".csv")]

    for csv_file in csv_files:
        csv_path = os.path.join(input_data_folder, csv_file)
        
        # Check if the file is already processed
        if os.path.exists(os.path.join("processed", csv_file)):
            logging.info(f"Skipping already processed file: {csv_file}")
            continue

        logging.info(f"Cleaning {data_type} data from: {csv_file}")
        # Step 1: Clean the data
        cleaning_command = f"python {cleaning_script} --input-csv {csv_path}"
        subprocess.run(cleaning_command, shell=True)

        # Move the processed file to the 'processed' directory
        move_to_processed(csv_path)

        logging.info(f"Verifying {data_type} data from: {csv_file}")
        # Step 2: Verify the data
        verifying_command = f"python {verifying_script} --input-csv {csv_path}"
        subprocess.run(verifying_command, shell=True)

def send_emails(input_data_folder, email_script):
    logging.info("Sending emails")
    # Step 3: Send emails to the verified list
    email_command = f"python {email_script} --input-folder {input_data_folder}"
    subprocess.run(email_command, shell=True)

def main():
    logging.info("Application started")

    # Specify the input data folder
    input_data_folder = "panjiva_data"

    # Get the data type
    data_type = get_data_type(os.path.join(input_data_folder, os.listdir(input_data_folder)[0]))

    if data_type:
        # Run the centralized workflow
        clean_and_verify_data(input_data_folder, data_type)
        send_emails(input_data_folder, "scripts/email_script.py")
    else:
        logging.error("Unable to determine data type. Exiting.")

if __name__ == "__main__":
    main()
