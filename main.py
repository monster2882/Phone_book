class Telebook:
    def __init__(self, filename):
        self.records = []
        self.id_record = self.load_current_id()
        self.filename = filename

    def load_current_id(self):
        try:
            with open("current_id.txt", "r") as file:
                content = file.readline().strip()
                if content:
                    return int(content)
                else:
                    return 1
        except FileNotFoundError:
            return 1

    def update_current_id(self):
        with open("current_id.txt", "w") as file:
            file.write(str(self.id_record))

    def add_record(self, surname: str, name: str, father_name: str, corporation: str, telephone: int, work_telephone: int):
        record = {
            "id_record": self.id_record,
            "surname": surname,
            "name": name,
            "father_name": father_name,
            "corporation": corporation,
            "telephone": telephone,
            "work_telephone": work_telephone
        }
        self.id_record += 1
        self.records.append(record)
        self.update_current_id()

    def save_to_file(self):
        with open(self.filename, 'a') as file:
            for record in self.records:
                file.write(f"id_record: {record['id_record']}\n")
                file.write(f"Surname: {record['surname']}\n")
                file.write(f"Name: {record['name']}\n")
                file.write(f"Father's Name: {record['father_name']}\n")
                file.write(f"Corporation: {record['corporation']}\n")
                file.write(f"Telephone: {record['telephone']}\n")
                file.write(f"Work Telephone: {record['work_telephone']}\n")
                file.write("\n")

    def return_book(self):
        with open("telebook.txt", 'r') as file:
            info_book = file.read()
            print(info_book)

    def redact_record(self, id_record: int, **kwargs):
        found_record = None
        for record in self.records:
            if record['id_record'] == id_record:
                found_record = record
                break

        if found_record is not None:
            for key, value in kwargs.items():
                if key in found_record:
                    found_record[key] = value

            self.save_to_file()
            print(f'Запись номер {id_record} отредактирована')
            print()
            return True

        print(f'Не получилось отредактировать запись номер {id_record}, проверьте id_record')
        print()
        return False

    def find_record(self, **kwargs):
        found_records = []
        for record in self.records:
            match = True
            for key, value in kwargs.items():
                if key in record and value != record[key]:
                    match = False
            if match:
                found_records.append(record)
        if len(found_records) != 0:
            print('Найденные записи:')
            print(*found_records, sep='\n')
            print()
        else:
            print(f'Совпадений не найдено по параметру {key}:{value}')
            print()


telebook = Telebook('telebook.txt')

telebook.add_record("Smith", "John", "Michael", "ABC Corp", 1234567890, 9876543210)
telebook.add_record("Johnson", "Jane", "Robert", "XYZ Inc", 9876543210, 1234567890)
telebook.add_record("Williams", "Emily", "David", "LMN Group", 5555555555, 4444444444)
telebook.add_record("Brown", "Olivia", "William", "PQR Industries", 1111111111, 2222222222)


telebook.save_to_file()

telebook.return_book()

telebook.redact_record(2, surname="Brown", corporation="PQR Industries")
telebook.redact_record(15, name='Timur')

telebook.find_record(name='q')
telebook.find_record(name='Sarah')

