import sympy as sp
from numpy import pi, linspace, meshgrid, sqrt, cos, sin



class SLG:
    def __init__(self, intralayer_Hopping=1.0,lattice_constant=1.42):
        """
        Initialize the SLG class with the given parameters.
        Parameters:
        intralayer_Hopping (float): The intralayer hopping parameter.
        lattice_constant (float): The lattice constant of the graphene structure.
        """
        self.t = intralayer_Hopping
        self.a = lattice_constant
        

        self.gammafunction()
        self.Hk()
        pass
    def __str__(self):
        return "SLG"
    def __repr__(self):
        return "SLG"
    def __call__(self, *args, **kwargs):
        """
        This function is a placeholder for the SLG class. It currently does nothing and returns None.
        """
        pass
    def gammafunction(self)->None:
        kx, ky, a, t = sp.symbols('kx ky a t', real=True)
        self.gamma = sp.exp(-sp.I*kx*a)*(1 + 2*sp.exp(sp.I*2*kx*a/2)*(sp.cos(sp.sqrt(3)*ky*a/2)))
    
    def Hk(self)->None:
        self.Hk = sp.Matrix([[0, self.t*self.gamma], [self.t*self.gamma.conjugate(), 0]])

    def solveH(self):
        self.E = self.Hk.eigenvals(multiple=True)

    def plzplot(self, kx, ky):
        import matplotlib.pyplot as plt
        
        kx_vals = linspace(kx[0], kx[1], kx[2])
        ky_vals = linspace(ky[0], ky[1], ky[2])
        KX, KY = meshgrid(kx_vals, ky_vals)
        
        self.solveH()

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(KX, KY, E_vals[0], cmap='viridis', alpha=0.9, edgecolor='none')

        # Optional: also plot lower band
        ax.plot_surface(KX, KY, E_vals[1], cmap='magma', alpha=0.8, edgecolor='none')

        ax.set_xlabel(r'$k_x$')
        ax.set_ylabel(r'$k_y$')
        ax.set_zlabel(r'$E$')
        ax.set_title("Graphene Tight-Binding Energy Bands")
        plt.tight_layout()
        plt.show()


