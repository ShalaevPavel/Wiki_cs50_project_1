from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from markdown2 import Markdown
from django.urls import reverse
from . import util
from . import forms


def index(request):
    if request.method == "POST":
        written = request.POST["written"]
        if written in util.list_entries():
            return HttpResponseRedirect(reverse("title", args=(written,)))
        else:
            return HttpResponseRedirect(reverse("search", args=(written,)))
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_by_title(request, name_of_title):
    markdowner = Markdown()
    return render(request, "encyclopedia/get_title.html", {"entry": markdowner.convert(util.get_entry(name_of_title))

                                                           })


def create_entry2(request):
    if request.method == 'POST':
        form = forms.Creatioal_form(request.POST)
        if form.is_valid():
            if form.cleaned_data["entry_name"] in util.list_entries():
                return HttpResponse("Already exists!")
            else:
                util.save_entry(form.cleaned_data["entry_name"], form.cleaned_data["content_instance"])
                return HttpResponseRedirect(reverse("title", args=(form.cleaned_data["entry_name"],)))
    return render(request, "encyclopedia/create.html", {'form': forms.Creatioal_form()})


def search_for_entry(request):
    if request.method == "GET":
        form = forms.Search_form(request.GET)

        if form.cleaned_data["input_data"] in util.list_entries():
            return HttpResponseRedirect(reverse("title", args=(form.cleaned_data["input_data"])))

        for entry_name in util.list_entries():
            if form.cleaned_data["input_data"] in entry_name:
                return HttpResponseRedirect(reverse("title", args=(entry_name,)))
    return render(request, "encyclopedia/layout.html", {"search_form": forms.Search_form()})


#
# def edit_entry(request, name_of_entry_to_edit):
#     list_entris = util.list_entries()
#     return render(request, "encyclopedia/edit.html", {"list": list_entris})


def edit_entry(request, entry):
    if request.method == 'POST':
        form = forms.Search_form(request.POST)
        if form.is_valid():
            util.save_entry(entry, form.cleaned_data["input_data"])
            return HttpResponseRedirect(reverse("title", args=(entry,)))
    return render(request, "encyclopedia/edit.html", {'form': forms.Search_form()})


def search_results(request, substring):
    list_of_entries = util.list_entries()

    return render(request, "encyclopedia/search_results.html", {"entries": list_of_entries,
                                                                "search_text": substring})
