from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    is_travel_agent = models.BooleanField(default=False)

class TravelAgentApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, blank=True)
    experience = models.TextField(help_text="Describe your travel industry experience")
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Application by {self.full_name}"
    
    def approve(self):
        self.status = 'approved'
        self.user.is_travel_agent = True
        self.user.save()
        self.save()
    
    def reject(self):
        self.status = 'rejected'
        self.save()

class PlaceCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Place Categories"

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Place(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.00)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='places/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Additional fields for rich content
    history = models.TextField(blank=True)
    highlights = models.TextField(blank=True)  # Store as JSON list
    best_time_to_visit = models.TextField(blank=True)
    getting_there = models.TextField(blank=True)
    tips = models.TextField(blank=True)  # Store as JSON list
    
    # For filtering and categorization
    categories = models.ManyToManyField(PlaceCategory)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    @property
    def highlights_list(self):
        import json
        return json.loads(self.highlights) if self.highlights else []
    
    @property
    def tips_list(self):
        import json
        return json.loads(self.tips) if self.tips else []

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.place.name}"

class Report(models.Model):
    REPORT_TYPES = [
        ('inappropriate', 'Inappropriate Content'),
        ('spam', 'Spam'),
        ('misinformation', 'Misinformation'),
        ('other', 'Other')
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed')
    ]
    
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reports_filed')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reports_resolved')
    
    def __str__(self):
        return f"Report by {self.reporter.username if self.reporter else 'Unknown'} on {self.place.name}"
    
    def resolve(self, admin_user):
        from django.utils import timezone
        self.status = 'resolved'
        self.resolved_at = timezone.now()
        self.resolved_by = admin_user
        self.save()
    
    def dismiss(self, admin_user):
        from django.utils import timezone
        self.status = 'dismissed'
        self.resolved_at = timezone.now()
        self.resolved_by = admin_user
        self.save()
