# Panjiva Email Blaster

This tool automates the process of cleaning, verifying, and sending emails using data extracted from Panjiva.

## Requirements

- Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
- Outlook desktop application.

## Getting Started

1. **Clone the Repository:**
   - Open PowerShell. You can do this by pressing `Win + X` and selecting "Windows PowerShell" or "PowerShell" from the menu.
   - Navigate to the directory where you want to clone the repository:
     ```powershell
     cd /path/to/desired/directory
     ```
   - Run the following command to clone the repository to your local machine:
     ```powershell
     git clone https://github.com/sebas-masia/emailBlasters.git
     ```

2. **Install Dependencies:**
   - Navigate to the cloned repository folder:
     ```powershell
     cd emailBlasters
     ```
   - Install the required Python packages by running:
     ```powershell
     pip install -r requirements.txt
     ```

3. **Prepare Data:**
   - Save your input CSV file with the name `input_data.csv` in the `panjiva_data` folder.

4. **Run the Script:**
   - Make sure the Outlook desktop application is open and running.
   - Run the following command to execute the main script:
     ```powershell
     python main_script.py
     ```
   - This will start the automated process of cleaning, verifying, and sending emails.

5. **Check Results:**
   - After the process completes, ensure that only `input_data.csv` and `top_img.png` remain in the `panjiva_data` folder.
   - Confirm that `input_data.csv` is not in the generated `processed` folder.

## Notes

- If you encounter any issues, please refer to the [GitHub Issues](https://github.com/sebas-masia/emailBlasters/issues) or [contact support](mailto:sebastianmasia@gmail.com).
- No GitHub account is required to clone the repository.