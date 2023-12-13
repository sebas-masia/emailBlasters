import pandas as pd
import win32com.client
import os

# Function to send an HTML email
def send_html_email(subject, html_body, to_email, image_path):
    ol = win32com.client.Dispatch('Outlook.Application')
    olmailitem = 0x0
    newmail = ol.CreateItem(olmailitem)
    newmail.Subject = subject
    newmail.To = to_email

    # Set the HTML body
    newmail.HTMLBody = html_body

    # Attach the image with Content-ID (CID)
    attachment = newmail.Attachments.Add(image_path, 1, 0, "ROK_Lanes_Logo")
    image_cid = "ROK_Lanes_Logo"
    attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", image_cid)

    newmail.Send()

# Function to process each row of the DataFrame
def process_row(row, signature, image_path):
    # Check if the score is not equal to 0
    if row['score'] != 0:
        # Extract data from the DataFrame row
        subject = 'Solid as a ROK'
        body = """
        Hello<br><br>

        How are your shipments handled when they come into or leave the US? Are you in need of dependable shipping within North America?<br><br>

        My name is Key Klungland with ROK Lanes, we're a trucking 3PL. We offer services anywhere in the US or Canada, and we also handle cross-border shipments to/from Mexico. A full list of our services includes: drayage, transloading, warehousing, FTL, LTL, and we can also help with sourcing loading equipment for those more difficult shipments. Our best selling point is our service. Our drivers are vetted to ensure your shipment is handled correctly, and our communication is the very best. On top of that, we utilize a system that you can log into to track your shipment in real-time, as well as access documents (PODs, bills, etc.) whenever is convenient for you.<br><br>

        If you're interested in learning more about ROK Lanes, feel free to visit our website: www.roklanes.com<br><br>

        Thank you,<br><br>
        """

        # Construct the HTML body with the signature and image
        html_body = f"""
        <html>
        <body>
            <p>{body}</p>
            <img src= "cid:ROK_Lanes_Logo" alt='ROK Lanes Logo'>
            <p>{signature}</p>
        </body>
        </html>
        """

        # Send the HTML email
        send_html_email(subject, html_body, row['email'], image_path)
        print(f"Email sent to {row['email']}")

# Specify the file path with the correct directory structure
# file_path = 'C:\\Users\\RokLanes\\Documents\\projects\\emailBlasters\\panjiva_data\\verification_results.csv'
# image_path = 'C:\\Users\\RokLanes\\Documents\\projects\\emailBlasters\\panjiva_data\\top_sig.png'
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'panjiva_data', 'verification_results.csv')
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'panjiva_data', 'top_sig.png')

# Specify your email signature
email_signature = """
    <p><b>Sebastian Masiá</b></p>
    <p>Account Operations Specialist</p>
    <p>O: (877) 765-8720 x827</p>
    <p><a href="http://www.roklanes.com">www.roklanes.com</a></p>
    <p>1000 N. West ST STE 1200 / Wilmington, DE 19801.</p>
    <p style="font-style: italic; color: grey;">All services provided by ROK LANES hereunder are subject to the applicable terms and conditions at <a href="http://www.roklanes.com">www.roklanes.com</a> which are incorporated herein for all purposes unless otherwise agreed to in writing by the parties.</p>
"""

try:
    # Read the verifications_results.csv file into a DataFrame
    df = pd.read_csv(file_path)

    # Process each row in the DataFrame sequentially
    for _, row in df.iterrows():
        process_row(row, email_signature, image_path)

except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
