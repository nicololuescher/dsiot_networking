#!/usr/local/bin/python3

#pip3 install zeroconf requests
## zeroconf: mdns
## requests: HTTP

# sources:
## https://pypi.org/project/zeroconf/


#from socket import gethostbyname
#gethostbyname()

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf


class MyListener(ServiceListener):

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated\n\r")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed\n\r")

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        print(f"Service {name} added, service info: {info}\n\r")


zeroconf = Zeroconf()
listener = MyListener()
#browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener, port=7979)
#browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener, port=7979)
browser = ServiceBrowser(zeroconf, "_hap._tcp.local.", listener)

try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()