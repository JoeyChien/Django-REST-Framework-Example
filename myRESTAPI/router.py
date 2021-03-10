from todolistapi.viewsets import TodoListViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todolist', TodoListViewset)
