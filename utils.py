from datetime import datatime

def format_message(username, message):
    current_time = datatime.now().strftime('%H:%M')
    return f"[{current_time}] {username} : {message}"
def system_messege(messege):
    return f"[SYSTEM] {messege}"
