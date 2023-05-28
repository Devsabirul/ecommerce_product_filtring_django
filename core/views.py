from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.db.models import Q
from django.template.loader import render_to_string

def home(request):
  product = Product.objects.all()
  productcategory = ProductCategory.objects.all()

# start get unique category for display in html template
  # unique category
  uCategory = dict()
  for unique in productcategory:
    if unique.categories in uCategory:
        uCategory[unique.categories] += 1
    else:
        uCategory[unique.categories] = 1
  categories = []
  for i in uCategory:
    categories.append(i)

  #unique Product Type
  uproduct_type = dict()
  for unique in productcategory:
    if unique.product_type in uproduct_type:
        uproduct_type[unique.product_type] += 1
    else:
        uproduct_type[unique.product_type] = 1
  product_type = []
  for i in uproduct_type:
    product_type.append(i)  

  # unique brands 
  ubrands = dict()
  for unique in productcategory:
    if unique.brands in ubrands:
        ubrands[unique.brands] += 1
    else:
        ubrands[unique.brands] = 1
  brands = []
  for i in ubrands:
    brands.append(i)  

  # unique seller 
  useller = dict()
  for unique in productcategory:
    if unique.seller in useller:
        useller[unique.seller] += 1
    else:
        useller[unique.seller] = 1
  seller = []
  for i in useller:
    seller.append(i)

  # unique warranty 
  uwarranty = dict()
  for unique in productcategory:
    if unique.warranty in uwarranty:
        uwarranty[unique.warranty] += 1
    else:
        uwarranty[unique.warranty] = 1
  warranty = []
  for i in uwarranty:
    warranty.append(i)
# End get unique category for display in html template

  return render(request, "home/index.html",locals())

def filterProduct(request):
  # get filter data 
  brands = request.GET.getlist('brands[]')
  categories = request.GET.getlist('categories[]')
  producttype = request.GET.getlist('producttype[]')
  seller = request.GET.getlist('seller[]')
  warranty = request.GET.getlist('warranty[]')
  allProducts = Product.objects.all()
# filtering data diffrent value 
  if len(brands)>0:
    allProducts = allProducts.filter(prodcut_category__brands__in=brands).distinct()
  if len(categories)>0:
    allProducts = allProducts.filter(prodcut_category__categories__in=categories).distinct()
  if len(producttype)>0:
    allProducts = allProducts.filter(prodcut_category__product_type__in=producttype).distinct()
  if len(seller)>0:
    allProducts = allProducts.filter(prodcut_category__seller__in=seller).distinct()
  if len(warranty)>0:
    allProducts = allProducts.filter(prodcut_category__warranty__in=warranty).distinct()
# end filtering data diffrent value

  template = render_to_string('home/product-list.html',{'data':allProducts})
  return JsonResponse({'data':template})