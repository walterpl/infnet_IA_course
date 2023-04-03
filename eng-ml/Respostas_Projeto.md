# Respostas do questinário do trabalho.

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

R: Todas as ferramentas auxiliam em diferentes partes durante a produção de uma solução IA, começando pelo **MLFlow**, que
é uma ferramente voltada para MLops, a qual nos permite manter o histórico de todos os modelos, seus parâmetros e seus 
resultados de treino, como nos permite testar as modelagens como diferentes funções de um pipeline, para garantir que
todo código da solução seja não apenas compilável, mas também funcional. **Scikit-Learn** é a ferramenta que possui diversos
modelos de ML incluse suas funções auxiliares para tratamentos de dados, e a partir dela que monta-se o modelo. **PyCaret** é
a ferramenta utilizada para construir, testar e escolher o melhor modelo no momento de teste, ela utiliza os recursos do
Scikit-Learn internamente para compilar os modelos e seus resultados são armazenados e catalogados no MLFlow. **StremLit** é a 
porta de saída do modelo para a produção, pois é a partir dele que o modelo deixará o ambiente de desenvolvimento e será enviado
ao ambiente de produção o tornando disponível via API.