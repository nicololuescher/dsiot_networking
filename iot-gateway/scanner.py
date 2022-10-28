from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
import requests
import time

class Scanner:
    class MyListener(ServiceListener):
        def __init__(self):
            self._hostnames: list[str] = []

        def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
            pass

        def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
            pass

        def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
            info = zc.get_service_info(type_, name)
            self._hostnames.append(info.server[:-1])

    def __init__(self):
        zeroconf = Zeroconf()
        self._listener = self.MyListener()
        self._browser = ServiceBrowser(zeroconf, "_hap._tcp.local.", self._listener)

    def get_device_hostnames(self) -> list[str]:
        return self._listener._hostnames

if __name__ == "__main__":
    scanner = Scanner()
    while True:
        print(f"----\n{scanner.get_device_hostnames()}")
        time.sleep(2)