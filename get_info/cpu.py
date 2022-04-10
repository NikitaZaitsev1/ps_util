import psutil


class CPU:

    def get(self):
        cpu_list = []
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq(percpu=True)[0][0]
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_list.append(cpu_count)
        cpu_list.append(cpu_freq)
        cpu_list.append(cpu_percent)
        return cpu_list

    def format(self):
        cpu_count = str(self.get()[0])
        cpu_freq = str(self.get()[1])
        cpu_percent = str(self.get()[2])
        format_info = 'Number of logical CPUs: {}\n' \
                      'The current CPU frequency: {} Ghz\n' \
                      'The current system-wide CPU utilization: {} %'. \
            format(cpu_count, cpu_freq, cpu_percent)
        return format_info

    def show(self):
        print(self.format())
