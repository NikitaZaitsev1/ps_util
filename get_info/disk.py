import psutil


class Disk:
    info = {}
    template = 'Total Disk:{total}\n'

    def get(self):
        self.info.update(total=psutil.disk_usage('/').total)
        self.info.update(used=psutil.disk_usage('/').used)
        self.info.update(free=psutil.disk_usage('/').free)
        self.info.update(percent=psutil.disk_usage('/').percent)

        self.info.update(device=[part.device for part in psutil.disk_partitions()])
        self.info.update(mountpoint=[m.mountpoint for m in psutil.disk_partitions()])

    def _prepare(self):
        self.template += 'Used Disk:'
        self.template += '{used}\n'

        self.template += 'Free Disk:'
        self.template += '{free}\n'

        self.template += 'Percent of Disk Usage:'
        self.template += '{percent}\n'

        self.template += 'Device:\n'

        for index in range(len(self.info['device'])):
            self.template += '{device[' + str(index) + ']}\n'

        self.template += 'Mountpoint:\n'

        for index in range(len(self.info['mountpoint'])):
            self.template += '{mountpoint[' + str(index) + ']}\n'

    def show(self):
        self._prepare()
        print(self.template.format(**self.info))
