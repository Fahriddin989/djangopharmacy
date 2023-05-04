from django.db import models
from account.models import UserModel
from ckeditor.fields import RichTextField

class Categories(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, verbose_name='Подкатегория', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural= 'Категории'


# class SubCategories(models.Model):
#     category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='категория')
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


class Manufactures(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural= 'Производители'


    def __str__(self):
        return self.name


class ActiveSubstances(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Активные вещества'
        verbose_name_plural= 'Активные вещества'


    def __str__(self):
        return self.name


class Medicines(models.Model):
    name = models.CharField('Наименование', max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='категория')
    country = models.CharField('Страна производителя', max_length=255)
    active_substances = models.ForeignKey(ActiveSubstances, on_delete=models.CASCADE, verbose_name='активные вещества')
    representative = models.CharField('Представитель', max_length=255)
    image = models.ImageField('Изображение', upload_to='medicine/%Y/%m/%d')
    manufacturer = models.ForeignKey(Manufactures, on_delete=models.CASCADE, verbose_name='Производитель')
    code_atx = models.CharField('Штрих-код', max_length=255)
    stock = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавление'
        verbose_name_plural= 'Добавление'



class CartItem(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def str(self):
        return f"{self.quantity} x {self.product.name} ({self.user.username})"

    @property
    def get_total(self):
        return self.product.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
