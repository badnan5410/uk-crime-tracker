import random, datetime

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

    def add_record(self, postcode, reporting_date):
        history_record = {
            "id": self.generate_record_id(),
            "postcode": postcode,
            "reporting_date": reporting_date,
            "searched_at": self.get_current_datetime()
        }

        # check if record_history is full, if true, remove first item
        if len(self.record_history) == self.MAX_HISTORY_ENTRIES:
            self.record_history.pop(0)

        # insert new record into record_history
        self.record_history.append(history_record)

    @staticmethod
    def get_current_datetime():
        date = datetime.datetime.now()

        formatted_date = date.strftime(
            "%d.%m.%Y | %H:%M:%S"
        )

        return formatted_date
