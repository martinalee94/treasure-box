from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models

from apps.cores.models import DeleteModel, TimeStampModel

# class CustomUserManager(BaseUserManager):
#     use_in_migrations = True

#     def create_user(self, username, uid, provider, **extra_fields):
#         if not username or not uid or not provider:
#             raise ValueError("가입 필수 항목이 부정확합니다.")

#         # extra_fields.setdefault("is_superuser", False)
#         user = self.model(username=username, uid=uid, provider=provider, **extra_fields)
#         user.save()
#         return user

#     def create_superuser(self, username, password, **extra_fields):
#         if not username or not password:
#             raise ValueError("관리자 가입 필수 항목이 부정확합니다.")

#         extra_fields.setdefault("uid", "admin")
#         extra_fields.setdefault("provider", "admin")
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("nickname", "admin")
#         superuser = self.model(username=username, **extra_fields)
#         superuser.set_password(password)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#         superuser.save()
#         return superuser


# class Member(PermissionsMixin, DeleteModel, TimeStampModel):
#     """
#     - PermissionsMixin : is_superuser, groups, user_permissions
#     - TimeStampModel : created_at, modified_at
#     - DeleteModel : is_deleted, deleted_at
#     """

#     username = models.CharField(max_length=50)
#     uid = models.CharField(max_length=256)
#     provider = models.CharField(max_length=30)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()
#     USERNAME_FIELD = "username"
# REQUIRED_FIELDS = ["username", "uid", "provider"]

# class Meta:
#     db_table = "member"
