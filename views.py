from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.contrib.auth.decorators import login_required

from models import IndexSection, IndexApp, IndexCustom


@login_required
def custom_admin_index(request):
    context = {}
    context['app_list'] = IndexSection.objects.all()
    return render_to_response('admin/custom_index.html',context_instance=RequestContext(request, context))    
