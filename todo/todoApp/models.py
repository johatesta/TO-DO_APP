from django.db import models

class Todo(models.model):
    tittle=models.CharField(max_length=120)
    description = models.TextField()
    completed=models.BooleanField(default=False)


    def __str__(self) -> str:
        return super().__str__()

