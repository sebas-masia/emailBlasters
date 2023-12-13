# Panjiva Email Blaster

## Overview

Panjiva Email Blaster is a tool designed to clean, verify, and send emails to a list of contacts extracted from Panjiva. The application is packaged as a standalone executable, making it easy to use without requiring a Python installation.

## Features

- **Data Cleanup:** Remove invalid characters and prefixes from email addresses.
- **Email Verification:** Check the validity of emails using the Hunter.io API.
- **Email Sending:** Send HTML emails to verified contacts.

## Getting Started

### Prerequisites

- [Download the latest release](#) of Panjiva Email Blaster for your operating system.

### Installation

1. Extract the downloaded ZIP file.
2. Place your Panjiva dataset in the `panjiva_data` folder as `input_data.csv`.

## Usage

1. **Data Cleanup:**
   - Double-click the executable (`panjiva_email_blaster.exe` or equivalent) to run the cleanup process.
   - Review the cleaned data in the `panjiva_data` folder (`cleaned_data.csv`).

2. **Email Verification:**
   - Run the verification process by executing the corresponding executable.
   - View the verification results in the `panjiva_data` folder (`verification_results.csv`).

3. **Email Sending:**
   - Run the email sending process by executing the corresponding executable.
   - Check the console for progress and errors.

## Troubleshooting

- If you encounter issues, ensure that your Panjiva dataset is correctly named and placed in the `panjiva_data` folder.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to [Hunter.io](https://hunter.io/) for providing email verification services.

---

**Note:** Customize the download link in the "Prerequisites" section with the actual link to your release file.
