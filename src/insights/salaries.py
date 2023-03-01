from typing import Union, List, Dict
from jobs import read


def get_max_salary(path: str) -> int:
    list_jobs = read(path)
    salaries = set(
        [job["max_salary"] for job in list_jobs
         # https://www.w3schools.com/python/ref_string_isdigit.asp
         # https://www.w3schools.com/python/ref_func_int.asp
         if job["max_salary"].isdigit()]
        )
    salaries = (int(salary) for salary in salaries)
    return max(salaries)


def get_min_salary(path: str) -> int:
    list_jobs = read(path)
    salaries = set(
        [job["min_salary"] for job in list_jobs
         if job["min_salary"].isdigit()]
        )
    salaries = (int(salary) for salary in salaries)

    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    types_value = [str, int]
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if not all(type(
        job[sal]) in types_value for sal in ["min_salary", "max_salary"]
               ):
        raise ValueError
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError
    if not type(salary) in types_value:
        raise ValueError
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    salarie_value = []
    for job in jobs:
        try:
            value = matches_salary_range(job, salary)
            if value:
                salarie_value.append(job)
        except ValueError:
            print("invalid")
    return salarie_value
