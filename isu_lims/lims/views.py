from django.shortcuts import render
from iastatetheme.models import SiteTheme
from django.views.generic.detail import DetailView




def index(request):
    return render(request, 'lims/index.html')

def thanks(request):
    return render(request, 'lims/thanks.html')

from .models import Genus

def genera(request):
    genera_list = Genus.objects.all()
    context = {'genera_list': genera_list,
    }

    return render(request, 'genera/index.html', context)

from django.views.generic import DetailView
from .models import Genus, Subgenus

class GenusDetailView(DetailView):

    model = Genus

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the genera
        context['genera_list'] = Genus.objects.all()
        return context

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'forms/name.html', {'form': form})

from .models import Subgenus

def subgenera(request):
    subgenera_list = Subgenus.objects.all()
    context = {'subgenera_list': subgenera_list,
    }

    return render(request, 'subgenera/index.html', context)

from django.views.generic import DetailView
from .models import Genus, Subgenus

class SubgenusDetailView(DetailView):

    model = Subgenus

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the subgenera
        context['subgenera_list'] = Subgenus.objects.all()
        return context

from .models import Genome

def genome(request):
    genome_list = Genome.objects.all()
    context = {'genome_list': genome_list,
    }

    return render(request, 'genome/index.html', context)

from django.views.generic import DetailView
from .models import Genus, Subgenus, Genome

class GenomeDetailView(DetailView):

    model = Genome

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the genome
        context['genome_list'] = Genome.objects.all()
        return context


from .models import Species

def species(request):
    species_list = Species.objects.all()
    context = {'species_list': species_list,
    }

    return render(request, 'species/index.html', context)

from django.views.generic import DetailView
from .models import Genus, Subgenus, Genome, Species

class SpeciesDetailView(DetailView):

    model = Species

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the genome
        context['species_list'] = Species.objects.all()
        return context

from .models import Accession

def accession(request):
    accession_list = Accession.objects.all()
    context = {'accession_list': accession_list,
    }

    return render(request, 'accession/index.html', context)

from django.views.generic import DetailView
from .models import Genus, Subgenus, Genome, Species, Accession

class AccessionDetailView(DetailView):

    model = Accession

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the accessions
        context['accession_list'] = Accession.objects.all()
        return context

from .models import Plant

def plant(request):
    plant_list = Plant.objects.all()
    context = {'plant_list': plant_list,
    }

    return render(request, 'plant/index.html', context)

from django.views.generic import DetailView
from .models import Genus, Subgenus, Genome, Species, Accession, Plant

class PlantDetailView(DetailView):

    model = Plant

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the plants
        context['plant_list'] = Plant.objects.all()
        return context

from .models import SeedPacket

def seedpacket(request):
    seedpacket_list = SeedPacket.objects.all()
    context = {'seedpacket_list': seedpacket_list,
    }

    return render(request, 'seedpacket/index.html', context)

from .models import Seed

from django.views.generic import DetailView
from .models import Genus, Subgenus, Genome, Species, Accession, Plant, SeedPacket

class SeedPacketDetailView(DetailView):

    model = SeedPacket

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the seed packets
        context['seedpacket_list'] = SeedPacket.objects.all()
        return context


def seed(request):
    seed_list = Seed.objects.all()
    context = {'seed_list': seed_list,
    }

    return render(request, 'seed/index.html', context)

class SeedDetailView(DetailView):

    model = Seed

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the seed packets
        context['seed_list'] = Seed.objects.all()
        return context

from .models import Project

def project(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list,
    }

    return render(request, 'project/index.html', context)

class ProjectDetailView(DetailView):

    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the seed packets
        context['project_list'] = Project.objects.all()
        return context

from .models import Sample

def sample(request):
    sample_list = Sample.objects.all()
    context = {'sample_list': sample_list,
    }

    return render(request, 'sample/index.html', context)
    
class SampleDetailView(DetailView):

    model = Sample

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the samples
        context['sample_list'] = Sample.objects.all()
        return context