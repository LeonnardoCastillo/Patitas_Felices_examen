class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, planta):
        if planta.code not in self.carrito.keys():
            self.carrito[planta.code]={
                "planta_id":planta.code, 
                "nombre": planta.nombre,
                "precio": str (planta.precio),
                "cantidad": 1,
                "total": planta.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key==planta.code:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = planta.precio
                    value["total"]= value["total"] + planta.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, planta):
        id = planta.code
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,planta):
        for key, value in self.carrito.items():
            if key == planta.code:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- planta.precio
                if value["cantidad"] < 1:   
                    self.eliminar(planta)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 