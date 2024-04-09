from django import forms
from .models import (
    MenuItem, MenuItemIncludedItem, MenuItemIngredient,
    IngredientOption, MenuCategory
)
from django.forms import formset_factory
from .widgets import CustomClearableFileInput


class MenuItemIncludedItemOptionForm(forms.Form):
    '''Form for MenuItem Included Item Options'''
    option = forms.ModelChoiceField(
        queryset=MenuItemIngredient.objects.none(),
        widget=forms.RadioSelect, required=False
    )

    def __init__(self, *args, item=None, **kwargs):
        super().__init__(*args, **kwargs)
        if item is not None:
            self.fields['option'].queryset = MenuItemIngredient.objects.filter(
                menu_item=item
            )


MenuItemIncludedItemOptionFormSet = formset_factory(
    MenuItemIncludedItemOptionForm, extra=0
)


class MenuItemIncludedItemChoiceField(forms.ModelChoiceField):
    '''Model Choice Field for MenuItem Included Items'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prices = {}

    def label_from_instance(self, obj):
        self.prices[obj.id] = obj.price
        if obj.included_item.price == 0:
            return f"{obj.included_item.name}"
        else:
            return f"{obj.included_item.name} - {obj.price}€"


class IngredientChoiceField(forms.ModelChoiceField):
    '''Model Choice Field for Ingredients'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prices = {}

    def label_from_instance(self, obj):
        self.prices[obj.id] = obj.price
        if obj.price == 0:
            return f"{obj.ingredient.name}"
        else:
            return f"{obj.ingredient.name} - {obj.price}€"


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    '''Custom Checkbox Select Multiple Widget'''
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option_dict = super().create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        option_dict['attrs']['data-price'] = self.choices.field.prices[
            value.value
        ]
        return option_dict


class CustomRadioSelect(forms.RadioSelect):
    '''Custom Radio Select Widget'''
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option_dict = super().create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        option_dict['attrs']['data-price'] = self.choices.field.prices[
            value.value
        ]
        return option_dict


class CustomSelect(forms.Select):
    '''Custom Select Widget'''
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option_dict = super().create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        if value:
            option_dict['attrs']['data-price'] = self.choices.field.prices[
                value.value
            ]
        return option_dict


class AddToCartForm(forms.Form):
    """
    A form for adding a menu item to the cart.

    This form includes fields for the menu item ID and the quantity.
    The menu item ID is a hidden field, and the quantity is an integer
    field with a minimum value of 1.

    The form's initialization function takes an optional 'item' argument,
    which is a menu item instance. If an item is provided, the function fetches
    all the ingredients associated with the item and categorizes them into
    'Options' and 'Extras'. These categories are then added as fields to 
    the form.

    If the 'Extras' category exists, it is added as a field with a custom
    checkbox select multiple widget and is not required.
    Other categories are added as fields with a custom radio select widget 
    and are required.

    If the 'adding' argument is True, the initial value of the 'Options' 
    fields is set to the ID of the last ingredient in the category.

    The function also fetches all the included items associated with 
    the menu item and adds them as a field to the form with a custom
    select widget. 
    The initial value of this field is set to the first included item.

    The 'get_options' method categorizes the ingredients into 'Options'
    and 'Extras' based on their option attribute. 
    If an ingredient does not have an option, it is categorized as an 'Extra'.
    The method returns a dictionary where the keys are the category names and
    the values are lists of ingredients in the category.
    """
    item_id = forms.ModelChoiceField(
        queryset=MenuItem.objects.all(), widget=forms.HiddenInput()
    )
    quantity = forms.IntegerField(
        min_value=1, initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control quantity'})
    )

    def __init__(self, *args, item=None, adding=True, **kwargs):
        super().__init__(*args, **kwargs)
        if item is not None:
            ingredients = MenuItemIngredient.objects.filter(menu_item=item)
            ingredient_options = self.get_options(ingredients)
            for option_name, items in ingredient_options.items():
                if option_name == 'Extras':
                    option_name = option_name.replace(' ', '_')
                    self.fields[option_name] = IngredientChoiceField(
                        queryset=MenuItemIngredient.objects.filter(
                            id__in=[i.id for i in items]
                        ),
                        widget=CustomCheckboxSelectMultiple,
                        required=False,
                        empty_label=None
                    )
                else:
                    option_name = option_name.replace(' ', '_')
                    self.fields[option_name] = IngredientChoiceField(
                        queryset=MenuItemIngredient.objects.filter(
                            id__in=[i.id for i in items]
                        ),
                        widget=CustomRadioSelect,
                        required=True
                    )
                    if adding:
                        self.fields[option_name].initial = (
                            items[-1].id if items else None
                        )

            included_items = MenuItemIncludedItem.objects.filter(
                menu_item=item)
            if included_items.exists():
                self.fields['included_item'] = MenuItemIncludedItemChoiceField(
                    queryset=included_items,
                    required=False,
                    widget=CustomSelect(
                        attrs={'class': 'd-block'})
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


class ItemForm(forms.ModelForm):
    '''Form for Menu Items'''
    class Meta:
        model = MenuItem
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = MenuCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['ingredients'].required = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
