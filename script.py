import pyautogui
import time

number_of_messages = int(input('Enter number of messages: '))
message_content = input('Enter message content: ')

time.sleep(3)

for num in range(number_of_messages):
    pyautogui.write(message_content)
    pyautogui.press('enter')

print('Script executed successfully')
