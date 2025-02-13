# TPC1: Somador ON/OFF

13/02/2025

## Autor  

- **Nome:** Moisés Antunes 
- **Número de Aluno:** A82263 

## Introdução

- Pretende-se um programa que **some** todas as sequências de dígitos que encontre num texto;
- Sempre que encontrar a string "off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado.
- Sempre que encontrar a string "on" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado.
- Sempre que encontrar o caráter '=', o resultado da soma é colocado na saída.
- No final, coloca o resultado da soma na saída.

## Solução

O programa `soma_on_off` lê um ficheiro de texto e percorre o seu conteúdo carácter por caráter. Através de lógica booleana, da qual provêm o nome "ON/OFF" do programa somador, este determina quando deve estar a contar carateres para somar ou quando os deve apenas ignorar.

## Execução

O programa é executado ao passar o ficheiro de input como argumento no terminal. 

```
$ python tpc1.py <input_file>
```
