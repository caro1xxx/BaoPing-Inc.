from main import models
from django.db.models import F


class DomainOp:
    def addVisitCount(self, domainObj):
        # domainObj.update(visit_count=F('visit_count')+1)
        domainObj.visit_count = F('visit_count') + 1
        domainObj.save()
        