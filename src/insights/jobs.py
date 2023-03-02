from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csv_file:
        jobs_csv = csv.DictReader(csv_file, delimiter=",")
        jobs_list = []
        for job in jobs_csv:
            jobs_list.append(job)
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_type_list = set()
    for type in jobs:
        job_type_list.add(type["job_type"])
    return job_type_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    search_job_type = list()
    for type_jobs in jobs:
        if type_jobs['job_type'] == job_type:
            search_job_type.append(type_jobs)
    return search_job_type
