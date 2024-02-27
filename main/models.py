from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="CategoryImg")

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='BannerIMG')

    def __str__(self):
        return self.title


class Slider(models.Model):
    img = models.ImageField(upload_to='SliderImg')
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    banner = models.ImageField(upload_to="ProfileImg", null=True, blank=True)
    img = models.ImageField(upload_to="ProfileImg", null=True, blank=True)
    explanation = models.TextField()

    def __str__(self):
        return self.first_name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SendPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='PostIMG')
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SendVideo(models.Model):
    title = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)
    text = models.TextField()
    url = models.URLField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    videos = models.FileField(upload_to='AboutVideo')

    def __str__(self):
        return self.title


class Team(models.Model):
    img = models.ImageField(upload_to='TeamImg')
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.f_name


class Information(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    fax = models.CharField(max_length=70)
    address = models.CharField(max_length=255)
    insta = models.URLField()
    tw = models.URLField()

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    subject = models.CharField(max_length=255)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    explanation = models.TextField()
    file = models.FileField(upload_to='ContactUs', null=True, blank=True)

    def __str__(self):
        return self.name


class SavedPost(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ManyToManyField(SendPost)

    def __str__(self):
        return self.author
