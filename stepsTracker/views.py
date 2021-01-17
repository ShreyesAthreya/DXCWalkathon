from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView

# Create your views here.
from .forms import CreateStepsForm, UpdateStepForm
from .models import Step


# def home(request):
#     return render(request, 'stepsTracker/index.html')


# class CreateStepsView(CreateView):
#     model = Step
#     template_name = 'stepsTracker/createSteps.html'
#     # fields = "__all__"
#     form_class = CreateStepsForm
#
#     def form_valid(self, form):
#         profile = form.save(commit=False)
#         profile.user = self.request.user
#         profile.save()


def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        my_list = [first_name, last_name, username, password1, password2]

        if '' in my_list:
            return render(request, 'stepsTracker/register.html', {'error': 'Fields can\'t be blank'})

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password1)
                user.save()
                messages.success(request, "You have registered successfully!")
                login(request, user)
                return redirect("add-steps")
            except ValueError:
                return render(request, 'stepsTracker/register.html', {'error': 'Username can\'t be blank'})

            except IntegrityError:
                return render(request, 'stepsTracker/register.html',
                              {'error': 'Username already taken. Please choose another one'})
        else:
            return render(request, 'stepsTracker/register.html', {'error': 'Password did not match'})

    else:
        return render(request, 'stepsTracker/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            login(request, user)
            ifUserSteps = Step.objects.filter(user=user.id).values()
            if ifUserSteps:
                return redirect("home")
            else:
                return redirect("add-steps")
        else:
            messages.error(request, "Unable to verify username and password")
            return redirect('signin')

    return render(request, 'stepsTracker/signin.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("/")


def addSteps(request):
    form = CreateStepsForm()

    if request.method == 'POST':
        request.POST = request.POST.copy()
        form = CreateStepsForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "You have added your steps successfully!")
        return redirect("home")

    context = {'form': form}
    return render(request, 'stepsTracker/createSteps.html', context)


class HomeView(ListView):
    model = Step
    template_name = 'stepsTracker/index.html'
    ordering = ['-steps']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Step.objects.all()
        try:
            context['totalSteps'] = float(list(Step.objects.aggregate(Sum('steps')).values())[0])
            context['remaining'] = 7966 - context['totalSteps']
        except:
            context[
                'openingMessage'] = "So I thought as I sipped a few glasses of wine over Christmas, " \
                                    "I think we should walk from Ireland to India. Sure, why not!!!. " \
                                    "This January, the Irish Early Careers team is going to walk from Ireland to India, " \
                                    "which is only 7,996 km!. It is a big personal challenge for all of us, but we are ready - " \
                                    "bring it on!!. A good starting point is to get yourself registered first. " \
                                    "\n \n \n" \
                                    "Click on the 'Sign Up' button at the top of the page if you haven't already." \
                                    "\n \tClick on Sign in to register your steps."
        return context


class StepDetailView(DetailView):
    model = Step
    template_name = 'stepsTracker/viewSteps.html'


class UpdateStepView(UpdateView):
    model = Step
    template_name = 'stepsTracker/updateSteps.html'
    form_class = UpdateStepForm
