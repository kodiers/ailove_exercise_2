import os
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


def validate_image(file):
    """
    Validate the image size between 50Kb and 2Mb. Validate that image extension is '.jpg', '.jpeg', '.bmp', '.tiff', '.png'
    """
    filesize = file.size
    max_limit = 2.0
    min_limit = 50.0
    if filesize < min_limit * 1024:
        raise ValidationError("File size too small for Image recognition.")
    if filesize > max_limit * 1024 * 1024:
        raise ValidationError("The file size exceeds the maximum size (2 MB)")
    ext = os.path.splitext(file.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.bmp', '.tiff', '.png']
    if not ext in valid_extensions:
        raise ValidationError("Invalid Format file formats supported: JPG, BMP, PNG, TIFF")


def send_user_notification(message, from_email, to_email, reply=None):
    """
    Send notification to user
    """
    full_name = message.name + ' ' + message.surname
    template_html = 'email/notification.html'
    html_content = render_to_string(template_html, {'subject': message.subject, 'notification': message.text,
                                                    'full_name': full_name, 'phone': message.phone,
                                                    'sender_email': message.email, 'reply': reply})
    text_content = strip_tags(html_content)
    if reply:
        # If reply send notification to user, which created message
        to_email = message.email
    msg = EmailMultiAlternatives(message.subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    if message.image:
        msg.attach_file(message.image.path)
    msg.send(fail_silently=False)