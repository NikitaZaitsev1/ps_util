import psutil

from get_info.information import Information


class SwapMemory(Information):
    template = 'Total Swap Memory:{total}\n'

    def get(self):
        self.info.update(total=psutil.swap_memory().total)
        self.info.update(used=psutil.swap_memory().used)
        self.info.update(free=psutil.swap_memory().free)
        self.info.update(percent=psutil.swap_memory().percent)

    def _prepare(self):
        self.template += 'Used Swap Memory::'
        self.template += '{used}\n'

        self.template += 'Free Swap Memory::'
        self.template += '{free}\n'

        self.template += 'Percent of Swap Memory::'
        self.template += '{percent}\n'
