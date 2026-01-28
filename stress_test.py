import time, random
from datetime import datetime
import json

# Used to generate the messy log string for stress test 
PATHS = {"app":"logs/app.log", "auth":"logs/auth.log", "payment": "logs/payment.log", "sql" : "logs/sql.log"}

LEVEL = ["INFO", "WARN", "CRITICAL", "ERROR"]

MESSAGE = {
    "app": [
        "Dashboard accessed",
        "Cache refreshed",
        "Background job executed"
    ],
    "auth": [
        "Login successful",
        "User not found",
        "Invalidated token"
    ],
    "payment": [
        "Payment rejected",
        "Payment sucessful",
        "Payment on hold"
    ],
    "sql": [
        "Invalid query execution",
        "INSERT query executed",
        "Could not find connection"
    ]
}

# Log is produced and written in the appropriate log file 
def prod_log(service, level):
    msg = random.choice(MESSAGE[service])
    time_stamp = datetime.now() 
    time_stamp = time_stamp.strftime("%d-%m-%Y %H:%M:%S")
    log_string = f"{level} {time_stamp} {service} {msg}"

    json_log = {
        "log_type": service,
        "message": log_string
    }

    with open(PATHS[service], "a") as f:
        f.write(json.dumps(json_log) + "\n")

# Stress test is executed on the pipeline 
def stress_test(rate, duration, burst):
    inter = 1/rate
    endtime = time.time() + duration

    while time.time() < endtime:
        service = random.choice(list(PATHS.keys()))

        if burst:
            level = "ERROR"
        else:
            level = random.choice(LEVEL)
        
        prod_log(service, level)
        time.sleep(inter)

# Main function is called to start the stress tests
# to evaluate pipeline performance 
if __name__ == "__main__":
    stress_test(10, 20, False)
    print("Light load concluded")

    stress_test(62, 20, False)
    print("Heavy load concluded")

    stress_test(1000, 30, True)
    print("Error burst concluded")