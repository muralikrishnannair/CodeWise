from django.db import models

# Create your models here.

"""
Schema     : Questions
Fields     : title, language, difficulty_level, notes,
                topic, published_date, sample_input, sample_output, is_active

"""

class Questions(models.Model):
    title = models.CharField(max_length=200)

    LANGUAGE_CHOICES = (
        ("python", "python"),
        ( "java", "java"  ),
        ("javascript", "javascript"),
        ("c", "c")
      
    )

    language=models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default="python")

    DIFFICULTY_LEVEL = (
    ("easy", "easy"),
    ("medium", "medium"),
    ("hard", "hard")
    )

    difficulty_level=models.CharField(max_length=100, choices=DIFFICULTY_LEVEL, default="easy")

    notes=models.TextField(null=True)

    topic = models.CharField(max_length=200)

    published_date = models.DateTimeField(auto_now_add=True)

    sample_input = models.TextField()

    sample_output = models.TextField()

    is_active=models.BooleanField(default=True)


class Submissions(models.Model):

    answer=models.TextField()

    question_id = models.IntegerField()

    points=models.PositiveIntegerField(null=True)

    owner=models.CharField(max_length=100)

    submission_date=models.DateTimeField(auto_now_add=True)
    
    remarks=models.TextField(null=True)
    