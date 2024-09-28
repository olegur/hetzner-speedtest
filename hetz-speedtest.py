import sys
import time
import requests
import math
import subprocess
import platform

hosts = {
  "fsn1-speed.hetzner.com",
  "hel1-speed.hetzner.com",
  "speed.hetzner.de",
  "ash.icmp.hetzner.com",
  "hil.icmp.hetzner.com"
}


# get latency of host
def get_latency(host):
  if platform.system() == "Windows":
    return 0
  try:
    output = subprocess.check_output(["ping", "-c", "1", host])
    output = output.decode("utf-8")
    output = output.split("\n")
    for line in output:
      if "time=" in line:
        return float(line.split("time=")[1].split(" ")[0])
  except:
    return 0


def main() :
  for host in hosts:
    if platform.system() == "Windows":
      print("Can't measure latency on Windows")
      continue
    print(f"Host: {host} Latency: {get_latency(host)}ms")

if __name__ == "__main__" :
  main()
