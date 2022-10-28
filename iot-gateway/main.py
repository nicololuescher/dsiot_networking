from myStromManagement import myStromManagement
from scanner import Scanner
import time

def main():
    scanner = Scanner()
    print("waiting 10 seconds")
    time.sleep(10)
    print("found devices: " + str(scanner.get_device_hostnames()))
    strom = myStromManagement(scanner.get_device_hostnames())
    

if __name__ =="__main__":
    main()