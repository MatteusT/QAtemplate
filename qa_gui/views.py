from django.shortcuts import render
from django.views import View
from qa_gui.code import get_contexts, get_answer

from .forms import SearchForm


N_PARAGRAPHS = 3


class SearchFormView(View):

    def get(self, request):
        form = SearchForm()
        context = {'form': form}
        return render(request, 'searchform.html', context)

    def post(self, request):
        form = SearchForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            paragraphs = get_contexts(form.cleaned_data["question"], n_paragraphs=N_PARAGRAPHS)
            answers = []
            for paragraph in paragraphs:
                answer = get_answer(form.cleaned_data["question"], paragraph)
                answers.append({
                    "answer": answer,
                    "context": paragraph
                })
            context["answers"] = answers
        return render(request, 'searchform.html', context)
