# Automated Whatsapp Messages Python Script

This is a simple script which sends multiple whatsapp messages using python script. This is used for educational purpose only. Please don't ruin anyone's phone to sending multiple messages.

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed.
* Python 3.8: Download it from https://www.python.org/downloads
* Pyautogui: Run in command prompt pip install pyautogui

## Approach
* First need to clone this respiratory.
* Run python script script.py using py script.py in terminal.
* The script will asks you to enter number of messages and message content in terminal, after entered both information successfully you keep cursor in message bar in weh Whatsapp application to whom you want to send message.
* The script will sleeps for 3 seconds and then begin to send messages continuously untill and unless messages not sent all.

Note: Just use for fun

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
Note: The script may not work in case if the HTML of web WhatsApp is changed.
