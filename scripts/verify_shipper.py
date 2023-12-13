import requests
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor

def verify_email(email, hunter_api_key):
    # Hunter.io API endpoint for email verification
    endpoint = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={hunter_api_key}"

    try:
        # Make the API request
        response = requests.get(endpoint)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            # Extract relevant information from the API response
            result = data.get('data', {})

            # Return the verification result
            return {
                'email': email,
                'result': result.get('result', ''),
                'score': result.get('score', 0),
            }

        else:
            # Handle API request failure
            print(f"Failed to verify email {email}. Error: {data.get('errors', '')}")

    except Exception as e:
        # Handle general exception
        print(f"Error verifying email {email}: {str(e)}")

    # Return None if verification fails
    return None

def verify_emails(input_file, hunter_api_key, concurrency=5):
    # Read the cleaned data into a pandas DataFrame
    cleaned_data = pd.read_csv(input_file)

    # Create an empty list to store verification results
    verification_results = []

    def verify_wrapper(email):
        return verify_email(email, hunter_api_key)
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        # Use concurrent.futures to parallelize the verification process
        futures = [executor.submit(verify_wrapper, email) for email in cleaned_data['Shipper Email 1']]

        for future in futures:
            result = future.result()
            if result:
                verification_results.append(result)

    # Get the absolute path of the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine the script directory with '..', 'panjiva_data', and 'verification_results.csv'
    output_file = os.path.join(script_dir, '..', 'panjiva_data', 'verification_results.csv')
    
    # Create a DataFrame from the verification results
    verification_df = pd.DataFrame(verification_results)

    # Save the verification results to a CSV file
    verification_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Specify the input file and Hunter.io API key
    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'panjiva_data', "cleaned_data.csv")  # Update with the actual path
    hunter_api_key = "b9889a5223c0a400da02ac76a26c3ffdd00b97d5"  # Replace with your actual Hunter.io API key

    # Perform email verification
    verify_emails(input_file, hunter_api_key)
