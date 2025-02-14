from django.shortcuts import render
from .tasks import send_mail, send_welcome_mail, send_subscription_mail, send_change_password_mail
from datetime import datetime
from datetime import timedelta
from celery import group
from celery import chain
from celery import chord

# Create your views here.
def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')

        send_mail.appy_async(email)

        '''
        
        task = group(
            send_mail.s(email),  # s -> signature
            send_welcome_mail.s(email),
            send_subscription_mail.s(email)
        )

        tasks = chain(
            send_mail.s(email), # s -> signature
            send_welcome_mail.s(),
            send_subscription_mail.s(),
        )
        
        tasks.apply_async()
        '''

        chord(
            [
                send_mail.s(email),
                send_welcome_mail.s(email),
                send_subscription_mail.s(email),
            ]
        )(
            send_change_password_mail.s()
        )

        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })