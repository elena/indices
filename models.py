from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


def app_choices(apps):
    APP_CHOICES = []
    i=1
    for x in apps:
        t = (x.split('.')[-1], str(x))
        #t = (str(x) , str(x))
        APP_CHOICES.append(t)
        i+=1
    return tuple(APP_CHOICES)



class IndexSection(models.Model):
    order   = models.IntegerField(help_text="number between 1-999, space evenly along this range",)
    desc    = models.CharField(max_length=100, blank=True, null=True, 
                    help_text="leave blank for a spacer")
    helper_text = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return '%s -- %s' % (self.order, self.desc)

    class Meta:
        ordering = ['order']
        


class IndexApp(models.Model):
    APP_CHOICES = app_choices(settings.INSTALLED_APPS)

    section = models.ForeignKey(IndexSection,)
    order   = models.IntegerField(help_text="number between 1-999, space evenly along this range",)
    #app     = models.IntegerField(max_length=100, choices=APP_CHOICES, blank=True, null=False)
    header  = models.CharField(max_length=100, choices=APP_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return self.header

    class Meta:
        ordering = ['section__order', 'order']



class IndexCustom(models.Model):
    app     = models.ForeignKey(IndexApp,)
    order   = models.IntegerField(help_text="number between 1-999, space evenly along this range",)
    model   = models.ForeignKey(ContentType, blank=True, null=True)
    alt_name = models.CharField(max_length=100, blank=True, null=True, help_text="Verbatim over-write model name")
    spec_msg = models.CharField(max_length=255, blank=True, null=True, help_text="Cute little message that will appear next to the model name")
    other_link = models.CharField(max_length=100, blank=True, null=True, help_text="Verbatim over-write href")
    shaded  = models.BooleanField(default=False,)

    def __unicode__(self):
        try:
            return self.model.name
        except:
            return 'None'

    class Meta:
        ordering = ['order']

    
