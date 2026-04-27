from pathlib import Path

def scan_files(directory):
    return [f for f in Path(directory).rglob("*") if f.is_file() and not f.name.endswith(".locked")]