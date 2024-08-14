class testing():
    def __init__(self) -> None:
        self.name = None

    def set_name(self, name:str):
        self.name = name

    def print_name(self):
        print(self.name)


test_1 = testing()
test_1.set_name('test 1')

test_2 = testing()
test_2.set_name('test 2')
def new_bark(self:testing):
    print(f'overwritten testing {self.name}')

test_2.print_name = new_bark.__get__(test_2, testing)


test_1.print_name()
test_2.print_name()

def over_write(original_function, new_function, instance, parent_class):
    instance.original_function = new_function.__get__(instance, parent_class)