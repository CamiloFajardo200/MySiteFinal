from django.urls import reverse_lazy, reverse
from review.forms import ReviewForm
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponseRedirect(reverse('blog-about'))
