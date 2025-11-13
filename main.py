from csv import reader

class DataItem:
    def __init__(self, line):
        self.movieName = line[0]
        self.genre = line[1]
        self.releaseDate = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.durationMins = line[6]
        self.productionCompany = line[7]
        self.quote = line[8]


class HashTable():
    def __init__(self, length: int):
        self.length = length
        self.table = [None] * length

    def add(self, value: DataItem):
        pass

    def search(self, value: DataItem):
        pass

    def remove(self, value: DataItem):
        pass

    def _hash(self, data):
        key = 0
        if type(data) == int:
            pass
        elif type(data) == str:
            for c in data:
                key += ord(c)
        return key % self.length


def main():
    with open("MOCK_DATA.csv", encoding="UTF-8") as f:
        for row in reader(f):
            DataItem(row)
    print(HashTable(15000)._hash("asd"))


if __name__ == "__main__":
    main()