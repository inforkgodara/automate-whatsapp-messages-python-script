# Automate Whatsapp Messages Python Script

This is a simple script that sends multiple WhatsApp messages using python script. This is used for educational purposes only. Please don't ruin anyone's phone by sending multiple messages.

## Demo
* Video clip on youtube of the script execution. https://youtu.be/tPm7Zvn4pFY

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed.
* Python 3.8: Download it from https://www.python.org/downloads
* Pyautogui: Run in command prompt pip install pyautogui

## Approach
* First need to clone this respiratory.
* Open web Whatsapp in any browser. link: https://web.whatsapp.com/
* Run python script script.py using py script.py in the terminal.
* The script will ask you to enter the number of messages and message content in the terminal, after entered both information successfully you keep the cursor in the message bar in the web Whatsapp application to whom you want to send the message.
* The script will sleep for 3 seconds and then begin to send messages continuously until and unless messages not send all.

Note: Please use just use for fun not to ruin anyone's phone.

## Code
```
import pyautogui
import time

number_of_messages = int(input('Enter number of messages: '))
message_content = input('Enter message content: ')

time.sleep(3)

for num in range(number_of_messages):
    pyautogui.write(message_content)
    pyautogui.press('enter')

print('Script executed successfully')
```

Video on youtube: https://youtu.be/tPm7Zvn4pFY
