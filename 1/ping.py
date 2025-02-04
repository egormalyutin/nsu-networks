from sys import argv
from ping3 import ping
import csv

if len(argv) != 3:
    print(f"usage: {argv[0]} hosts.csv output.csv")
    exit(1)

hosts_path, output_path = argv[1:]

hosts = []

with open(hosts_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) != 1:
            print("invalid hosts file format")
            exit(1)
        hosts.append(row[0])


with open(output_path, "w", newline="") as file:
    writer = csv.writer(file, delimiter=" ")
    writer.writerow(["host", "status", "delta"])

    for host in hosts:
        status = ping(host, unit="ms")
        if status is False:
            writer.writerow([host, "UNKNOWN", 0.0])
        elif status is None:
            writer.writerow([host, "TIMEOUT", 0.0])
        else:
            writer.writerow([host, "OK", status])

        file.flush()
