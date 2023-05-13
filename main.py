import requests
import subprocess
import time
import random

while(True):
    oiminion_request = requests.get('https://www.codewars.com/api/v1/users/oiminion')
    oiminion_values = oiminion_request.json()

    Cloverfieldo_request = requests.get('https://www.codewars.com/api/v1/users/Cloverfieldo')
    Cloverfieldo_values = Cloverfieldo_request.json()

    def sendmessage(message):
        subprocess.Popen(['notify-send', message])
        return

    if Cloverfieldo_values['honor'] <= oiminion_values['honor']:
        sendmessage("Oiminon has surpressed me")
    time.sleep(180)