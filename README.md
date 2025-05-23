# Relatório de Atividades – Quality Assurance (QA)

## 1. Apresentação

**Nome completo:**  
Luis Eduardo Meireles Silva

**Curso e semestre:**  
Gestão da Tecnologia da Informação - 5º Semestre
Turma: GTI.5NA

**Breve descrição da experiência com a disciplina:**  
Durante a disciplina, tive uma boa experiência e pude aprender sobre a importância dos testes no desenvolvimento de software. Entendi como o Quality Assurance ajuda a garantir que os sistemas sejam mais seguros, estáveis e confiáveis. Também explorei diferentes tipos de testes e utilizei ferramentas como Google Colab e GitHub, o que facilitou a prática e o aprendizado ao longo do semestre.


## 2. O que é Quality Assurance (QA)?

Quality Assurance, ou QA, é o conjunto de práticas que ajudam a garantir que um software funcione bem e sem erros. Basicamente, é como cuidar para que tudo saia certo antes do produto chegar ao usuário. Essa disciplina me ensinou bastante sobre como diferentes testes ajudam a evitar problemas e deixar o software mais confiável.


## 3. Conceitos Aprendidos Durante o Semestre

**Qualidade em software e cultura de qualidade:**  
Aprendi que qualidade em software significa entregar um sistema que funcione corretamente, seja confiável e atenda às necessidades dos usuários. Também compreendi que a cultura de qualidade deve envolver toda a equipe e estar presente desde as primeiras fases do desenvolvimento, não apenas nos testes finais.

**Tipos de testes (unitário, integração, sistema, aceitação, regressão e exploratório):**

- **Teste unitário:** verifica o funcionamento de pequenas partes do código, como funções ou métodos individuais.  
- **Teste de integração:** avalia se diferentes partes do sistema funcionam bem juntas, como a comunicação entre módulos.  
- **Teste de sistema:** testa o sistema como um todo, simulando seu uso real para garantir que tudo funcione corretamente.  
- **Teste de aceitação:** verifica se o sistema atende aos requisitos e expectativas do cliente ou usuário final.  
- **Teste de regressão:** garante que novas mudanças ou atualizações não causem problemas em funcionalidades que já estavam funcionando.  
- **Teste exploratório:** é feito sem um roteiro fixo, permitindo que o testador explore o sistema em busca de falhas ou comportamentos inesperados.

**Planejamento de testes (critérios de aceitação, planos e casos de teste):**  
Aprendi que um bom planejamento de testes ajuda a garantir melhores resultados. Entendi como definir critérios de aceitação claros, montar planos de teste que organizem as atividades e escrever casos de teste detalhados para cobrir os diferentes cenários da aplicação.

**Ferramentas de testes utilizadas durante o semestre (Colab, GitHub, etc.):**  
Utilizei o Google Colab para escrever e executar scripts de testes de forma prática e online. Também usei o GitHub para versionamento dos arquivos e entrega dos trabalhos. Além disso, acessei sites como o ReqRes, que disponibiliza APIs simuladas para testes com requisições HTTP.

**Automação de testes e integração com CI/CD:**  
Aprendi que automatizar testes ajuda a economizar tempo e reduzir erros manuais. Também entendi o papel da integração contínua (CI) e da entrega contínua (CD), que permitem rodar testes automaticamente sempre que o código é atualizado, facilitando o desenvolvimento contínuo com qualidade.

**Monitoramento e controle de qualidade (uso de métricas, rastreamento de bugs, observabilidade):**  
Aprendi que monitorar a aplicação mesmo depois da entrega é essencial. Com o uso de métricas, rastreamento de bugs e ferramentas de observabilidade, é possível acompanhar o desempenho do sistema, identificar falhas rapidamente e manter a qualidade no ambiente de produção.


## 4. Ferramentas e Sites Utilizados

- [Google Colab](https://colab.research.google.com/)
- [GitHub](https://github.com/)
- [ReqRes (API para testes)](https://reqres.in/)
- [UptimeRobot](https://uptimerobot.com/)
- [Fake Filler](https://fakefiller.com/)
- [Ghost Inspector](https://ghostinspector.com/)

## 5. Resultados dos Testes

### Teste 01 – Formatação correta de nomes

**Objetivo:**  
Verificar se a função `formatar_nome` formata corretamente nomes com letras minúsculas, maiúsculas, misturadas e com acentos.

**Biblioteca utilizada:**  
`unittest`

**Resultado esperado:**  
Teste passa se o nome for retornado com as iniciais maiúsculas corretamente.

**Link para o arquivo:**  
https://colab.research.google.com/drive/1oKEM0IdM_dQcRXbRZt_IaK2D6rYS1flF?usp=sharing


### Teste 02 – Verificação de respostas da API Agify para múltiplos nomes

**Objetivo:**  
Verificar se a API pública https://api.agify.io retorna status HTTP 200 para várias requisições GET com nomes diferentes e se o nome retornado no JSON corresponde ao nome enviado.

**Biblioteca utilizada:**  
`requests`

**Resultado esperado:**  
Teste passa se todas as requisições retornarem status 200 e o campo `name` do JSON corresponder ao nome enviado (ignorar diferenças de maiúsculas/minúsculas).

**Link para o arquivo:**  
https://colab.research.google.com/drive/1VMLC5dV9aytLpKTVBNeuZEOLFfq_qAST?usp=sharing


### Teste 03 – Verificação de função que identifica números primos

**Objetivo:**  
Testar a função que verifica se um número é primo, validando casos de números primos, não primos e valores limite.

**Biblioteca utilizada:**  
`pytest`

**Resultado esperado:**  
Teste passa se a função retornar `True` para números primos e `False` para números não primos, sem gerar erros.

**Link para o arquivo:**  
https://colab.research.google.com/drive/1DO5rqh7QWuEPy5mI9s_-lGEox72ksppV?usp=sharing
