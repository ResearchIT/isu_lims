from django.shortcuts import render
from iastatetheme.models import SiteTheme
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'lims/index.html')

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


from .models import Subgenus

def subgenera(request):
    subgenera_list = Subgenus.objects.all()
    context = {'subgenera_list': subgenera_list,
    }

    return render(request, 'subgenera/index.html', context)

from .models import Genome

def genome(request):
    genome_list = Genome.objects.all()
    context = {'genome_list': genome_list,
    }

    return render(request, 'genome/index.html', context)


from .models import Species

def species(request):
    species_list = Species.objects.all()
    context = {'species_list': species_list,
    }

    return render(request, 'species/index.html', context)

from .models import Accession

def accession(request):
    accession_list = Accession.objects.all()
    context = {'accession_list': accession_list,
    }

    return render(request, 'accession/index.html', context)

from .models import Plant

def plant(request):
    plant_list = Plant.objects.all()
    context = {'plant_list': plant_list,
    }

    return render(request, 'plant/index.html', context)

from .models import SeedPacket

def seedpacket(request):
    seedpacket_list = SeedPacket.objects.all()
    context = {'seedpacket_list': seedpacket_list,
    }

    return render(request, 'seedpacket/index.html', context)

from .models import Seed

def seed(request):
    seed_list = Seed.objects.all()
    context = {'seed_list': seed_list,
    }

    return render(request, 'seed/index.html', context)

from .models import Project

def project(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list,
    }

    return render(request, 'project/index.html', context)

from .models import Sample

def sample(request):
    sample_list = Sample.objects.all()
    context = {'sample_list': sample_list,
    }

    return render(request, 'sample/index.html', context)


from .forms import NewSeedPacketForm
def newseedpacket(request):
    if request.method == 'POST':
        form = NewSeedPacketForm(request.POST)
        if form.is_valid():
            seedpacket = form.save()
            return HttpResponseRedirect('seedpacket/new')
    else:
        form = NewSeedPacketForm()
    return render(request, 'seedpacket/newseedpacketform.html', {'form': form})
