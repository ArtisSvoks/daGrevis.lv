from django.db import models


class LegacyArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.IntegerField()
    last_updated = models.IntegerField()
    tweet_id = models.CharField(max_length=255, null=True)

    class Meta(object):
        app_label = "legacy"
        db_table = "blog_articles"

    def __unicode__(self):
        return self.title
