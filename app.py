from get_info.cpu import CPU
from get_info.disk import Disk
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

    disk = Disk()
    disk.get()
    disk.show()


if __name__ == '__main__':
    main()
