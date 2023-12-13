import pandas as pd
import os

def cleanup_email(email):
    
    # Convert NaN to None
    if pd.isna(email):
        return None
    
    # Remove invalid characters
    invalid_chars = [';', ':', '/', '#', '(', ')', '<', '>', '\\', "'", '"', '=']
    for char in invalid_chars:
        email = str(email).replace(char, '')

    # Check if the value is NaN (float) or a string
    if isinstance(email, str):
        # Check if email starts with "em" and remove it
        if email.lower().startswith("em") or email.lower().startswith("te"):
            return email[2:]
        else:
            return email
    else:
        return email

def cleanup_contacts(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(input_file)

    # Display the first few rows of the original data
    print("Original Data:")
    print(data.head())

    # Apply the cleanup_email function to the 'Consignee Email 1' column
    data['Consignee Email 1'] = data["Consignee Email 1"].apply(cleanup_email) 

    # Select only the desired columns (Consignee name and Consignee email 1)
    cleaned_data = data[['Consignee Name', 'Consignee Email 1']]

    # Display the first few rows of the cleaned data
    print("\nCleaned Data:")
    print(cleaned_data.head())

    # Drop rows with missing values in either Consignee name or Consignee email 1
    cleaned_data = cleaned_data.dropna(subset=['Consignee Name', 'Consignee Email 1'])

    # Display the first few rows of the final cleaned data
    print("\nFinal Cleaned Data:")
    print(cleaned_data.head())

    # Save the cleaned data to a new CSV file
    cleaned_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Specify the input and output file names 
    input_file = "input_data.csv"
    output_file = 'cleaned_data.csv'

    # Construct the full path to the input file and output file
    input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'panjiva_data', input_file)
    output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'panjiva_data', output_file)

    # Perform the cleanup
    cleanup_contacts(input_file_path, output_file_path)