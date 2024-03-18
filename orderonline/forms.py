from django import forms
from .models import MenuItem, MenuItemIncludedItem, MenuItemIngredient, IngredientOption
from django.forms import formset_factory

class MenuItemIncludedItemOptionForm(forms.Form):
    option = forms.ModelChoiceField(queryset=MenuItemIngredient.objects.none(), widget=forms.RadioSelect, required=False)

    def __init__(self, *args, item=None, **kwargs):
        super().__init__(*args, **kwargs)
        if item is not None:
            self.fields['option'].queryset = MenuItemIngredient.objects.filter(menu_item=item)

MenuItemIncludedItemOptionFormSet = formset_factory(MenuItemIncludedItemOptionForm, extra=0)

class MenuItemIncludedItemChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if obj.included_item.price == 0:
            return f"{obj.included_item.name}"  # If the price is 0, only display the name
        else:
            return f"{obj.included_item.name} - {obj.price}€"  # If the price is not 0, display the name and the price
        

class IngredientChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prices = {}

    def label_from_instance(self, obj):
        self.prices[obj.id] = obj.price
        if obj.price == 0:
            return f"{obj.ingredient.name}"  # If the price is 0, only display the name
        else:
            return f"{obj.ingredient.name} - {obj.price}€"  # If the price is not 0, display the name and the price

class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_dict = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        # Add 'data-price' attribute to the option
        option_dict['attrs']['data-price'] = self.choices.field.prices[value.value]
        return option_dict

class CustomRadioSelect(forms.RadioSelect):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_dict = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        # Add 'data-price' attribute to the option
        option_dict['attrs']['data-price'] = self.choices.field.prices[value.value]
        return option_dict

class AddToCartForm(forms.Form):
    item_id = forms.ModelChoiceField(queryset=MenuItem.objects.all(), widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control quantity'}))

    def __init__(self, *args, item=None, adding=True,**kwargs):
        super().__init__(*args, **kwargs)
        if item is not None:
            ingredients = MenuItemIngredient.objects.filter(menu_item=item)
            ingredient_options = self.get_options(ingredients)
            for option_name, items in ingredient_options.items():
                if option_name == 'Extras':
                    self.fields[option_name] = IngredientChoiceField(
                        queryset=MenuItemIngredient.objects.filter(id__in=[i.id for i in items]),
                        widget=CustomCheckboxSelectMultiple,
                        required=False,
                        empty_label=None
                    )
                else:
                    self.fields[option_name] = IngredientChoiceField(
                        queryset=MenuItemIngredient.objects.filter(id__in=[i.id for i in items]),
                        widget=CustomRadioSelect,
                        required=True
                    )
                    if adding:
                        self.fields[option_name].initial = items[-1].id if items else None

            included_items = MenuItemIncludedItem.objects.filter(menu_item=item)
            if included_items.exists():
                self.fields['included_item'] = MenuItemIncludedItemChoiceField(
                    queryset=included_items, 
                    required=False, 
                    widget=forms.Select(attrs={'class': 'd-block mx-auto w-100'})
                )
                self.fields['included_item'].initial = included_items.first()

    def get_options(self, items):
        options = {}
        for item in items:
            option = item.option
            if option is None:
                option_name = 'Extras'
            else:
                option_name = option.name
            if option_name not in options:
                options[option_name] = []
            options[option_name].append(item)
        return options