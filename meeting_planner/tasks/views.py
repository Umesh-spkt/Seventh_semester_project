from django.shortcuts import render, get_object_or_404, redirect

from .models import Task, Student
from .forms import TaskForm


def detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, "tasks/detail.html", {"task": task})


def students_list(request):
    return render(request, "tasks/students_list.html",
            {"students": Student.objects.all()})


def new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = TaskForm()
    return render(request, "tasks/new.html", {"form": form})


# As a bonus, here are example implementations
# Of an edit and delete form
# See also urls.py and templates

def edit(request, id):
    # First, get the meeting to edit from the database
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        # After editing: get data from form
        # Note the second argument: the meeting we are editing
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # redirect back to detail page after save
            return redirect("detail", id)
    else:
        # Pre-fill the form with data from existing meeting
        form = TaskForm(instance=task)
    return render(request, "tasks/edit.html", {"form": form})


# Delete is different: the form is only shown to ask for confirmation
# When we get a POST, we know we can go ahead and delete
def delete(request, id):
    # First, get the meeting to edit from the database
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        task.delete()
        return redirect("welcome")
    else:
        return render(request, "tasks/confirm_delete.html", {"task": task})