import os
from indeed import get_jobs as get_indeed_jobs

os.system("clear")

indeed_jobs = get_indeed_jobs()
print(indeed_jobs)