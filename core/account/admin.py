# from django.contrib import admin
# from .models import *
# from rangefilter.filters import DateRangeFilter

# class LastNameFilter(admin.SimpleListFilter):
#     template = 'input_filter.html'
#     parameter_name = 'last_name'

#     def lookups(self, request, model_admin):
#         return ((),)

#     def choices(self, changelist):
#         all_choice = next(super().choices(changelist))
#         all_choice['query_parts'] = (
#             (k, v)
#             for k, v in changelist.get_filters_params().items()
#             if k != self.parameter_name
#         )
#         yield all_choice

#     def queryset(self, request, queryset):
#         if self.value() is not None:
#             last_name = self.value()
#             return queryset.filter(last_name__contains=last_name)


# class FirstNameFilter(admin.SimpleListFilter):
#     template = 'input_filter.html'
#     parameter_name = 'first_name'

#     def lookups(self, request, model_admin):
#         return ((),)

#     def choices(self, changelist):
#         all_choice = next(super().choices(changelist))
#         all_choice['query_parts'] = (
#             (k, v)
#             for k, v in changelist.get_filters_params().items()
#             if k != self.parameter_name
#         )
#         yield all_choice

#     def queryset(self, request, queryset):
#         if self.value() is not None:
#             first_name = self.value()
#             return queryset.filter(first_name__contains=first_name)


# # Register your models here.

# @admin.register(UserInfo)
# class UserInfoModelAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name', 'national_id', 'birth_date', 'created_at')
#     list_display = ['first_name', 'last_name', 'national_id', 'birth_date', 'created_at']
#     list_filter = (
#         ('created_at', DateRangeFilter),
#         LastNameFilter,
#         FirstNameFilter,
#     )