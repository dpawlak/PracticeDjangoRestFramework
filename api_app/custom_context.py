from .models import Post

# Count number of traumas
def trauma_counter(request):
    trauma_count = Post.objects.filter(tags__name="Trauma").count()
    return {"trauma_count" : trauma_count}

# Count number of pediatrics
def pediatric_counter(request):
    pediatrics_count = Post.objects.filter(tags__name="Pediatrics").count()
    return {"pediatrics_count" : pediatrics_count}

# Count number of optometries
def optometry_counter(request):
    optometry_count = Post.objects.filter(tags__name="Optometry").count()
    return {"optometry_count" : optometry_count}

# Count number of neurologies
def nuerology_counter(request):
    nuerology_count = Post.objects.filter(tags__name="Nuerology").count()
    return {"nuerology_count" : nuerology_count}

# Count number of psychiatrics
def psychiatry_counter(request):
    psychiatry_count = Post.objects.filter(tags__name="Psychiatry").count()
    return {"psychiatry_count" : psychiatry_count}

    
