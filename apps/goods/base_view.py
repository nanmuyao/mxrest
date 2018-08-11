# _*_ coding:utf-8 _*_
__author__ = 'tars'
_date__ = '2018/7/29 10:03'

from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# class MyView(LoginRequiredMixin, ...):
#     # this is a generic view
#     ...

#
# class goods(View):
#
#     @method_decorator(login_required)
#     def get(self, request):
#         return HttpResponse('success')
#
#
#
