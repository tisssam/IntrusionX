import time
import random

ips = [
"185.234.217.10",
"103.45.67.89",
"45.33.32.156"
]

while True:

    ip = random.choice(ips)

    log = f"Jul 10 Failed password for root from {ip} port 22 ssh2\n"

    with open("sample_logs/auth.log", "a") as f:
        f.write(log)

    print(f"Attack from {ip}")

    time.sleep(2)