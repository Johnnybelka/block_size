def get_block_size(
        dataset: pd.DataFrame
):
    """"
    Определение размера блока

    :code_assign: users
    :code_type: Пользовательские функции
    :imports: init_gui_dict, Window, Canvas, LinePlot
    :packages:
    import math
    import pandas as pd
    :param_block pd.DataFrame dataset: датасет, содержащий данные о скорости и количествеопераций чтения/записи
    :returns: message_text, dataset, gui_dict
    :rtype: str, pd.DataFrame, dict
    :semrtype: MSG, DataSet,
    """

    read_speed = float(dataset['read_speed'].iloc[0])
    write_speed = float(dataset['write_speed'].iloc[0])
    read_iops = float(dataset['read_iops'].iloc[0])
    write_iops = float(dataset['write_iops'].iloc[0])

    try:
        dataset['block_size_read']: int = math.ceil((read_speed / read_iops) / 1024)
    except ZeroDivisionError:
        dataset['block_size_read']: int = 0
    try:
        dataset['block_size_write']: int = math.ceil((write_speed / write_iops) / 1024)
    except ZeroDivisionError:
        dataset['block_size_write']: int = 0

    message_text: str = 'clock: ' + str(dataset['clock'].iloc[0]) + '\n' \
                        + 'read_iops = ' + str(dataset['read_iops'].iloc[0]) + ' ' \
                        + 'read_speed = ' + str(dataset['read_speed'].iloc[0]) + 'Mb/s ' \
                        + 'block_size_read = ' + str(dataset['block_size_read'].iloc[0]) + 'k\n' \
                        + 'write_iops = ' + str(dataset['write_iops'].iloc[0]) + ' '\
                        + 'write_speed = ' + str(dataset['write_speed'].iloc[0]) + 'Mb/s ' \
                        + 'block_size_write = ' + str(dataset['block_size_write'].iloc[0]) + 'k'

    gui_dict = init_gui_dict()

    gui_dict['text'].append({'title': 'График block_size_read', 'value': float(dataset['block_size_read'].iloc[0])})
    gui_dict['plot'].append(
        Window(
            window_title='Значения размеров блока',
            canvases=[Canvas(title='Размеры блоков',
                             x_title='Время',
                             y_title='block_size_read',
                             showlegend=True,
                             plots=[LinePlot(x=dataset['clock'],
                                             y=dataset['block_size_read'],
                                             names=['block_size_read'])]
                             ),
                      ]
        ).to_dict())

    return message_text, dataset, gui_dict
