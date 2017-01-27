
#!!! Favor object composition over inheritance
#https://www.toptal.com/python/python-design-patterns


#wrapper class for another class
class User:
    #define accesable methods
    _persist_methods = ['get', 'save', 'delete']
	#initialize the wrapper
    def __init__(self, persister):
        self._persister = persister
    #check and return the method
    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)
			
			

			