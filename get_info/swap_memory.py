import psutil


class SwapMemory:

    def get(self):
        return psutil.swap_memory()

    def format(self):
        total_swap_memory = round(int(self.get()[0]) / 1024 / 1024 / 1024, 2)
        used_swap_memory = round(int(self.get()[1]) / 1024 / 1024 / 1024, 2)
        free_swap_memory = round(int(self.get()[2]) / 1024 / 1024 / 1024, 2)
        format_info = 'Total swap memory: {} GB\n' \
                      'Used swap memory: {} GB\n' \
                      'Free swap memory: {} GB'. \
            format(total_swap_memory, used_swap_memory, free_swap_memory)
        print('-' * 150)
        return format_info

    def show(self):
        print(self.format())
