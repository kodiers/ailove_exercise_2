import hashlib
from celery.task import task

from .functions import send_user_notification


@task(name='send-email-task')
def send_email_task(message, reply=None):
    """
    Task for send email to user.
    :param message - Message object
    :param reply - Replies object
    :return: None
    """
    send_user_notification(message, 'robot@myservice.com', 'helpdesk@myservice.com', reply)