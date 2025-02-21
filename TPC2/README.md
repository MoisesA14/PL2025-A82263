# TPC2: Análise de um dataset de obras musicais

20/02/2025

## Autor  

- **Nome:** Moisés Antunes 
- **Número de Aluno:** A82263 

## Introdução

Pretende-se um programa que leia e processe o dado dataset e crie os seguintes resultados
- Lista ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras catalogadas em cada período;
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.

## Solução

Criar um programa que identifica e separa strings correspondentes ao campo que se pretende para cada resultado específico dos restantes campos baseado na sua posição na linha relativa a uma dada obra (neste caso, para cada obra, o primeiro campo corresponde ao nome, o segundo à descrição e assim sucessivamente conforme o primeira linha do ficheiro dataset). Essas strings depois formarão as listas e os dicionários pretendidos. Cada campo está separado do seguinte por ';', exceto o último de cada linha (_id), que deverá estar seguido de '\n', para causar a mudança de linha entre obras.

## Execução

O programa é executado no terminal. 

```
$ py tpc2.py
```
