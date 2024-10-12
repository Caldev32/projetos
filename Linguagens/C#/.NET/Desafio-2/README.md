
## Desafio de projeto
Usando conhecimentos adquiridos no módulo de orientação a objetos, da trilha .NET da DIO.

## Contexto
Abstração de um celular e disponibilização de maneiras de diferentes marcas e modelos terem seu próprio comportamento, possibilitando um maior reuso de código e usando a orientação a objetos.

## Proposta
Sistema em .NET, do tipo console, que mapeia uma classe abstrata e classes específicas para dois tipos de celulares: Nokia e iPhone. 


## Regras e validações
1. A classe **Smartphone** deve ser abstrata, não permitindo instanciar e servindo apenas como modelo.
2. A classe **Nokia** e **Iphone** devem ser classes filhas de Smartphone.
3. O método **InstalarAplicativo** deve ser sobrescrito na classe Nokia e iPhone, pois ambos possuem diferentes maneiras de instalar um aplicativo.

