import subprocess

def block_ip(ip):

    try:
        subprocess.run(
            ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )

        print(f"[BLOCKED] {ip}")

    except Exception as e:

        print(f"[ERROR] Failed to block {ip}: {e}")