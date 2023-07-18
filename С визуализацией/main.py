import math
import pandas as pd

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

    dataframe['block_size_read']: int = math.ceil((read_speed / read_iops))
    dataframe['block_size_write']: int = math.ceil((write_speed / write_iops))

    message_text: str = 'block_size_read = ' + str(dataset['block_size_read'].iloc[0])+ 'k\n' \
                        + 'block_size_write = ' + str(dataset['block_size_write'].iloc[0]) + 'k'

    return message_text, dataframe


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataframe = pd.DataFrame({
        'tome_index': [2],
        'tome_name': ['pl109/vol2'],
        'read_iops': [140],
        'write_iops': [150],
        'read_speed': [550],
        'write_speed': [600]
    })
    message_text, new_dataframe = get_block_size(dataframe)

    print(message_text)
