import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="New Message",
            message="Sleeping time",
            timeout=10
        )
        time.sleep(3600)