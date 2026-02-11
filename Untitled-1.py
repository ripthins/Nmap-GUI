# ...existing code...
import shutil
import subprocess
import json
import nmap3

def run_nmap_bin(target):
    cmd = ["nmap", "-sC", "-sV", target]
    subprocess.run(cmd)

def run_nmap3(target):
    nm = nmap3.Nmap()
    out = nm.scan_top_ports(target)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    target = input("Enter target (IP or domain): ").strip()
    if not target:
        print("No target provided. Exiting.")
    elif shutil.which("nmap"):
        run_nmap_bin(target)
    else:
        run_nmap3(target)
# ...existing code...