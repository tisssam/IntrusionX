import re
from collections import defaultdict

FAILED_LOGIN_PATTERN = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"
THRESHOLD = 3


def analyze_logs(log_file):

    ip_attempts = defaultdict(int)

    with open(log_file, "r") as f:

        for line in f:

            match = re.search(FAILED_LOGIN_PATTERN, line)

            if match:
                ip = match.group(1)
                ip_attempts[ip] += 1

    suspicious_ips = []

    for ip, attempts in ip_attempts.items():

        if attempts >= THRESHOLD:

            suspicious_ips.append({
                "ip": ip,
                "attempts": attempts
            })

    return suspicious_ips