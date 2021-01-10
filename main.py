from indeed import get_jobs as get_jobs_from_indeed
from so import get_jobs as get_jobs_from_so
from save import save_to_file

indeed_jobs = get_jobs_from_indeed()
so_jobs = get_jobs_from_so()
jobs = indeed_jobs + so_jobs

save_to_file(jobs)

