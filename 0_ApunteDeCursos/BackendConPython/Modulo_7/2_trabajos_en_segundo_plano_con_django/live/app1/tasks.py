from celery import shared_task

@shared_task
def send_mail(to):
    print(f'Mail sent to {to}!')
    return to

@shared_task
def send_welcome_mail(to):
    print(f'Mail welcome sent to {to}!')
    return to

@shared_task
def send_subscription_mail(to):
    print(f'Mail subscription sent to {to}!')
    return to

@shared_task
def send_change_password_mail(*args):
    print(f'Mail change_password sent!')