# main.py

import math
import statistics
import requests
from HandsOn import square, cube, average

def fetch_ip():
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        return response.json()['ip']
    return "Unavailable"

def main():
    data = [3, 7, 9, 2, 6]

    print("Original Data:", data)
    print("Squared:", [square(x) for x in data])
    print("Cubed:", [cube(x) for x in data])
    
    print("\n--- Statistics ---")
    print("Mean:", statistics.mean(data))
    print("Median:", statistics.median(data))
    print("Standard Deviation:", statistics.stdev(data))
    print("Custom Average (from HandsOn):", average(data))

    print("\n--- IP Address ---")
    ip = fetch_ip()
    print("Your Public IP Address is:", ip)

if __name__ == "__main__":
    main()
