from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    file_jobs = read(path)
    industrie = set()
    for row in file_jobs:
        if row["industry"] != "":
            industrie.add(row["industry"])
    return industrie


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_list = list(
        [job for job in jobs
         if job["industry"] == industry]
        )
    return jobs_list
