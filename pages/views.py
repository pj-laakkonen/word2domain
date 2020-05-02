from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class W2DPageView(TemplateView):
    template_name = 'pages/w2d.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


    # def post(self, a):
    #     # if this is a POST request we need to process the form data
    #     if self.request.method == 'POST':
    #         # create a form instance and populate it with data from the request:
    #         form = NameForm(self.request.POST)
    #         # check whether it's valid:
    #         if form.is_valid():
    #             # process the data in form.cleaned_data as required
    #             # ...
    #             # redirect to a new URL:
    #             # return render(self.request, 'pages/name.html', {'form': form})
    #             return HttpResponseRedirect('/about/')
    #
    #     # if a GET (or any other method) we'll create a blank form
    #     else:
    #         form = NameForm()
    #
    #     return render(self.request, 'pages/name.html', {'form': form})

