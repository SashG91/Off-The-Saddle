from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Climb, RideTime, Comment
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import DeleteView, UpdateView
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView


from .forms import CommentForm, EditForm

from django.contrib.messages.views import SuccessMessageMixin


class ClimbList(generic.ListView):
    """
    A view to render all blog posts in a paginated list.
    Renders information from the climb model.
    """
    model = Climb
    queryset = Climb.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ClimbDetail(SuccessMessageMixin, View):
    """
    A view to render the details of each blog post.
    Renders further information from the climb model.
    """
    model = Climb
    template_name = 'climb_detail.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = Climb.objects.filter(status=1)
        climb = get_object_or_404(queryset, slug=slug)
        comments = climb.comments.filter(approved=True).order_by('created_on')
        liked = False
        if climb.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "climb_detail.html",
            {
                "climb": climb,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Climb.objects.filter(status=1)
        climb = get_object_or_404(queryset, slug=slug)
        comments = climb.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if climb.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = climb
            comment.save()
            messages.success(request,
                             'Your comment has been uploaded for approval.')
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "climb_detail.html",
            {
                "climb": climb,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Climb, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('climb_detail', args=[slug]))

# class AddClimbTime(CreateView): 
#     """
#     Create Climb Time View
#     """
#     model = RideTime
#     fields = ['time']
#     template_name = 'add_climb.html'


class Page403(TemplateView):
    template_name = '403.html'


class Page404(TemplateView):
    template_name = '404.html'


class Page500(TemplateView):
    template_name = '500.html'
