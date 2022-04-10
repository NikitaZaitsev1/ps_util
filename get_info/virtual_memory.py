import psutil


class VirtualMemory:

    def get(self):
        return psutil.virtual_memory()

    def prepare_info(self):
        prepared_data = []
        total_memory = round(int(self.get().total) / 1024 / 1024 / 1024, 0)
        used_memory = round(int(self.get().used) / 1024 / 1024 / 1024, 2)
        prepared_data.append(total_memory)
        prepared_data.append(used_memory)

        return prepared_data

    def show(self):
        format_info = 'Total virtual memory: {} GB\nUsed virtual memory: {} GB'. \
            format(self.prepare_info()[0], self.prepare_info()[1])

        print('-' * 150)
        print(format_info)
