from typing import Any
from django.views.generic import DetailView
from django.shortcuts import redirect, render, get_object_or_404
from .models import Menu
from .functions import get_menu_tree


class MenuDetail(DetailView):
    model = Menu
    template_name = 'default.html'
    context_object_name = 'menu'
    slug_field = 'slug'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['menu_tree'], context['menu_indents'], context['menu_path'] \
            = get_menu_tree(context['menu'])
        return context
        
    def get_object(self):
        return get_object_or_404(Menu, slug=self.kwargs['slug'])
    
    
def home_view(request):
    home_menu = Menu.objects.get(nesting_level=0)
    context = {}
    context['menu_tree'], context['menu_indents'] = get_menu_tree(home_menu)[:2]
    return render(request, 'default.html', context)
