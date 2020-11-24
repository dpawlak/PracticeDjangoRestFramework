from .models import Post

# Count number of traumas
def counter(request):
    trauma_count = Post.objects.filter(tags__name="Trauma").count()
    return {"trauma_count" : trauma_count}


        