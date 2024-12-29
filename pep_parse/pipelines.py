import csv
from collections import defaultdict

from itemadapter import ItemAdapter

from pep_parse.settings import BASE_DIR, FILE_NAME


class PepParsePipeline:

    def open_spider(self, spider):

        self.number_of_pep = defaultdict(int)

        DOWNLOADS_DIR = BASE_DIR / 'results'
        DOWNLOADS_DIR.mkdir(exist_ok=True)
        archive_path = DOWNLOADS_DIR / FILE_NAME
        self.file = open(archive_path, 'w', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Статус', 'Количество'])

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if 'status' in adapter.keys():
            status = adapter['status']
            self.number_of_pep[status] += 1

        return item

    def close_spider(self, spider):
        self.number_of_pep['Total'] = sum(self.number_of_pep.values())
        self.writer.writerows(self.number_of_pep.items())
        self.file.close()
