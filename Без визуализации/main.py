def get_block_size(
        dataset: pd.DataFrame
):
    """"
    Определение размера блока

    :code_assign: users
    :code_type: Анализ данных
    :packages:
    import math
    import pandas as pd
    :param_block pd.DataFrame dataset: датасет, содержащий данные о скорости и количествеопераций чтения/записи
    :returns: message_text
    :rtype: str
    :semrtype: MSG
    """

    read_speed = float(dataset['read_speed'].iloc[0])
    write_speed = float(dataset['write_speed'].iloc[0])
    read_iops = float(dataset['read_iops'].iloc[0])
    write_iops = float(dataset['write_iops'].iloc[0])

    try:
        block_size_read: int = math.ceil((read_speed / read_iops))
    except ZeroDivisionError:
        block_size_read: int = 0
    try:
        block_size_write: int = math.ceil((write_speed / write_iops))
    except ZeroDivisionError:
        block_size_write: int = 0

    message_text: str = 'block_size_read = ' + str(block_size_read) + 'k\n' \
                        + 'block_size_write = ' + str(block_size_write) + 'k'

    return message_text
