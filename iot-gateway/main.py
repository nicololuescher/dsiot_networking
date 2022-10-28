#!/usr/local/bin/python3

# Elia Bieri

import time

from rich.live import Live
from rich.table import Table

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

mystrom_devices : list[str] = []

class MyListener(ServiceListener):

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        mystrom_devices.append(info.server[:-1])

def generate_table() -> Table:
    table = Table()
    table.add_column("name")

    for device in mystrom_devices:
        table.add_row(device)
    return table


def main():
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_hap._tcp.local.", listener)
    with Live(generate_table(), refresh_per_second=4) as live:
        for _ in range(40):
            time.sleep(0.4)
            live.update(generate_table())

if __name__ == "__main__":
    main()