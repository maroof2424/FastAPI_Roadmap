from fastapi import APIRouter, BackgroundTasks
import time

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

def send_email_background(email: str, message: str):
    time.sleep(3)  
    with open("sent_emails.log", "a") as f:
        f.write(f"Sent to {email}: {message}\n")


@router.post("/send-email/")
async def send_email(
    email: str,
    message: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email_background, email, message)
    return {"status": "Email is being sent in the background"}
