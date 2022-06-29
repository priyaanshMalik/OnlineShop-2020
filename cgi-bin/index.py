import base

products = base.getProducts()

base.header()

print('''
  <div class="container">
    <h1 class="text-center">Products</h1>
    <hr>
    <div class="row">
''')

for product in products:
    base.createProduct(product)

print('''
    </div>
  </div>
''')


base.footer()