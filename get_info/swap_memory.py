import psutil


class SwapMemory:

    def get(self):
        return psutil.swap_memory()

    def prepare_info(self):
        prepared_data = []
        total_swap_memory = round(int(self.get()[0]) / 1024 / 1024 / 1024, 2)
        used_swap_memory = round(int(self.get()[1]) / 1024 / 1024 / 1024, 2)
        free_swap_memory = round(int(self.get()[2]) / 1024 / 1024 / 1024, 2)
        prepared_data.append(total_swap_memory)
        prepared_data.append(used_swap_memory)
        prepared_data.append(free_swap_memory)

        return prepared_data

    def show(self):
        format_info = 'Total swap memory: {} GB\n' \
                      'Used swap memory: {} GB\n' \
                      'Free swap memory: {} GB'. \
            format(self.prepare_info()[0], self.prepare_info()[1], self.prepare_info()[2])

        print('-' * 150)
        print(format_info)
