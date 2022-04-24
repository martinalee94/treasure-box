from django.contrib.auth.models import User
from django.db import models

from apps.cores.models import DeleteModel, TimeStampModel


class Member(DeleteModel, TimeStampModel):
    """
    - PermissionsMixin : is_superuser, groups, user_permissions
    - TimeStampModel : created_at, modified_at
    - DeleteModel : is_deleted, deleted_at
    """

    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="social_name")  # type: ignore

    class Meta:
        db_table = "member"
