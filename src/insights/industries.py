from src.insights.jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    csvfile = read(path)
    industry = []
    for jobs in csvfile: 
        if jobs["industry"] not in industry and jobs["industry"] != '':
            industry.append(jobs["industry"])
    return industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_industry_types = []
    for job_industry in jobs:
        if job_industry["industry"] == industry:
            filter_industry_types.append(job_industry)
    return filter_industry_types
