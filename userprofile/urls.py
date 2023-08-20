from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProfileSettings.as_view(), name="profile-setting" ),
    path("userlist/", views.UserList.as_view(), name="user-list"),
    path("delete-bank/<int:pk>", views.delete_bank_account, name="delete-bank"),
    path("change-password/", views.change_password, name="change-passowrd"),
    path("transactions/", views.Transactions.as_view(), name="user-details"),
    path("userlist/accout-operation/", views.user_active_inactive, name="active-inactive"),
    path("transaction/<int:pk>/", views.payment_admin_view, name="admin-panel" ),
    path("update-payment-status/<int:pk>", views.update_payment_status, name="update_payment_status"),
    path("task-view/", views.HandleTask.as_view(), name="task-view"),
]   