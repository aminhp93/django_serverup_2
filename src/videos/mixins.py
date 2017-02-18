from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator

class MemberRequiredMixin(object):
	def dispatch(self, request, *args, **kwargs):
		print("requiring??")
		obj = self.get_object()
		if request.user.is_staff:
			return super().dispatch(request, *args, **kwargs)			
		if obj.free:
			return super().dispatch(request, *args, **kwargs)
		return HttpResponse("not free")

class StaffMemberRequiredMixin(object):
	
	@method_decorator(staff_member_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)