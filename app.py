from get_info.cpu import CPU
from get_info.disk_usage import DiskUsage
from get_info.processes import Processes
from get_info.swap_memory import SwapMemory
from get_info.virtual_memory import VirtualMemory


def main():
    cpu = CPU()
    cpu.get()
    cpu.show()

    virtual_memory = VirtualMemory()
    virtual_memory.get()
    virtual_memory.show()

    swap_memory = SwapMemory()
    swap_memory.get()
    swap_memory.show()

    disk_usage = DiskUsage()
    disk_usage.get()
    disk_usage.show()

    processes = Processes()
    processes.get()
    processes.show()


if __name__ == '__main__':
    main()
