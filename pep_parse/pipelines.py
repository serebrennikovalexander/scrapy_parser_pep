import csv
from datetime import datetime
from pep_parse.settings import BASE_DIR

from itemadapter import ItemAdapter


class PepParsePipeline:

    def __init__(self):
        self.number_of_pep = {}
        self.total = 0

    def open_spider(self, spider):
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"status_summary_{formatted_time}.csv"
        downloads_dir = BASE_DIR / "results"
        downloads_dir.mkdir(exist_ok=True)
        archive_path = downloads_dir / file_name
        self.file = open(archive_path, "w", newline="")
        self.writer = csv.writer(self.file)
        self.writer.writerow(["Статус", "Количество"])

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if "status" in adapter.keys():
            status = adapter["status"]
            self.total += 1
            self.number_of_pep[status] = self.number_of_pep.get(status, 0) + 1

        return item

    def close_spider(self, spider):
        self.writer.writerows(self.number_of_pep.items())
        self.writer.writerow(["Total", self.total])
        self.file.close()
