from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "ervin/home.html"

class ProfileView(TemplateView):

    template_name = 'ervin/profile.html'
