from django.shortcuts import render, get_object_or_404

from .models import TutorialModel

def homeIndex(request):
    return render(request, 'index.html', {'tutorials':TutorialModel.objects.all()})


def tutorialIndex(request, slug, pk):
    # print(slug, 'slug')
    # print(dir(TutorialModel))
    tutorial = get_object_or_404(TutorialModel, pk=pk)
    print(tutorial, tutorial.body)
    return render(request, 'single.html', {'tutorial':tutorial, 'tutorials':TutorialModel.objects.all()})