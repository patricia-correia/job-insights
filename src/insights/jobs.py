import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        job_list = []
        for list in reader:
            job_list.append(list)
    return job_list


def get_unique_job_types(path: str) -> List[str]:
    csvfile = read(path)
    job_types = []
    for jobs in csvfile:
        if jobs["job_type"] not in job_types:
            job_types.append(jobs["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_job_type.append(job)
    return filter_job_type
