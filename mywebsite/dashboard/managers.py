from django.db.models import QuerySet
from django.db.models import aggregates, expressions

class DashboardManager(QuerySet):
    def sum_of_likes(self):
        celebrities = self.all()
        return celebrities.aggregate(aggregates.Sum('likes'))
