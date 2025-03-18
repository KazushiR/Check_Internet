import os

with open("Check_status.txt", "r") as file_read:
    status = file_read.read().strip()
    print(status)
    if status == "Email Sent":
        with open("Check_status.txt", "w") as file_write:
            file_write.write("Email Not Sent")