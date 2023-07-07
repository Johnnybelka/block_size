import math

def get_block_size(
        iops: int,
        speed: int = 500
):
    """"
    Определение размера блока

    :code_assign: users
    :code_type: Анализ данных
    :packages:
    import math
    :param_block int speed: скорость чтения/записи
    :param_block int iops: количество операций ввода-вывода
    :returns: block_size
    :rtype: int
    :semrtype: ,
    """

    block_size: int = math.ceil((speed / iops))

    return block_size


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    iops = int(input("Enter iops value: "))
    block_size = get_block_size(iops)

    print("Block size: ", block_size)
