import random

class HistoryManager:
    MAX_HISTORY_ENTRIES = 10

    def __init__(self):
        self.record_history = []

    def generate_record_id(self):
        while True:
            record_id = str(
                random.randint(100000000000, 999999999999)
            )

            duplicate_found = False
            for record in self.record_history:
                if record["id"] == record_id:
                    duplicate_found = True
                    break

            if not duplicate_found:
                return record_id