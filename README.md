# CODER CHALLENGE DSIN: Etapa Bônus

## Sistema para levantamento de naves espaciais caídas, permitindo registro e geração automática de classificação.

### 💻 Executando o projeto

Para rodar o projeto basta rodar o comando:<br>
```bash
python index.py
```

Para fins de teste, as informações são salvas localmente utilizando SQLite. Uma instância do banco será criada automaticamente caso não exista.

### ⚙️ Funcionamento

No sistema é possível realizar as seguintes operações:
- Registrar naves
- Listar as naves registradas
- Visualizar os detalhes das naves
- Editar as informações das naves
- Deletar uma nave

### 📂 Critério de Classificação

Ao registrar ou editar uma nave, uma classificação será gerada para a nave de acordo com os dados informados. Cada informação adiciona um ponto para uma das classificações possíveis e ao final a nave recebe a classificação que possuir o maior valor, seguindo uma ordem de prioridade. <br>
Verifique a descrição de cada classificação e os critérios de pontuação para cada uma abaixo, organizados por ordem de prioridade.
- Ameaça em Potencial: Possui elementos que podem ser perigosos, como armadilhas, sistemas autônomos hostis ou biocontaminantes.
- Arsenal Alienígena: Contém armamentos ou defesas avançadas que podem ser úteis para reforçar nossa segurança;
- Joia Tecnológica: Possui sistemas e componentes avançados que podem ser estudados e adaptados para melhorar nossa própria tecnologia.
- Biblioteca Intergalática: A nave contém informações e registros de culturas, idiomas e ciências alienígenas. Pode ser valiosa para a compreensão de outras civilizações e para o avanço de nossas ciências e filosofia.
- Enigma Científico: A nave possui tecnologia ou design incomum, sem semelhança com outras civilizações conhecidas, sugerindo uma origem além dos limites conhecidos do espaço. Estuda-la pode revelar segredos ocultos do universo.
- Fonte de Energia Alternativa: Contém tecnologias de propulsão ou sistemas de energia únicos que poderiam ser aproveitados.
- Sucata Espacial: A nave tem pouco ou nenhum valor tecnológico, mas suas peças podem ser reutilizadas em outras construções ou projetos.

| Classificação |  Poderio Bélico  | Qtd. Armas | Tipo Combustível | Avaria | Potencial Tecnológico | Periculosidade | Info. Armazenada |
|:--------------|:----------------:|:----------:|:----------------:|:------:|:---------------------:|:--------------:|-----------------:|
| Ameaça em Potencial          | Alto ou superior | 6 a 8 | Não determinante | Exceto Destruído | Alto ou superior | Alto ou superior | Mediano ou inferior |
| Arsenal Alienígena           | Alto ou superior | 3 a 5 | Não determinante | Uso mínimo ou superior | Mediano ou superior | Alto | Mediano ou inferior |
| Joia Tecnológica             | Baixo | Até 2 | Não determinante | Desgastado ou superior | Alto ou superior | Moderado ou inferior | Mediano ou inferior |
| Biblioteca Intergalática     | Baixo | Até 1 | Não determinante | Uso mínimo ou superior | Alto ou superior | Baixo | Alto ou superior |
| Enigma Científico            | Moderado ou inferior | Até 2 | Não determinante | Exceto Destruído | Além da Compreensão | Moderado ou inferior | Alto ou superior |
| Fonte de Energia Alternativa | Moderado ou inferior | Até 1 | Cristais de Gravidade Líquida, Matéria Escura ou Campo de Vibração Quântica | Desgastado ou superior | Mediano ou Superior | Moderado ou inferior | Mediano ou inferior |
| Sucata Espacial              | Baixo | Não determinante | Não determinante | Muito Desgastado ou inferior | Baixo | Moderado ou inferior | Baixo |
