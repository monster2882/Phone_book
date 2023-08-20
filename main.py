class Telebook:
    def __init__(self):
        self.records = []
        self.id_record = 1

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

    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
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
        for record in self.records:
            print(f"id_record: {record['id_record']}")
            print(f"Surname: {record['surname']}")
            print(f"Name: {record['name']}")
            print(f"Father's Name: {record['father_name']}")
            print(f"Corporation: {record['corporation']}")
            print(f"Telephone: {record['telephone']}")
            print(f"Work Telephone: {record['work_telephone']}")
            print()

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

            self.save_to_file("telebook.txt")
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



telebook = Telebook()
telebook.add_record("Smith", "John", "Michael", "ABC Corp", 1234567890, 9876543210)
telebook.add_record("Johnson", "Jane", "Robert", "XYZ Inc", 9876543210, 1234567890)
telebook.add_record("Williams", "Sarah", "David", "LMN Ltd", 9871234560, 7894561230)
telebook.add_record("Brown", "James", "William", "PQR Industries", 5551234567, 7779876543)
telebook.add_record("Davis", "Emily", "Thomas", "DEF Group", 1112223333, 4445556666)
telebook.add_record("Martinez", "Daniel", "Jose", "GHI Solutions", 8881112222, 3334445555)
telebook.add_record("Miller", "Linda", "Susan", "JKL Enterprises", 6667778888, 2223334444)
telebook.add_record("Jones", "Michael", "Christopher", "MNO Corporation", 3334445555, 8889990000)
telebook.add_record("Garcia", "Maria", "Juan", "RST Inc", 4445556666, 7778889999)
telebook.add_record("Lee", "Sarah", "Richard", "UVW Group", 9990001111, 1112223333)
telebook.return_book()
telebook.save_to_file("telebook.txt")

telebook.redact_record(2, surname="Brown", corporation="PQR Industries")
telebook.redact_record(15, name='Timur')

telebook.find_record(name='q')
telebook.find_record(name='Sarah')