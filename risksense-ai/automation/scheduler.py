# scheduler.py
# Schedules and manages automation tasks
import time
from interfaces.cli import run_pipeline

if __name__ == "__main__":
    while True:
        run_pipeline()
        time.sleep(86400)  # run daily
# --- IGNORE ---
- --- IGNORE ---
- --- IGNORE ---
- --- IGNORE ---
