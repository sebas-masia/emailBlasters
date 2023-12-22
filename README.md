# Panjiva Email Blaster

This tool automates the process of cleaning, verifying, and sending emails using data extracted from Panjiva.

## Requirements

- [Python](https://www.python.org/downloads/) installed on your computer.
- Outlook desktop application.

## Getting Started

1. **Install Python:**
   - If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).
   - Make sure to check the option to add Python to your PATH during installation.

2. **Open a Command Terminal:**
   - On Windows, you can open a command terminal by pressing `Win + R`, typing `cmd`, and pressing Enter.
   - Alternatively, open the Start menu, search for "Command Prompt," and click on it.

3. **Install Dependencies:**
   - Navigate to the folder where you extracted the tool. For example, if you extracted it to the Downloads folder:
     ```
     cd Downloads\emailBlasters
     ```
   - Install required Python packages:
     ```
     pip install pandas
     pip install -r requirements.txt
     ```

4. **Prepare Data:**
   - Save your input CSV file with the name `input_data.csv` in the `panjiva_data` folder.

5. **Run the Script:**
   - Ensure that the Outlook desktop application is open and running.
   - Run the following command in the terminal:
     ```
     python main_script.py
     ```
   - This will start the automated process of cleaning, verifying, and sending emails.

6. **Check Results:**
   - After the process completes, ensure that only `input_data.csv` and `top_img.png` remain in the `panjiva_data` folder.
   - Confirm that `input_data.csv` is not in the generated `processed` folder.

## Notes

- If you encounter any issues, please refer to the [GitHub Issues](https://github.com/sebas-masia/emailBlasters/issues) or [contact support](mailto:sebastianmasia@gmail.com).
