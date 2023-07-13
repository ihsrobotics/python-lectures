from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class DiskObject(ABC):
    """
    Represents an abstract object on a filesystem
    """

    name: str
    date_created: datetime

    @property
    @abstractmethod
    def size(self) -> int:
        pass


class File(DiskObject):
    """
    A simple file on a filesystem
    """

    def __init__(self, name: str, date_created: datetime, file_size: int) -> None:
        super().__init__(name, date_created)
        self.__size = file_size

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        if type(size) == int and size >= 0:
            self.__size = size
        else:
            raise ValueError("Sizes should be integers greater than or equal to 0")


class Directory(DiskObject):
    """
    A directory on a filesystem; it can contain files, other directories, and anything that
    derives from DiskObject
    """

    def __init__(
        self, name: str, date_created: datetime, *children: DiskObject
    ) -> None:
        super().__init__(name, date_created)
        self.children = list(children)

    @property
    def size(self) -> int:
        return sum(map(lambda disk_object: disk_object.size, self.children))


cool_image = File("image.png", datetime.now(), 128000)
print(cool_image.size)

text_file = File("text.txt", datetime.now(), 1000)
text_file.size = 2000  # this should work
try:
    text_file.size = -1000  # this should raise an exception caught by the except clause
except ValueError:
    print("correctly stopped user from trying to resize text file to negative size")

first_directory = Directory("directory", datetime.now(), cool_image, text_file)
print(
    first_directory.size
)  # this should be equivalent to cool_image.size + text_file.size
print(first_directory.children)

second_directory = Directory(
    "/",
    datetime.now(),
    File("temp.b", datetime.now(), 100),
    File("other.b", datetime.now(), 247),
    first_directory,  # since `Directory`s are `DiskObjects`, this should work
)
print(second_directory.size)
