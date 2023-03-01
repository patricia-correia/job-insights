from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    count_python = count_ocurrences(path, 'python')
    count_tasks = count_ocurrences(path, 'tasks')

    assert count_python == 1639
    assert count_tasks == 745
