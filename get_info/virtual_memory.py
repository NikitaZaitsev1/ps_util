import psutil


class VirtualMemory:
    info = {}
    template = 'Total Virtual Memory:{total}\n'

    def get(self):
        self.info.update(total=psutil.virtual_memory().total)
        self.info.update(used=psutil.virtual_memory().used)
        self.info.update(free=psutil.virtual_memory().free)

    def _prepare(self):
        self.template += 'Used Virtual Memory:'
        self.template += '{used}\n'

        self.template += 'Free Virtual Memory:'
        self.template += '{free}\n'

    def show(self):
        self._prepare()
        print(self.template.format(**self.info))
