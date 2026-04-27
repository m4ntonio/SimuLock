from pathlib import Path

FLAG = Path(".executado.flag")

def already_executed():
    return FLAG.exists()

def mark_executed():
    FLAG.write_text("executado")