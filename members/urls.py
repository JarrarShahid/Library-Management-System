from django.urls import path
from .views import add_members_view, get_member_view, update_member_view,search_members,members_preview,delete_member_view


urlpatterns = [
    path('add-member',add_members_view,name="addMember"),
    path('get-member/<str:memberID>/', get_member_view, name='get-member'),
    path('update-member',update_member_view, name='updateMember'),
    path("search_members/",search_members, name="search_members"),
    path("members-preview/",members_preview, name="members_preview"),
    path('delete-member',delete_member_view,name="deleteMember"),
]