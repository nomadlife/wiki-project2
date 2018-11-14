from django.conf import settings
from django.http import HttpResponseServerError
from django.template import loader
from django.template.context import RequestContext
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render
from django.utils.decorators import method_decorator
from wiki.views.article import ArticleView
from wiki.models.article import Article
from wiki.decorators import get_article

from django.http import HttpResponse

##
from wiki.views.mixins import ArticleMixin

@requires_csrf_token
def server_error(request, template_name='500.html', **param_dict):
    # You need to create a 500.html template.
    t = loader.get_template(template_name)
    return HttpResponseServerError(t.render(RequestContext(
        request,
        {
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL,
            'request': request,
        },
    )))


def page_not_found(request, template_name='404.html', exception=None):
    response = server_error(
        request,
        template_name=template_name,
        exception=exception
    )
    response.status_code = 404
    return response

def hello_fn(request, name="World"):
    return HttpResponse("Hello {}!".format(name))

from django.views.generic import View
class HelloView(View):
    def get(self, request, name="World"):
        return HttpResponse("Hello {}!!".format(name))

class GreetView(View):
    greeting = "Hello {}!!!"
    default_name = "World"
    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))
        
class SuperVillainView(GreetView):
    greeting = "We are the future, {}. Not them. "
    default_name = "my friend"


def myhome(request):
    return render(request, 'base.html', {'title':'HOME'})  

def test1(request):
    return render(request, 'wiki/test1.html', {'wiki_pagetitle':'pagetitle', 'string':'param test'})  

def test2(request):
    return render(request, 'wiki/test2.html', {'title':'Test'})  

class WikiListView(ArticleView):
    template_name = 'test3.html'
    # model = Article
    # revision = current_revision
#     date = created
    # context_object_name = 'posts'
    # ordering = ['-date_posted']
    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['path'] = ''
        return ArticleMixin.get_context_data(self, **kwargs)