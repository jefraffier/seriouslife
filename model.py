

class plateau(object):
    def __init__(self):
        self.plateau = None
        
        self.users = []
        self.cartes = []
        
    # Start of user code -> properties/constructors for plateau class

    # End of user code
    def creer_user(self):
        # Start of user code protected zone for creer_user function body
        raise NotImplementedError
        # End of user code	
    def creer_partie(self):
        # Start of user code protected zone for creer_partie function body
        raise NotImplementedError
        # End of user code	
    def creer_jauge(self):
        # Start of user code protected zone for creer_jauge function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for plateau class

    # End of user code

class users(object):
    def __init__(self):
        self.id = 0
        self.nom = ""
        self.genre = ""
        self.jauge_sante = 0
        self.jauge_sociabilite = 0
        self.jauge_richesse = 0
        self.position = 0
        
        self.plateau = None
        self.cartes = []
        
    # Start of user code -> properties/constructors for users class

    # End of user code
    def piocher_carte(self):
        # Start of user code protected zone for piocher_carte function body
        return 0
        # End of user code	
    # Start of user code -> methods for users class

    # End of user code

class cartes(object):
    def __init__(self):
        self.nom = ""
        self.description = ""
        
        self.plateau = None
        self.users = None
        
    # Start of user code -> properties/constructors for cartes class

    # End of user code
    def action(self):
        # Start of user code protected zone for action function body
        return 0
        # End of user code	
    # Start of user code -> methods for cartes class

    # End of user code



class Sociabilite(cartes):
    pass
    # Start of user code -> properties/constructors for Sociabilite class

    # End of user code
    def action(self):
        # Start of user code protected zone for action function body
        return 0
        # End of user code	
    # Start of user code -> methods for Sociabilite class

    # End of user code

class Richesse(cartes):
    pass
    # Start of user code -> properties/constructors for Richesse class

    # End of user code
    def action(self):
        # Start of user code protected zone for action function body
        return 0
        # End of user code	
    # Start of user code -> methods for Richesse class

    # End of user code

class Sante(cartes):
    pass
    # Start of user code -> properties/constructors for Sante class

    # End of user code
    def action(self):
        # Start of user code protected zone for action function body
        return 0
        # End of user code	
    # Start of user code -> methods for Sante class

    # End of user code


# Start of user code -> functions/methods for model package

# End of user code
