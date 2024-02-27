from django.db import models

# Create your models here.


class MenuCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    

class MenuItem(models.Model):
    category = models.ForeignKey('MenuCategory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254,null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    allergens= models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True) 
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='menu_items/',null=True, blank=True)
    ingredients = models.ManyToManyField('Ingredient', through='MenuItemIngredient')
    included_items = models.ManyToManyField('self', through='MenuItemIncludedItem', related_name='included_in_items', blank=True)


    def __str__(self):
        return self.name
    
class MenuItemIngredient(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    option = models.ForeignKey('IngredientOption', null=True, blank=True, on_delete=models.SET_NULL)  # new field
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    is_optional = models.BooleanField(default=True)

    def __str__(self):
        return self.menu_item.name + ' - ' + self.ingredient.name
    
class IngredientOption(models.Model):
    menu_items = models.ManyToManyField('MenuItem', blank=True)
    category= models.ForeignKey('MenuCategory', null=True,blank=True,  on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    single_select = models.BooleanField(default=False)  # moved from Ingredient

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
class MenuItemIncludedItem(models.Model):
    menu_item = models.ForeignKey('MenuItem', related_name='included_menu_items', on_delete=models.CASCADE)
    included_item = models.ForeignKey('MenuItem', related_name='included_in', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Included: {self.menu_item.name} -> {self.included_item.name}'