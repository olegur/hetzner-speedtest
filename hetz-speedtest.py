import sys
import time
import requests
import math
import subprocess
import platform
import multiprocessing

hosts = {
  "fsn1-speed.hetzner.com",
  "hel1-speed.hetzner.com",
  "speed.hetzner.de",
  "ash.icmp.hetzner.com",
  "hil.icmp.hetzner.com"
}


# get latency of host
def get_latencyavg(host):
  if platform.system() == "Windows":
    return 0
  try:
    print(host)
    output = subprocess.check_output(["ping", "-c", "10", host])
    output = output.decode("utf-8")
    output = output.split("\n")
    listavg = []
    for line in output:
      if "time=" in line:
        listavg.append(float(line.split("time=")[1].split(" ")[0]))
    latencyAvg = sum(listavg) / len(listavg)
    print(f"Host: {host} Latency: {(latencyAvg)}ms")
  except:
    return 0


def main() :
  if platform.system() == "Windows":
    print("Can't measure latency on Windows")
  #print(get_latencyavg(hosts))
  processPoolObj = multiprocessing.Pool()
  processPoolObj.map(get_latencyavg, hosts)
  processPoolObj.close()
  #print(result)
if __name__ == "__main__" :
  main()
