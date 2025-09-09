import pytest
from app import tasks
import asyncio

@pytest.mark.anyio
async def test_send_email_notification(capsys):
    await tasks.send_email_notification("test@example.com", "Hello World")
    captured = capsys.readouterr()
    assert "Sending email to test@example.com with message: Hello World" in captured.out
