import psutil


class DiskUsage:

    def get(self):
        return psutil.disk_usage('/')

    def prepare_info(self):
        prepared_data = []
        total = round(int(self.get()[0]) / 1024 / 1024 / 1024, 2)
        used = round(int(self.get()[1]) / 1024 / 1024 / 1024, 2)
        free = round(int(self.get()[2]) / 1024 / 1024 / 1024, 2)
        percent = round(int(self.get()[3]))
        prepared_data.append(total)
        prepared_data.append(used)
        prepared_data.append(free)
        prepared_data.append(percent)

        return prepared_data

    def show(self):
        format_info = 'Total root disk space: {} GB\n' \
                      'Used root disk space: {} GB\n' \
                      'Free root disk space: {} GB\n' \
                      'Percentage usage: {} %'. \
            format(self.prepare_info()[0], self.prepare_info()[1],
                   self.prepare_info()[2], self.prepare_info()[3])

        print('-' * 150)
        print(format_info)
