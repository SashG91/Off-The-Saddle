from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Climb(models.Model):
    """
    Django model for the information stored
    about each climb type.
    """

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    CLIMB_DIFFICULTY_CHOICES = [
        ("1", "An ascend that can get challenging, weather and pace affect!"),
        ("2", "For those who are starting to take it seriously"),
        ("3", "An absolute beast that requires you to give it all you've got"),
    ]

    climb_difficulty = models.CharField(
        max_length=250,
        choices=CLIMB_DIFFICULTY_CHOICES,
        default="1",
        null=False
    )

    CLIMB_SURFACE_CHOICES = [
        ("ASPHALT", "A purely asphalt surface"),
        ("ASPHALTCOBBLED", "A combination of asphalt and cobble surface"),
    ]

    climb_surface = models.CharField(
        max_length=250,
        choices=CLIMB_SURFACE_CHOICES,
        default="1",
        null=False
    )

    climb_length_in_miles = models.DecimalField(
        null=True,
        decimal_places=1,
        max_digits=5,
    )

    climb_elevationgain_in_meters = models.DecimalField(
        null=True,
        decimal_places=1,
        max_digits=5,
    )

    climb_KOMQOM_in_minutes = models.CharField(
        max_length=250,
        default="1",
        null=False
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Django model for the information storage
    of every comment.
    """
    post = models.ForeignKey(
        Climb, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
