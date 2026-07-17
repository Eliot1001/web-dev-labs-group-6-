from django.contrib import admin

from .models import Approval, Proposal, Review, Reviewer, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "full_name", "email", "role")
    list_filter = ("role",)
    search_fields = ("full_name", "email")


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ("proposal_id", "title", "user", "status", "submission")
    list_filter = ("status",)
    search_fields = ("title", "description")


@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ("reviewer_id", "full_name", "email")
    search_fields = ("full_name", "email")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("review_id", "proposal", "reviewer", "score", "review_date")
    list_filter = ("score",)


@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ("approval_id", "proposal", "approved_by", "approval_date")
