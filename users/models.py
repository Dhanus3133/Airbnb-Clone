import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import strip_tags
from django.template.loader import render_to_string


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KWR = "kwr"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KWR, "KWR"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10,  blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_USD)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)
    
    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string("emails/verify_email.html", context={"secret": secret, "name": self.first_name + ' ' + self.last_name})
            send_mail("Verify Airbnb Account",
                      strip_tags(html_message),
                      settings.EMAIL_FROM,
                      [self.email],
                      fail_silently=False,
                      html_message=html_message
                  )
            self.save()
        return

