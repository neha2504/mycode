import os
import time

def delete_old_files(directory, days_old):
    now = time.time()
    cutoff = now - (days_old * 86400)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff:
            os.remove(file_path)
            print(f"Deleted {file_path}")

if __name__ == "__main__":
    target_directory = "/Users/nehachaudhary/Desktop/Kubernetes"
    days_to_keep = 5
    
    while True:
        delete_old_files(target_directory, days_to_keep)
        time.sleep(86400)  # Run daily
