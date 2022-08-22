from pydoc import cli


def main():
    clientes = {}
    print(clientes)
    clientes = {"Assinante1" : ["Henrique", "henrique@gmail.com", 33],
                "Assinante2" : ["José", "jose@gmail.com", 32],
                "Assinante3": ["Jackson", "jackson@gmail.com", 31]}    
    
    print(clientes)
    
    
if __name__ == '__main__':
    main()