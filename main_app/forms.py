from django import forms


class UserChoiceFilterForm(forms.Form):
    sort_by_price_ascending = 'price_as'
    sort_by_price_descending = 'price_des'
    sort_by_date = 'date'
    sort_by_name = 'name'
    sort_by_promotion = 'action'
    sort_products = [
        (sort_by_date, 'sort by date'),
        (sort_by_price_ascending, 'sort by price ascending'),
        (sort_by_price_descending, 'sort by price descending'),
        (sort_by_name, 'sort by name'),
        (sort_by_promotion, 'sort by action')
    ]
    filter_by = forms.ChoiceField(choices=sort_products)








