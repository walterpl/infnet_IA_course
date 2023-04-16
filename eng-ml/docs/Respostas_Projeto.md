# Respostas do questinário do trabalho.

1- A solução criada nesse projeto deve ser disponibilizada em repositório git e disponibilizada em servidor de repositórios (Github (recomendado), Bitbucket ou Gitlab). O projeto deve obedecer o Framework TDSP da Microsoft. Todos os artefatos produzidos deverão conter informações referentes a esse projeto (não serão aceitos documentos vazios ou fora de contexto). Escreva o link para seu repositório. 

R: <https://github.com/walterpl/infnet_IA_course/tree/main/eng-ml>

2- Iremos desenvolver um preditor de arremessos usando duas abordagens (regressão e classificação) para prever se o "Black Mamba" (apelido de Kobe) acertou ou errou a cesta.
Para começar o desenvolvimento, desenhe um diagrama que demonstra todas as etapas necessárias em um projeto de inteligência artificial desde a aquisição de dados, passando pela criação dos modelos, indo até a operação do modelo.'

R:
![Diagram!](wflow_diagram.jpg)

3- Descreva a importância de implementar pipelines de desenvolvimento e produção numa solução de aprendizado de máquinas.

R: Quando um projeto ja está em uso, eventualmente alguma atualização/
correção/bug/modificação se faz necessária, para garantir que 
o desenvolvimento do código futuro não afete o código presente,
o mesmo é desenvolvido de forma isolada do código em uso, que é chamado de produção.
O código em desenvolvimento é criado em um ambiente chamado de desenvolvimento, que normalmente
é um espelho do ambiente de produção, depois de desenvolvido e testado
o mesmo é entregue ao ambiente de produção, normalmente sem a 
percepção do usuário final.

4- Como as ferramentas Streamlit, MLFlow, PyCaret e Scikit-Learn auxiliam na construção dos pipelines 
descritos anteriormente? A resposta deve abranger os seguintes aspectos:

5- Com base no diagrama realizado na questão 2, aponte os artefatos que serão criados ao longo de um projeto.
Para cada artefato, indique qual seu objetivo.

R: Os dataframes que seriam o data.csv, clean_data.parquet, train_base.parquet, test_base.parquet e o modelo
best_model.pckl.

R: Todas as ferramentas auxiliam em diferentes partes durante a produção de uma solução IA, começando pelo **MLFlow**, que
é uma ferramente voltada para MLops, a qual nos permite manter o histórico de todos os modelos, seus parâmetros e seus 
resultados de treino, como nos permite testar as modelagens como diferentes funções de um pipeline, para garantir que
todo código da solução seja não apenas compilável, mas também funcional. **Scikit-Learn** é a ferramenta que possui diversos
modelos de ML incluse suas funções auxiliares para tratamentos de dados, e a partir dela que monta-se o modelo. **PyCaret** é
a ferramenta utilizada para construir, testar e escolher o melhor modelo no momento de teste, ela utiliza os recursos do
Scikit-Learn internamente para compilar os modelos e seus resultados são armazenados e catalogados no MLFlow. **StremLit** é a 
porta de saída do modelo para a produção, pois é a partir dele que o modelo deixará o ambiente de desenvolvimento e será enviado
ao ambiente de produção o tornando disponível via API.

5

6- 

A) Os dados devem estar localizados em "/Data/kobe_dataset.csv"

R: 
![DATA!](dados_gerados.png)

B) A variável shot_made_flag será seu alvo, onde 0 indica que Kobe errou e 1 que a cesta foi realizada. O dataset resultante 
será armazenado na pasta "/Data/processed/data_filtered.parquet". Ainda sobre essa seleção, qual a dimensão resultante 
do dataset?

R: 
![DATA!](dados_gerados.png)
![Original!](parametro_data_Set_completo.png)


C) Explique como a escolha de treino e teste afetam o resultado do modelo final. Quais estratégias ajudam a minimizar
os efeitos de viés de dados.


