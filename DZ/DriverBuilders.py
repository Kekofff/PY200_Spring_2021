from abc import ABC, abstractmethod
from DZ.a_driver import IStructureDriver, JsonFileDriver, PickleFileDriver, CsvFileDriver


class DriverBuilder(ABC):
    @abstractmethod
    def build(self) -> IStructureDriver:
        ...


class JsonFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.json'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название json файла: (.json)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.json'):
            filename = f'{filename}.json'
        return JsonFileDriver(filename)


class PickleFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.pickle'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название pickle файла: (.pickle)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.pickle'):
            filename = f'{filename}.pickle'
        return PickleFileDriver(filename)


class CsvFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.csv'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название csv файла: (.csv)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.csv'):
            filename = f'{filename}.csv'
        return CsvFileDriver(filename)


class FabricDriverBuilder:
    DRIVER_BUILDER = {
        'json_file': JsonFileBuilder,
        'pickle_file': PickleFileBuilder,
        'csv_file': CsvFileBuilder
    }
    DEFAULT_DRIVER = 'json_file'

    @classmethod
    def get_driver(cls):
        driver_name = input("Введите название драйвера: ")
        driver_name = driver_name or cls.DEFAULT_DRIVER

        driver_builder = cls.DRIVER_BUILDER[driver_name]
        return driver_builder.build()


if __name__ == '__main__':
    driver = FabricDriverBuilder.get_driver()