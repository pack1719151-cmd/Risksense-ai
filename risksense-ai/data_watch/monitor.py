import os
import time
import logging

# monitor.py
# Monitors data sources for changes and updates
def monitor_directory(path, callback, interval=5):
    """
    Monitors the specified directory for file changes and calls the callback on change.

    Args:
        path (str): Directory path to monitor.
        callback (function): Function to call when a change is detected.
        interval (int): Time in seconds between checks.
    """
    logger = logging.getLogger(__name__)
    if not os.path.isdir(path):
        logger.error(f"Provided path '{path}' is not a valid directory.")
        raise ValueError(f"Provided path '{path}' is not a valid directory.")

    logger.info(f"Starting directory monitor on: {path} (interval: {interval}s)")
    previous_snapshot = set(os.listdir(path))
    try:
        while True:
            time.sleep(interval)
            current_snapshot = set(os.listdir(path))
            added = current_snapshot - previous_snapshot
            removed = previous_snapshot - current_snapshot
            if added or removed:
                logger.debug(f"Change detected. Added: {added}, Removed: {removed}")
                callback(added, removed)
            previous_snapshot = current_snapshot
    except KeyboardInterrupt:
        logger.info("Directory monitoring stopped by user.")

def on_change(added, removed):
    if added:
        logging.info(f"Files added: {', '.join(added)}")
    if removed:
        logging.info(f"Files removed: {', '.join(removed)}")

# Example usage:
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     monitor_directory('/path/to/data', on_change)