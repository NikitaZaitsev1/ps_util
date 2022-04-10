import psutil


class DiskUsage:

    def get(self):
        return psutil.disk_usage('/')

    def format(self):
        total = round(int(self.get()[0]) / 1024 / 1024 / 1024, 2)
        used = round(int(self.get()[1]) / 1024 / 1024 / 1024, 2)
        free = round(int(self.get()[2]) / 1024 / 1024 / 1024, 2)
        percent = round(int(self.get()[3]))
        format_info = 'Total root disk space: {} GB\n' \
                      'Used root disk space: {} GB\n' \
                      'Free root disk space: {} GB\n' \
                      'Percentage usage: {} %'. \
            format(total, used, free, percent)
        print('-' * 150)
        return format_info

    def show(self):
        print(self.format())
