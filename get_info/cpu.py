import psutil

from get_info.information import Information


class CPU(Information):
    template = 'CPU count:{count}\n'

    def get(self):
        self.info.update(count=psutil.cpu_count())
        self.info.update(freq=[freq.current for freq in psutil.cpu_freq(percpu=True)])
        self.info.update(percent=psutil.cpu_percent(interval=1, percpu=True))

    def _prepare(self):
        self.template += 'CPU frequency:\n'
        for index in range(len(self.info['freq'])):
            self.template += '{freq[' + str(index) + ']}\n'

        self.template += 'CPU Percent:\n'
        for index in range(len(self.info['percent'])):
            self.template += '{percent[' + str(index) + ']}\n'
