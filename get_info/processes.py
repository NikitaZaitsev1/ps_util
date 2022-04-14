import psutil
from colorama import Fore


class Processes:

    def get(self):
        return psutil.process_iter()

    def show(self):
        header = '{:^5}{:^30}{:^20}{:<50}'.format('PID', 'NAME', 'STATUS', 'USER')
        print('-' * 150)
        print(header)
        print('-' * 60)
        for proc in self.get():
            print(Fore.GREEN + '{:^5}{:^30}{:^20}{:<50}'.format(proc.as_dict()['pid'],
                                                                proc.as_dict()['name'],
                                                                proc.as_dict()['status'],
                                                                proc.as_dict()['username']))
