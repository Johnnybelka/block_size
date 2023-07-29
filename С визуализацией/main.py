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
    :returns: message_text, dataset
    :rtype: str, pd.DataFrame
    :semrtype: MSG, DataSet
    """

    read_speed = float(dataset['read_speed'].iloc[0])
    write_speed = float(dataset['write_speed'].iloc[0])
    read_iops = float(dataset['read_iops'].iloc[0])
    write_iops = float(dataset['write_iops'].iloc[0])

    try:
        dataset['block_size_read']: int = math.ceil((read_speed / read_iops))
    except ZeroDivisionError:
        dataset['block_size_read']: int = 0
    try:
        dataset['block_size_write']: int = math.ceil((write_speed / write_iops))
    except ZeroDivisionError:
        dataset['block_size_write']: int = 0

    message_text: str = 'clock: ' + str(dataset['clock'].iloc[0]) + '\n' \
                        + 'read_iops = ' + str(dataset['read_iops'].iloc[0]) + '\n' \
                        + 'read_speed = ' + str(dataset['read_speed'].iloc[0]) + 'Mb/s\n' \
                        + 'block_size_read = ' + str(dataset['block_size_read'].iloc[0]) + 'k\n' \
                        + 'write_iops = ' + str(dataset['write_iops'].iloc[0]) + '\n' \
                        + 'write_speed = ' + str(dataset['write_speed'].iloc[0]) + 'Mb/s\n' \
                        + 'block_size_write = ' + str(dataset['block_size_write'].iloc[0]) + 'k'

    return message_text, dataset
