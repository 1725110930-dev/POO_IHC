class HelloWord:
    
    def __init__(self):
        print("Builder")

    def methodOne(self):
        print("Method one")
    
    def methodTwo(self, num_one:int, num_two:int)->int:
        """
        Este metodo  realiza la suma de dos numeros enteros y regresa el resultado

        Args:
            num_one:int - Primer numero para la suma
            num_two:int - Segundo numero para la suma

        Return: 
            result:int - Variable con el resultado de la suma
        """
        result = num_one + num_two
        return result
    
    def methonThree(self, num_one, num_two):
        result = num_one + num_two
        return result

    def methodFour(self, num_one, num_two):
        result = num_one + num_two
        print(f"The addition is {result}")

obj_name = HelloWord(self)
