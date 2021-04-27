# worker.py
import time, os
from jobs import q, update_job_status

worker_ip = os.environ.get('WORKER_IP')

@q.worker
def execute_job(jid):
    update_job_status(jid, "in progress", worker_ip)
    time.sleep(15)
    update_job_status(jid, "complete")

execute_job()