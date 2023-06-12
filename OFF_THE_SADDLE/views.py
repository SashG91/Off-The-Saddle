from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Climb, RideTime, Comment
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.views.generic import DeleteView, UpdateView

from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm, EditForm
from django.contrib.messages.views import SuccessMessageMixin


class ClimbList(generic.ListView):
    """
    A view to render all blog posts in a paginated list.
    Renders information from the climb model.
    Forms the main page of the website.
    """
    model = Climb
    queryset = Climb.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ClimbDetail(SuccessMessageMixin, View):
    """
    A view to render the details of each blog post.
    Renders further information from the climb model.
    Includes get and post methods for commenting.
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
    """
    A view to add likes to each climb.
    If clicked, users are directed to the original page.
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Climb, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('climb_detail', args=[slug]))


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to allow users to delete a ride contribution.
    Ensures the user logged in is the owner of the comment.
    Prompts user before deletion, confirms if deleted.
    Redirects to the original ride post.
    """
    model = Comment
    template_name = "delete_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user.username == comment.name

    def delete(self, request, *args, **kwargs):
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        climb_slug = self.object.post.slug
        # ClimbDetail.comment_deleted = True
        messages.success(self.request, 'Your comment has been deleted.')
        return reverse("climb_detail", kwargs={"slug": climb_slug})


class Page403(TemplateView):
    template_name = '403.html'


class Page404(TemplateView):
    template_name = '404.html'


class Page500(TemplateView):
    template_name = '500.html'
