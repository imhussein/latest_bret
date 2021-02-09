def search_model(func):
    def search(model, request, keyword, *args, **kwargs):
        query_list = model.objects.all()
        if keyword in request.GET:
            value = request.GET[keyword]
            if value:
                query_list = query_list.filter(**kwargs)
        func(model, request, keyword, query_list, *args, **kwargs)
        return query_list
    return search


@search_model
def apply_search(model, request, keyword, *args, **kwargs):
    for key, value in kwargs.items():
        print(
            f'Filtering {model.get_model_name()} Model for keyword {key.split("__")[0]} and value {value}')
