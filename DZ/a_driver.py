"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""
import json
import pickle
import csv
from typing import Sequence
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер
        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер
        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, json_filename):
        self.json_filename = json_filename

    def read(self) -> Sequence:
        with open(self.json_filename) as f:
            return json.load(f)

    def write(self, data: Sequence, indent: int = 4) -> None:
        with open(self.json_filename, 'w') as f:
            data = [value for value in data]
            json.dump(data, f, indent=indent)


class PickleFileDriver(IStructureDriver):
    def __init__(self, pickle_filename):
        self.pickle_filename = pickle_filename

    def read(self) -> Sequence:
        with open(self.pickle_filename, 'rb') as f:
            return pickle.load(f)

    def write(self, data: Sequence):
        with open(self.pickle_filename, 'wb') as f:
            pickle.dump(data, f)


class CsvFileDriver(IStructureDriver):
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename

    def read(self) -> Sequence:
        list_ = []
        with open(self.csv_filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                list_.append(row)
        return list_

    def write(self, data: Sequence):
        with open(self.csv_filename, 'w') as f:
            csv_writer = csv.writer(f, delimiter=',', lineterminator="\r")
            for value in data:
                csv_writer.writerow(value)


if __name__ == '__main__':
    # driver = JsonFileDriver('my_test.json')
    # d = [1, 2, 3, 4, 5]
    # driver.write(d)
    # output = driver.read()
    # assert d == output

    # driver = PickleFileDriver('my_test.pickle')
    # d = [1, 2, 3, 4]
    # driver.write(d)
    # output = driver.read()
    # assert d == output

    driver = CsvFileDriver('my_test.csv')
    d = [["O1", "O2"], ["E", "15"], ["F", "19"]]
    driver.write(d)
    output = driver.read()
    # print(output)
    assert d == output