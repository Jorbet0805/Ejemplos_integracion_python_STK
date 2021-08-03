def decorador_error(mensaje="",
                    hacer_print=False,
                    hacer_log=False,
                    mensaje_comienzo="Comenzar proceso",
                    mensaje_exito="Todo fue bien"
                    ):
    def decorador(funtion):
        """ 
        Si ocurre un error, se imprime o logea un mensaje
        """
        def wrapper(*args, **kwargs):
            try:
                print(mensaje_comienzo)
                funtion(*args, **kwargs)
                print(mensaje_exito)
            except:
                if hacer_print:
                   print(mensaje)
                if hacer_log:
                   pass

        return wrapper
    
    return decorador