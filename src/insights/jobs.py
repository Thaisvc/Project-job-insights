from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
# https://docs.python.org/pt-br/3/library/csv.html?highlight=dictreader#csv.DictReader
def read(path: str) -> List[Dict]:
    with open(path) as csv_file:
        jobs_csv = csv.DictReader(csv_file, delimiter=",")
        jobs_list = []
        for job in jobs_csv:
            jobs_list.append(job)
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    # ou  set([job["job_type"] for job in file])
    job_type_list = set()
    for type in jobs:
        job_type_list.add(type["job_type"])
    return job_type_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
