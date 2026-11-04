def without_zeros(numbers):
    """Возвращает числа без нулей. Переданный список менять нельзя."""
    for index in range(len(numbers)):
        if numbers[index] == 0:
            del numbers[index]
    return numbers


def done_share(tasks):
    """Доля задач с done == True, округлённая до 2 знаков. Пустой список — 0."""
    done = 0
    for task in tasks:
        if task["done"]:
            done += 1
    share = done / len(tasks)
    if not tasks:
        return 0
    return round(share, 2)
