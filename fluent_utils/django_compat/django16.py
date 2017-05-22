import django
from django.db import transaction

# New transaction support in Django 1.6
try:
    transaction_atomic = transaction.atomic
except AttributeError:
    transaction_atomic = transaction.commit_on_success


# Preserving admin form filters when adding parameters to the URL
try:
    # Django 1.6 supports this, and django-parler also applies this fix.
    from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
except ImportError:
    # Django <1.6 does not preserve filters
    def add_preserved_filters(context, form_url):
        return form_url

if django.VERSION >= (1, 6):
    def is_queryset_empty(queryset):
        """
        Check whether a queryset is empty by using ``.none()``.
        """
        return queryset.query.is_empty()
else:
    from django.db.models.query import EmptyQuerySet

    def is_queryset_empty(queryset):
        return isinstance(queryset, EmptyQuerySet)
