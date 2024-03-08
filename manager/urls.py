from django.urls import path

from .views import TaskView, TaskEditView

urlpatterns = [
    path("task/", TaskView.as_view(), name="task"),
    path("task/<int:id>/", TaskEditView.as_view(), name="task-edit"),
]