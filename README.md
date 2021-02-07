# Python Design Patterns

Design patterns are standard solutions to problems that typically occur in software development. These patterns usually depend on a compiler to enforce and maintain them, however the Python language provides features that make it possible to implement design patterns without a compiler.

One nice thing about design patterns is once you start using them, you sorta automatically use others by default. Because of this, some of the more complex design patterns in this library may contain other simpler design patterns to facilitate them.

This project is doing just that - implementing various design pattners the "Python" way as practice.

### Design Patterns Included

* Abstract Factory 
  * Implemented in the `abstract_factory` folder in the root directory.
  * Demonstrates how to create version independent creator/product objects to facilitate loose coupling to external dependencies.
* Adapter
  * This is a simpler design pattern, implemented in the `abstract_factory.factory.company` module.
  * This adapter wraps around an object that had it's definition changed, (`address` was removed) and re-adds that that property so the existing code that references `address` doesn't need to be changed.
* Decorator
  * Implemented in the `decorator` folder in the root directory.
  * This pattern (a personal favorite) demonstrates how to attach new behaviors and functionality to objects without modifying the other objects.
* More to come...
