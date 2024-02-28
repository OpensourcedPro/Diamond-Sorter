import json


class Config:
    def __init__(self):
        self.config_file = "settings.json"

    def settings_reader(self):
        with open(self.config_file, "r", encoding='utf-8') as read_file:
            data = json.load(read_file)
        return data

    def settings_write(self, data):
        with open(self.config_file, "w", encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4)

class DB_logs:
    def __init__(self):
        self.config_file = "logs_info.json"

    def settings_reader(self):
        with open(self.config_file, "r", encoding='utf-8') as read_file:
            data = json.load(read_file)
        return data

    def settings_write(self, data):
        with open(self.config_file, "w", encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4)

