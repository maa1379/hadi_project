# from django.contrib.auth import get_user_model
# from django.utils import timezone
#
# user=get_user_model()
#
#
# class UpdateLastActivityMiddleware(object):
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         assert hasattr(request, 'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
#         if request.user.is_authenticated():
#             user.objects.filter(user__id=request.user.id) \
#                            .update(last_activity=timezone.now())
#
#
# MIDDLEWARE_CLASSES = (
#     # other middlewares
#     'myproject.profiles.middleware.UpdateLastActivityMiddleware',
# )