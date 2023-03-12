import copy
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    
}


def recept(request, url_):
    rec = []
    for rec_key in DATA.keys():
        rec.append(rec_key)
    for i in range(len(rec)):
        if rec[i] == url_:
            name = rec[i]
            servings = int(request.GET.get('servings', 1))
            rec_copy = copy.copy(DATA[url_])
            for ingredient, amount in DATA[url_].items():
                rec_copy[ingredient] = amount * servings
            context = {
                'url_': url_,
                'recipe': rec_copy,
                'servings': servings,
                'name': url_
            }
            return render(request, 'calculator/index.html', context)
    context = {
        'empty': None
    }
    return render(request, 'calculator/index.html', context)
