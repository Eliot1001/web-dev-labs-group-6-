from django.db.utils import OperationalError, ProgrammingError
from django.shortcuts import render

from .models import Proposal, Review, User


def home(request):
    stats = {
        "users": 0,
        "proposals": 0,
        "reviews": 0,
    }
    recent_proposals = []

    try:
        stats = {
            "users": User.objects.count(),
            "proposals": Proposal.objects.count(),
            "reviews": Review.objects.count(),
        }
        recent_proposals = Proposal.objects.select_related("user").order_by("-submission")[:5]
    except (OperationalError, ProgrammingError):
        pass

    context = {
        "stats": stats,
        "recent_proposals": recent_proposals,
    }
    return render(request, "pop_system/home.html", context)


def proposal_list(request):
    proposals = []

    try:
        proposals = Proposal.objects.select_related("user").order_by("-submission")
    except (OperationalError, ProgrammingError):
        pass

    return render(request, "pop_system/proposal_list.html", {"proposals": proposals})
