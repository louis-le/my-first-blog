from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #edited = False;
    #edited_date = models.DateTimeField(
    #        blank=True, null=True)
    vote_count = 0

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # def upvote(self):
    #     self.vote_count += 1

    # def downvote(self):
    #     self.vote_count -= 1

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #edited = False;
    #edited_date = models.DateTimeField(
    #        blank=True, null=True)
    approved_comment = models.BooleanField(default=False)
    sub_comments = []

    def approve(self):
        self.approved_comment = True
        self.save()

    def add_comment(self, comment):
        self.sub_comments.append(comment)

    def __str__(self):
        return self.text

# class SubComment(models.Model):
#     parent_comment = models.ForeignKey('blog.Comment', related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)
#     sub_comments = []

#     def approve(self):
#         self.approved_comment = True
#         self.save()

#     def add_comment(self, comment):
#         self.sub_comments.append(comment)

#     def __str__(self):
#         return self.text