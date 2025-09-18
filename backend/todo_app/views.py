from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes, OpenApiResponse

@extend_schema(tags=['Todo'])
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        completed = self.request.query_params.get('completed', None)
        if completed is not None:
            completed_bool = completed.lower() == 'true'
            queryset = queryset.filter(completed=completed_bool)
        return queryset

    @extend_schema(
        summary="Получить весь список задач",
        description="Возвращает все задачи с возможностью фильтрации по статусу.",
        parameters=[
            OpenApiParameter(
                name='completed',
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Фильтр по статусу завершения (true/false)"
            ),
        ],
        examples=[
            OpenApiExample(
                "Пример ответа",
                value=[
                    {"id": 1, "content": "Купить продукты", "completed": False, "created_at": "2025-18-09T10:00:00Z"},
                    {"id": 2, "content": "Завершить проект", "completed": True, "created_at": "2025-18-09T10:00:00Z"}
                ]
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Создать новую задачу",
        description="Создает новую задачу с заданными параметрами",
        request=TaskSerializer,
        responses={
            200: TaskSerializer,
            400: OpenApiResponse(description="Неверно введены данные")
        },  
        examples=[
            OpenApiExample(
                "Пример запроса",
                value={"content": "Новая задача"}
            ),
            OpenApiExample(
                'Пример ответа',
                value={"id": 3, "content": "Новая задача", "completed": False, "created_at": "2025-18-09T10:00:00Z"}
            )
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

    @extend_schema(
        summary="Получить одну задачу",
        description="Возвращает детали конкретной задачи по ID.",
        responses={
            200: TaskSerializer,
            404: OpenApiResponse(description="Задача не найдена")
        }, 
        examples=[
            OpenApiExample(
                'Пример ответа',
                value={"id": 1, "content": "Купить продукты", "completed": False, "created_at": "2025-18-09T10:00:00Z"}
            )
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить задачу полностью",
        description="Заменяет все поля задачи новыми данными.",
        request=TaskSerializer,
        responses={
            200: TaskSerializer,
            400: OpenApiResponse(description="Неверные данные"),
            404: OpenApiResponse(description="Задача не найдена"),
        }, 
        examples=[
            OpenApiExample(
                'Пример запроса',
                value={"content": "Обновленная задача", "completed": True}
            ),
            OpenApiExample(
                'Пример ответа',
                value={"id": 1, "content": "Обновленная задача", "completed": True, "created_at": "2025-18-09T10:00:00Z"}
            )
        ]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить задачу частично",
        description="Обновляет только указанные поля задачи.",
        request=TaskSerializer(partial=True),
        responses={
            200: TaskSerializer,
            400: OpenApiResponse(description="Неверные данные"),
            404: OpenApiResponse(description="Задача не найдена"),
        }, 
        examples=[
            OpenApiExample(
                'Пример запроса',
                value={"completed": True}
            ),
            OpenApiExample(
                'Пример ответа',
                value={"id": 1, "content": "Купить продукты", "completed": True, "created_at": "2025-18-09T10:00:00Z"}
            )
        ]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить задачу",
        description="Удаляет задачу по ID.",
        responses={
            204: OpenApiResponse(description="Задача удалена"),
            401: OpenApiResponse(description="Неавторизован"),
            404: OpenApiResponse(description="Задача не найдена"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)