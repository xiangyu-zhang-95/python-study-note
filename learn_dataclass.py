import dataclasses

@dataclasses.dataclass
class Foo:
    name: str
    value: float

foo = Foo("az", 3.1415)
print(foo.name, foo.value)