from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("lecturer", "Lecturer"),
        ("admin", "Admin"),
    ]

    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.full_name


class Proposal(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("under_review", "Under Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    proposal_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    submission = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proposals", db_column="user_id")

    def __str__(self):
        return self.title


class Reviewer(models.Model):
    reviewer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name="reviews", db_column="proposal_id")
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name="reviews", db_column="reviewer_id")
    comments = models.TextField(blank=True, null=True)
    score = models.PositiveSmallIntegerField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.review_id} for {self.proposal.title}"


class Approval(models.Model):
    approval_id = models.AutoField(primary_key=True)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name="approvals", db_column="proposal_id")
    approved_by = models.CharField(max_length=255)
    approval_date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Approval {self.approval_id} for {self.proposal.title}"
