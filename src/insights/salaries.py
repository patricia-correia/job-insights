from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    salaries = []
    salary = 0
    for job in jobs_list:
        if job["max_salary"] != '' and job["max_salary"] != 'invalid':
            salaries.append(int(job["max_salary"]))
    for value in salaries:
        if value > salary:
            salary = value
    return salary


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    salaries = []
    for job in jobs_list:
        if job["min_salary"] != '' and job["min_salary"] != 'invalid':
            salaries.append(int(job["min_salary"]))
    salary = salaries[0]
    for value in salaries:
        if value < salary:
            salary = value
    return salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        int(salary)
    except TypeError:
        raise ValueError

    if min_salary > max_salary:
        raise ValueError
    return max_salary >= int(salary) >= min_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filtered_jobs_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs_range.append(job)
        except ValueError:
            pass
    return filtered_jobs_range
