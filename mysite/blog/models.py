from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
  author=models.ForeignKey('auth.User')
  title=models.CharField(max_length=200)
  text=models.TextField()
  create_date=models.DateTimeField(default=timezone.now())
  published_date=models.DateTimeField(blank=True,null=True)

  def publish(self):
    self.published_date=timezone.now()
    self.save()

  def approve_comments(self):
    return self.comments.filter(approved_comments=True)

  def get_absolute_url(self):
    return reverse("post_detail",kmargs={'pk':self.pk})

  def _str_(self):
    return self.title

class Comment(model,MOdel):
  post=models.ForeignKey('blog.Post',related_name='comments')
  author=models.CharField(max_length=200)
  text=models/TextField()
  create_data=models.DataTimeField(default=timezone.now())
  approved_comment=models.BooleanField(default=False)

  def approve(self):
    self.approved_comment=True
    self/save( )

  def get_absolute_url(self):
    return reverse('post_list')
    

  def _str_(self):
    return self.text