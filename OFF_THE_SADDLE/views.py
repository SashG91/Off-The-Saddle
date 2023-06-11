from django.shortcuts import render
from django.views import generic
from .models import Climb


class ClimbList(generic.ListView):
    model = Climb
    queryset = Climb.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ClimbDetail(SuccessMessageMixin, View):

    def get(self, request, slug, *args, **kwargs):
        model = Climb
        queryset = Plant.objects.filter(status=1)
        template_name = 'index.html'
        climb = get_object_or_404(queryset, slug=slug)
        comments = plant.comments.filter(approved=True).order_by('created_on')
        liked = False
        if climb.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "climb": climbt,
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
                             'Your comment has been uploaded for admin approval.')
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "climb": plant,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )