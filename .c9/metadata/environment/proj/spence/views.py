{"filter":false,"title":"views.py","tooltip":"/proj/spence/views.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":29},"end":{"row":13,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"21ff585b365bb821692ac7021ad81c3ae100f5b9","undoManager":{"mark":91,"position":91,"stack":[[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":6,"column":50},"action":"insert","lines":["from django.http import HttpResponse","# Create your views here.","def index(request):","return HttpResponse(\"You're at the movies index.\")"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":4}],[{"start":{"row":5,"column":18},"end":{"row":6,"column":0},"action":"remove","lines":[":",""],"id":6}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":[":"],"id":7}],[{"start":{"row":5,"column":19},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"remove","lines":["s"],"id":9},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"remove","lines":["e"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":["i"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["v"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["o"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["m"]}],[{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["s"],"id":10},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["p"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["e"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":["n"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["c"]},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":8,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["from django.shortcuts import render","from .models import Movie","","def index(request):","    newest_movies = Movie.objects.order_by('-release_date')[:15]","    context = {'newest_movies': newest_movies}","    return render(request, 'movies/index.html', context)",""],"id":12}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["e"],"id":13},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["i"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["v"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["o"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["M"]}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["S"],"id":14},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["p"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["e"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["n"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["c"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":["e"],"id":15},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["i"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":["v"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["o"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["M"]}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["S"],"id":16},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["p"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["e"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["n"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["c"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"remove","lines":["s"],"id":17},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"remove","lines":["e"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"remove","lines":["i"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"remove","lines":["v"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"remove","lines":["o"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"remove","lines":["m"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["i"],"id":18},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["t"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"remove","lines":["e"],"id":19},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"remove","lines":["t"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"remove","lines":["i"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["p"],"id":20},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["a"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["n"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["t"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["r"]},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["y"]}],[{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["s"],"id":21},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["e"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["i"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["v"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["o"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["m"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["p"],"id":22},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["a"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["n"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["t"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["r"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["y"]}],[{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"remove","lines":["s"],"id":23},{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"remove","lines":["e"]},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"remove","lines":["i"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"remove","lines":["v"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"remove","lines":["o"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"remove","lines":["m"]}],[{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"insert","lines":["p"],"id":24},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":["a"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"insert","lines":["n"]},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"insert","lines":["t"]},{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"insert","lines":["r"]},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"insert","lines":["y"]}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["s"],"id":25},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["i"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["v"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["o"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["m"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["s"],"id":26},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["p"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["n"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["c"]}],[{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["c"],"id":27},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["n"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["e"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["p"],"id":28},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["n"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["c"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":34},"action":"remove","lines":["spence"],"id":29},{"start":{"row":14,"column":28},"end":{"row":14,"column":35},"action":"insert","lines":["spence/"]}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["/"],"id":30}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "],"id":31},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["S"],"id":32}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["s"],"id":33}],[{"start":{"row":12,"column":20},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":6},"action":"insert","lines":["# "],"id":36}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["s"],"id":37},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["p"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["e"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["n"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["c"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["."],"id":38},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["o"]},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":["b"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"insert","lines":["j"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":["e"]},{"start":{"row":12,"column":31},"end":{"row":12,"column":32},"action":"insert","lines":["c"]},{"start":{"row":12,"column":32},"end":{"row":12,"column":33},"action":"insert","lines":["t"]},{"start":{"row":12,"column":33},"end":{"row":12,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":33},"end":{"row":12,"column":34},"action":"remove","lines":["s"],"id":39},{"start":{"row":12,"column":32},"end":{"row":12,"column":33},"action":"remove","lines":["t"]},{"start":{"row":12,"column":31},"end":{"row":12,"column":32},"action":"remove","lines":["c"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"remove","lines":["e"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"remove","lines":["j"]},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"remove","lines":["b"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"remove","lines":["o"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"remove","lines":["."]}],[{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"remove","lines":["e"],"id":40},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":["c"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["n"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":["e"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["p"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["s"]}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["S"],"id":41},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["p"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":23},"action":"remove","lines":["Spe"],"id":42},{"start":{"row":12,"column":20},"end":{"row":12,"column":26},"action":"insert","lines":["Spence"]}],[{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["."],"id":43}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":34},"action":"insert","lines":["objects"],"id":44}],[{"start":{"row":12,"column":34},"end":{"row":12,"column":35},"action":"insert","lines":["."],"id":45}],[{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"insert","lines":["o"],"id":46}],[{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"remove","lines":["o"],"id":47},{"start":{"row":12,"column":35},"end":{"row":12,"column":45},"action":"insert","lines":["order_by()"]}],[{"start":{"row":12,"column":44},"end":{"row":12,"column":46},"action":"insert","lines":["''"],"id":48}],[{"start":{"row":12,"column":45},"end":{"row":12,"column":46},"action":"insert","lines":["-"],"id":49},{"start":{"row":12,"column":46},"end":{"row":12,"column":47},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":47},"end":{"row":12,"column":48},"action":"insert","lines":["e"],"id":50},{"start":{"row":12,"column":48},"end":{"row":12,"column":49},"action":"insert","lines":["l"]},{"start":{"row":12,"column":49},"end":{"row":12,"column":50},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":50},"end":{"row":12,"column":51},"action":"insert","lines":["a"],"id":51},{"start":{"row":12,"column":51},"end":{"row":12,"column":52},"action":"insert","lines":["s"]},{"start":{"row":12,"column":52},"end":{"row":12,"column":53},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":53},"end":{"row":12,"column":54},"action":"insert","lines":["_"],"id":52},{"start":{"row":12,"column":54},"end":{"row":12,"column":55},"action":"insert","lines":["d"]},{"start":{"row":12,"column":55},"end":{"row":12,"column":56},"action":"insert","lines":["a"]},{"start":{"row":12,"column":56},"end":{"row":12,"column":57},"action":"insert","lines":["t"]},{"start":{"row":12,"column":57},"end":{"row":12,"column":58},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":60},"end":{"row":12,"column":62},"action":"insert","lines":["[]"],"id":53}],[{"start":{"row":12,"column":61},"end":{"row":12,"column":62},"action":"insert","lines":[":"],"id":54},{"start":{"row":12,"column":62},"end":{"row":12,"column":63},"action":"insert","lines":["1"]},{"start":{"row":12,"column":63},"end":{"row":12,"column":64},"action":"insert","lines":["5"]}],[{"start":{"row":0,"column":0},"end":{"row":6,"column":56},"action":"remove","lines":["# from django.shortcuts import render","","# # Create your views here.","# from django.http import HttpResponse","# # Create your views here.","# def index(request):","#     return HttpResponse(\"You're at the spence index.\")"],"id":55}],[{"start":{"row":0,"column":0},"end":{"row":12,"column":60},"action":"insert","lines":["from django.http import Http404","from django.shortcuts import render","from .models import Movie","def index(request):","newest_movies = Movie.objects.order_by('-release_date')[:15]","context = {'newest_movies': newest_movies}","return render(request, 'movies/index.html', context)","def show(request, movie_id):","try:","movie = Movie.objects.get(pk=movie_id)","except Movie.DoesNotExist:","raise Http404(\"Movie does not exist\")","return render(request, 'movies/show.html', {'movie': movie})"],"id":56}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":57}],[{"start":{"row":4,"column":19},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":58}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":[" "],"id":59}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"remove","lines":[" "],"id":60}],[{"start":{"row":4,"column":19},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "],"id":62}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "],"id":63}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":64}],[{"start":{"row":9,"column":28},"end":{"row":10,"column":0},"action":"remove","lines":["",""],"id":65}],[{"start":{"row":9,"column":28},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":66},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":8},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":67}],[{"start":{"row":10,"column":8},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":68},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "],"id":69}],[{"start":{"row":12,"column":30},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":70}],[{"start":{"row":12,"column":30},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":71},{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":[" "],"id":72},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":[" "]},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":[" "]},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["# "],"id":73},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":2},"action":"insert","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"insert","lines":["# "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"remove","lines":["e"],"id":74},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"remove","lines":["i"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"remove","lines":["v"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"remove","lines":["o"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"remove","lines":["M"]}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["S"],"id":75},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["p"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["e"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["n"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["c"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":64},"action":"remove","lines":["newest_movies = Movie.objects.order_by('-release_date')[:15]"],"id":76},{"start":{"row":5,"column":4},"end":{"row":5,"column":65},"action":"insert","lines":["newest_pantry = Spence.objects.order_by('-release_date')[:15]"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":46},"action":"remove","lines":["context = {'newest_movies': newest_movies}"],"id":77},{"start":{"row":6,"column":4},"end":{"row":6,"column":46},"action":"insert","lines":["context = {'newest_pantry': newest_pantry}"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":56},"action":"remove","lines":["return render(request, 'movies/index.html', context)"],"id":78},{"start":{"row":7,"column":4},"end":{"row":7,"column":56},"action":"insert","lines":["return render(request, 'spence/index.html', context)"]}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":21},"action":"remove","lines":["Movie"],"id":79},{"start":{"row":11,"column":16},"end":{"row":11,"column":22},"action":"insert","lines":["Spence"]}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["e"],"id":80},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["i"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["v"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["o"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"remove","lines":["m"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["s"],"id":81},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["p"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["e"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["n"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["c"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":16},"action":"remove","lines":["Movie"],"id":82},{"start":{"row":12,"column":11},"end":{"row":12,"column":17},"action":"insert","lines":["Spence"]}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["s"],"id":83},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["i"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["v"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["o"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["m"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["s"],"id":84},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["p"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["n"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["c"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":34},"action":"remove","lines":["spence"],"id":85},{"start":{"row":14,"column":28},"end":{"row":14,"column":35},"action":"insert","lines":["spence/"]}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["/"],"id":86}],[{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"remove","lines":["e"],"id":87},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"remove","lines":["i"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"remove","lines":["v"]},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"remove","lines":["o"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"remove","lines":["m"]}],[{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"insert","lines":["s"],"id":88},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"insert","lines":["p"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"insert","lines":["e"]},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"insert","lines":["n"]},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"insert","lines":["c"]},{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"remove","lines":["e"],"id":89},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"remove","lines":["i"]},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"remove","lines":["v"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"remove","lines":["o"]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"remove","lines":["m"]}],[{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"insert","lines":["s"],"id":90},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"insert","lines":["p"]},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"insert","lines":["e"]},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"insert","lines":["n"]},{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"insert","lines":["c"]},{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["e"],"id":91},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["i"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["v"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["o"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["M"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["P"],"id":92},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["a"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["t"],"id":93},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["e"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["y"]}],[{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["y"],"id":94},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["e"]}],[{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["r"],"id":95},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["y"]}]]},"timestamp":1697991477991}