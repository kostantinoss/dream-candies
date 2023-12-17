class Exporter:

    @staticmethod
    def export(string: str, filename: str):
        with open(filename, 'a') as file:
            file.write(string)