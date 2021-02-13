"""
Por que testar o código?

    - Reduzir bugs no código existe;
    - Testes garantem que novos recursos da sua aplicação não quebrem o recurso antigos;
    - Testes garantem que bugs que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatoração que costumamos fazer não tragam novos bugs;

Metodologia TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

class Pokemon:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def treinar(self):
        print(f"{self.__nome} está treinando!")


squirtle = Pokemon("squirtle")

squirtle.treinar()

"""