R: Partindo do pressuposto que a classe está desbalanceada, a separação da mesma diretamente pelo método 80|20 pode 
resultar é uma base de teste enviesada, onde a maioria dos dados pertencem a classe X, resultando em um modelo tendencioso a 
escolher a classe X como resultado, caso a base de teste seja oposta a precisão tenderá a ser baixa, o mesmo para o f1-score entretanto 
talvez o recall seja um pouco maior. Algumas estratégias podem ser adotadas para evitar o vies dos dados desbalanceados, o primeiro
é excluir os dados da classe de maior incidência, caso o resultado final não seja uma base curta, o segundo método seria
gerar valores sintéticos para a classe de menor incidência visando balancear a classe, também podemos excluir a feature caso
o peso dela no modelo seja baixo ou tenha alta correlação com outra feature balanceada e por ultimo a correlação cruzada 
pode amenizar os efeitos da base enviesada pois dividirá a mesma em multiplas partes, efetuará multiplos treinamentos 
testando essas partes menores umas contra as outras.

D) Registre os parâmetros (% teste) e métricas (tamanho de cada base) no MlFlow

R: 
![Original!](test_train_param.png)

7- 
A e B)

![Original](lr_metrics.png)

c) Com os dados separados para treinamento, treine um modelo de classificação do sklearn usando a biblioteca pyCaret. 
A escolha do algoritmo de classificação é livre. Justifique sua escolha.

R: Continuando a utilizar a lib Pycarret, após testar todos os modelos uns contra os outros e utilizar o auto-tunning,
o modelo com melhor resultado foi o Gradient Boosting classifier.

D)  Registre a função custo "log loss" e F1_score para esse novo modelo.

R: ![Original](best_ml_metrics.png)

8- Registre o modelo de classificação e o disponibilize através do MLFlow através de API.
Selecione agora os dados da base de dados original onde shot_type for igual à 3PT Field Goal 
(será uma nova base de dados) e através da biblioteca requests, aplique o modelo treinado. 
Publique uma tabela com os resultados obtidos e indique o novo log loss e f1_score.

R: ![Original](code_request.png)
![Original](class_metric.png)

A) O modelo é aderente a essa nova base? Justifique.

R: Não, o modelo não é capaz de inferir se Kobe conseguiria pontuar a partir da linha de 3 pontos. O fato ocorreu
pois diversas features relacionadas a distancia e posicionamento foram omitidas do treino, pois da perspectiva do modelo
a distancia, latitude, longitude serão outliers para a cesta de 3 pontos e como todas estão acima dos treshold das de 2,
o modelo definiu que Kobe não conseguiria marcar nenhum ponto. 

B) Descreva como podemos monitorar a saúde do modelo no cenário com e sem a disponibilidade da variável resposta para o modelo em operação

R: O caso de dados com labels é mais simples, pois basta frequentemente rodar o modelo contra os novos dados, coletar as métricas
e comparar com o histório, caso um desvio acima do normal aconteça, analisar a qualidade dos dados ou reavalirar os hyperparametros
do modelo se faz necessário. Para o caso onde não existe o label, a análise deve ser feita nos novos dados, os comparando
com os dados históricos em busca de bruscas variações de média, covariância, corelação e etc, vale verificar também
se alguma feature passou a assumir um valor antes inexistente(casos categóricos).

C) Descreva as estratégias reativa e preditiva de retreinamento para o modelo em operação.

R: A preditiva segue conforme mencionado na questão anterior, testes com uma determinada frequência contra a base de
dados em diferentes folds e a medida que esses dados aumentam, diminuem ou mudem, os testes e os resultados históricos desses
sempre apresentaram o comportamento o modelo ao longo do tempo. O caso reativo normalmente se da por reclamação ou aviso
do usuário final e para entender onde o problema ocorreu, faz-se necessário descobrir o porquê da classificação do modelo
para determinada entrada, um teste de shape para verificar o peso de cada featura para a tomada de decisão e a comparação
das features de input com features da base histórica ajudam a verificar a razão de determinada classificação.

9- 