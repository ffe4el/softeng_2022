from django.utils import timezone

from django.db import models
from django.urls import reverse

#기본 기한 one_week_hence()을 설정하는 데 유용한 독립 실행형 유틸리티 기능을 정의합니다 .ToDoItem
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

#Django의 django.db.models.Model슈퍼클래스를 확장하는 두 개의 클래스를 정의
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]