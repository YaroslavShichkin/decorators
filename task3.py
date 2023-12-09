import types
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        with open('log_task3.log', 'a') as file:
            start = str(datetime.datetime.now())
            file.write(f'Date and time of the function call: {start}\n')
            name = old_function.__name__
            file.write(f'Function name: {name}\n')
            items = args, kwargs
            file.write(f'Arguments: {items}\n')
            result = old_function(*args, **kwargs)
            file.write(f'Return value: {result}\n\n')
        return result
    return new_function

@logger
def flat_generator(list_of_lists):
    for item in sum(list_of_lists, []):
        yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        print(flat_iterator_item)

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()