from django.urls import path

# views
from docket.api.views import (
    ProjectViewSet,
    EmailTokenObtainPairView,
    RegisterUser,
    RequestPasswordResetEmail,
    PasswordTokenCheckAPI,
    SetNewPasswordAPIView,
)

# views
from docket.api.views import (
    ProjectViewSet,
    EmailTokenObtainPairView,
    TaskViewSet,
    TaskCommentViewSet,
    BoardViewSet,
    BoardTaskViewSet,
    SubTaskViewSet,
    UserPermissionViewSet,
    TeamViewSet
)

# token
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("token/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Register
    path(
        "register/",
        RegisterUser.as_view(),
        name="register",
    ),
    # forgot password
    path(
        "request-reset-email/",
        RequestPasswordResetEmail.as_view(),
        name="request-reset-email",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordTokenCheckAPI.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "password-reset-complete",
        SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
    # task
    path("tasks/", TaskViewSet.as_view({"post": "create"}), name="task_create"),
    path(
        "tasks/<int:pk>/",
        TaskViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="task_info",
    ),
    # task comments
    path(
        "tasks/<int:task_id>/comments/",
        TaskCommentViewSet.as_view(
            {"post": "create"}
        ),
        name="task_comment_create",
    ),
     path(
        "tasks/comments/<int:pk>/",
        TaskCommentViewSet.as_view(
            {"get": "retrieve","put": "update", "delete": "destroy"}
        ),
        name="task_comment_info",
    ),
    # Sub Tasks
    path(
        "tasks/<int:task_id>/subtasks/",
        SubTaskViewSet.as_view(
            {"post": "create"}
        ),
        name="subtask_create",
    ),
    path(
        "tasks/subtasks/<int:pk>/",
        SubTaskViewSet.as_view(
            {"get": "retrieve","put": "update", "delete": "destroy"}
        ),
        name="subtask_info",
    ),
    # task assignee
    # path(
    #     "tasks/<int:task_id>/comments/",
    #     TaskCommentViewSet.as_view(
    #         {"post": "create", "put": "update", "delete": "destroy"}
    #     ),
    #     name="task_info",
    # ),
    # # projects
    path(
        "projects/",
        ProjectViewSet.as_view({"get": "list", "post": "create"}),
        name="projects_list",
    ),
    path(
        "projects/<int:pk>/",
        ProjectViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="projects_info",
    ),
    # Boards
    path(
        "boards/",
        BoardViewSet.as_view({"post": "create"}),
        name="board_create",
    ),
    path(
        "boards/<int:pk>/",
        BoardViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="projects_info",
    ),
    path(
        "boards/<int:pk>/tasks/",
        BoardTaskViewSet.as_view({"post": "create", "put": "update"}),
    ),
    # User Permission
    path(
        "user_permission/",
        UserPermissionViewSet.as_view(
            {"post":"create"}
        ),
        name="user_permission",
    ),
    # Team
    path(
        "team/",
        TeamViewSet.as_view(
            {"post":"create", "put": "update", "delete": "destroy"}
        ),
        name="user_permission",
    ),  
]