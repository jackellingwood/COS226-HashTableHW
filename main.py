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


def main():
    with open("MOCK_DATA.csv", encoding="UTF-8") as f:
        for row in reader(f):
            DataItem(row)


if __name__ == "__main__":
    main()