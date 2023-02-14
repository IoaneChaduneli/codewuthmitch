# from django.db import models

# # Create your models here.
# PRIORITY =(
#     ('H', 'High' ),
#     ('M', 'Medium'),
#     ('L', 'Low')
# )

# class Question(models.Model):
#     title                   = models.CharField(max_length=120)
#     Question                = models.TextField(max_length=400)
#     priority                = models.CharField(max_length=1, choices=PRIORITY)

#     def __str__(self) -> str:
#         return self.title
#     class Meta:
#         verbose_name = 'The Question'
#         verbose_name_plural = 'Users Questions'