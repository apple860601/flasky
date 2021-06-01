from ndscheduler import job
import apscheduler,logging,sys
sys.path.append('jobs/workers/zbx_host_stats')



logger = logging.getLogger(__name__)
class AINOCJob(job.JobBase):

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'notes': 'This sends a push notification to APNS servers. '
                     'The environment variable APNS_CERT_PATH" should be provided '
                     'for APNS cert file path.',
            'arguments': [
                # APNS device token
                {'token': 'string', 'description': 'Device token'},
                # APNS Title's Alert Text
                {'alert': 'string', 'description': 'What do you want to send?'},
            ],
            'example_arguments': ('["da1232badh2", "Hello from scheduler"]')
        }

    def run(self,*args):
        print(args)
        return pdfname

if __name__=='__main__':
    job = AINOCJob.create_test_instance()
    job.run()