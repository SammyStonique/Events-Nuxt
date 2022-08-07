from rest_framework import permissions


class IsProfileOwner(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and obj.author == request.user