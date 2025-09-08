import time
from fastapi import BackgroundTasks

def send_email_notefication(email:str,message:str):
    time.sleep(2)
    print(f"Email sent to {email}: {message}")

    