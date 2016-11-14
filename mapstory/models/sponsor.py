from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField(blank=False)
    icon = models.ImageField(blank=False, upload_to='sponsors')
    description = models.TextField(blank=True)
    order = models.IntegerField(blank=True, default=0)
    stamp = models.CharField(max_length=8, blank=True)

    def url(self):
        return self.icon.url + "?" + self.stamp

    def save(self, *args, **kwargs):
        if self.icon.name:
            self.stamp = _stamp(self.icon.read())
        super(Sponsor, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Sponsor - %s' % self.name

    class Meta:
        ordering = ['order']

    def image_tag(self):
        return u'<img src="%s" />' % self.url()
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


def get_sponsors():
    return Sponsor.objects.filter(order__gte=0)
