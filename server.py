"""Run the scheduler process."""

from ndscheduler.server import server


class SimpleServer(server.SchedulerServer):

    def post_scheduler_start(self):
        # New user experience! Make sure we have at least 1 job to demo!
        jobs = self.scheduler_manager.get_jobs()
        # if len(jobs) == 0:
        #     self.scheduler_manager.add_job(
        #         job_class_string='simple_scheduler.jobs.sample_job.AwesomeJob',
        #         name='My Awesome Job',
        #         pub_args=['first parameter', {'second parameter': 'can be a dict'}],
        #         minute='*/1')
        #           c:\Users\DBdata\Desktop\ddd\c:\Users\DBdata\Desktop\ddd\db_sched_report_py36_deploy\jobs\workers\zbx_host_stats\zbx_host_stats.py


if __name__ == "__main__":
    SimpleServer.run()
