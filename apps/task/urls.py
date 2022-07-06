from rest_framework import routers
from apps.task.views import TaskViewSet

router = routers.SimpleRouter(trailing_slash=False)


router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    *router.urls,
]
