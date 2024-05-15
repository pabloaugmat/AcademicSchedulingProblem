# Academic Scheduling Problem

O Academic Scheduling Problem (ASP) trata-se do desafio de organizar horários para cursos em instituições educacionais de maneira que se otimize a utilização de recursos como salas de aula, professores e horários disponíveis. O objetivo é desenvolver um cronograma que respeite várias restrições, como a disponibilidade de professores, a capacidade máxima de cada sala, a não sobreposição de horários para cursos que possam ter o mesmo público-alvo e as preferências de horários tanto de alunos quanto de professores. Resolver este problema envolve achar um equilíbrio entre essas necessidades conflitantes, garantindo a eficácia e a eficiência do ambiente acadêmico.

## Propósito

Este repositório é dedicado exclusivamente à modelagem do Academic Scheduling Problem (ASP) no contexto do Instituto de Matemática e Computação (IMC) da Universidade Federal de Itajubá (UNIFEI). A particularidade desta modelagem é que consideraremos apenas os recursos de professores e disciplinas, sem incluir o recurso de local físico.

O foco deste trabalho não é implementar soluções diretamente, mas sim estabelecer uma representação precisa e detalhada do problema. A modelagem adequada é crucial, pois serve como o primeiro passo essencial para qualquer abordagem de solução subsequente. Seja através de métodos de otimização, heurísticas ou outros algoritmos, uma compreensão clara das variáveis e restrições envolvidas é fundamental para o sucesso na resolução do ASP.

Neste contexto, procuramos desenvolver uma base sólida que permita a futuras pesquisas ou projetos, aplicar e testar diferentes estratégias de solução com eficácia, tendo em vista as particularidades do ambiente acadêmico do IMC na UNIFEI.

## Requisitos

Este projeto foi testado e validado exclusivamente no ambiente Windows Subsystem for Linux (WSL2) utilizando Python versão 3. Para garantir a compatibilidade e o funcionamento adequado das scripts e ferramentas desenvolvidas, recomendamos a utilização deste ambiente.

### Dependências

Para executar os scripts e realizar a modelagem proposta neste repositório, é necessário instalar as seguintes bibliotecas Python:

#### Pandas

Pandas é uma biblioteca fundamental para a manipulação e análise de dados em Python. Instale usando o seguinte comando:

```bash
pip install pandas
```

#### Graphviz

Graphviz é uma ferramenta que permite a visualização de grafos, útil para representar relações e dependências de forma gráfica. Instale com o comando:

```bash
pip install graphviz
```

Assegure-se de que todas as dependências estejam instaladas para evitar problemas na execução dos modelos.

## Execução do Programa

Este repositório contém dois scripts principais: um para a aplicação e renderização da modelagem no conjunto de dados (DataSet) e outro para a renderização do modelo conceitual. Ambos os scripts são fundamentais para a compreensão e visualização do Academic Scheduling Problem conforme modelado para o IMC na UNIFEI.

### Como Executar

Para executar qualquer um dos scripts, siga os passos abaixo:

1. Abra o terminal no seu sistema.
2. Navegue até o diretório onde os scripts estão localizados.
3. Execute o comando abaixo para iniciar o script desejado:

```bash
python3 main.py
```

## Contribuindo
Contribuições são sempre bem-vindas! Se você tem melhorias ou correções, sinta-se à vontade para forkar o repositório e enviar um pull request com suas mudanças.
