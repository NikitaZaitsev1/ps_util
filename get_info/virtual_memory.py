import psutil


class VirtualMemory:

    def get(self):
        return psutil.virtual_memory()

    def show(self):
        total_memory = round(int(self.get().total) / 1024 / 1024 / 1024, 0)
        used_memory = round(int(self.get().used) / 1024 / 1024 / 1024, 2)
        format_info = 'Total virtual memory: {} GB\nUsed virtual memory: {} GB'. \
            format(total_memory, used_memory)
        print('-' * 150)
        print(format_info)
