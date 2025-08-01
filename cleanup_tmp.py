import os
import time

# Path to the directory
directory = "/tmp/test"
# Time in seconds (7 days)
seven_days_ago = time.time() - (7 * 24 * 60 * 60)

# Walk through the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Only delete files (not directories) older than 7 days
    if os.path.isfile(file_path):
        file_mtime = os.path.getmtime(file_path)
        if file_mtime < seven_days_ago:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
