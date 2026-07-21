from rest_framework.permissions import BasePermission
from .models import Profile

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                if request.user.profile.role == Profile.Roles.DOCTOR:
                    return True
                else:
                    return False
            except Exception:
                return False
        else:
            return False