# If you notice the folder named ecommerce in the Packages folder, 
# it's a package, which is a collection of modules, which are created when a folder contain
# a __init__.py file, which is a file that is executed when the package is imported

# To use a module from a package, you have to import it just like a module
import ecommerce.shipping

ecommerce.shipping.calc_shipping() # This will print "Calculating shipping"

# But you see, this is not the best way to use a package, because you have to write 
# ecommerce.shipping.calc_shipping() every time you want to use a function from the shipping module

# So we can use the from keyword to import a module from a package
from ecommerce.shipping import calc_shipping

calc_shipping()

# But what about when the module have more than a single function?

from ecommerce.shipping import calc_shipping, calc_tax # See that we can import more than one function separated by a comma

calc_shipping()
calc_tax()

# Or we can import all the functions from the module
from ecommerce import shipping

shipping.calc_shipping()
shipping.calc_tax()