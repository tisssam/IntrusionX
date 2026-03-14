import subprocess
import platform

blocked_ips = set()

def block_ip(ip):

    if ip in blocked_ips:
        return

    blocked_ips.add(ip)

    system = platform.system()

    if system == "Linux":

        try:

            subprocess.run(
                ["iptables","-A","INPUT","-s",ip,"-j","DROP"],
                check=True
            )

            print(f"[BLOCKED] {ip}")

        except Exception as e:

            print(f"[ERROR] Failed to block {ip}: {e}")

    else:

        print(f"[SIMULATION] Blocking IP: {ip}")