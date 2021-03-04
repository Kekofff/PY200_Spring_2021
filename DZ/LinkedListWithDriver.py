from lesson_3.linked_list import LinkedList
from DZ.a_driver import IStructureDriver, JsonFileDriver, PickleFileDriver, CsvFileDriver
from DZ.DriverBuilders import FabricDriverBuilder


class LinkedListWithDriver(LinkedList):
    def __init__(self, data, driver: IStructureDriver = None):
        super().__init__(data)
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver or FabricDriverBuilder.get_driver()

    @driver.setter
    def driver(self, driver):
        self.__driver = driver


    def read(self):
        """Взять драйвер и считать из него информацию в LinkedList"""
        output = self.driver.read()
        self.clear()
        for value in output:
            self.append(value)

    def write(self):
        """Взять драйвер и записать в него информацию из LinkedList"""
        self.driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver([["O1", "O2"], ["E", "15"], ["F", "19"]])  # проверка для csv драйвера
    ll.write()
    ll = LinkedListWithDriver([])
    ll.read()
    print(ll)


