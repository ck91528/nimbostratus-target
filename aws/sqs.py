import logging

from core.region_connection import SQSConnection


def teardown_sqs():
    conn = SQSConnection()
    
    for queue in conn.get_all_queues(prefix='nimbostratus'):
        
        # Empty the queue in order to remove it
        queue.clear()
        
        logging.warn('Removing SQS queue %s' % queue.name)
        conn.delete_queue(queue)