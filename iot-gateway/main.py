def main():
    scanner = Scanner()
    print("waiting 10 seconds")
    time.sleep(10)
    strom = myStromManagement(scanner.get_device_hostnames())
    

if __name__ =="__main__":
    main()