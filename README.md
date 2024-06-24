# WhatsApp Message Automation Script

This script automates the process of sending a message to a list of phone numbers using WhatsApp Web. The script uses Selenium to control a Chrome browser and send messages.

## Prerequisites

- Python 3.10 and above
- Google Chrome browser
- ChromeDriver (managed by `webdriver-manager`)
- Selenium

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2.  **Install the required packages**:
    ```bash
	pip install -r requirements.txt

## Usage
1. **Prepare the Script**:
 -Ensure the app.py script is in the repository directory.
 -Modify the phone_numbers list in app.py if you need to add or change the phone numbers.

2. **Run the Script**:
   ```bash
   python3 app.py

3. **Scan the QR Code**:

 -The script will open WhatsApp Web in a new Chrome window.
 -Scan the QR code with your phone to log in to WhatsApp Web.

4 **Automation**:

After logging in, the script will automatically send the message "RejectFinanceBill2024" to each phone number in the list.
The script waits for 0.5 seconds between sending each message.
Customization
Message: You can change the message by modifying the message variable in app.py.
Delay: Adjust the delay between sending messages by modifying the time.sleep(0.5) line in the script.
Troubleshooting
Element Not Found: If the script encounters an error like no such element, it means it could not find the message input box. Ensure that the XPath used in the script matches the current structure of WhatsApp Web.
ChromeDriver Issues: Ensure that your Chrome browser and ChromeDriver are compatible. The script uses webdriver-manager to manage ChromeDriver versions automatically.
Disclaimer
This script is for educational purposes only. Automating actions on WhatsApp Web may violate WhatsApp's terms of service. Use this script responsibly and at your own risk.

License
This project is licensed under the MIT License.
