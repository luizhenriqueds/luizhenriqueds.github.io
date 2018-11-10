## **Detecção de Fraude em transações de cartão de crédito (dataset desbalanceado)** 
Esse projeto utiliza técnicas de Aprendizado de Máquina supervisionado para classificar uma transação usando cartão de crédito como fraudulenta ou genuína. Esse problema, no entanto, não é um problema trivial de classificação, onde treinamos o modelo, fazemos a classificação e validamos a acurácia do mesmo, pois os dados apresentados são desbalanceados, ou seja, uma classe tem muito mais ocorrências que a outra. Se analisarmos, entretanto, isso faz sentido, uma vez que é muito mais comum que uma transação seja genuína do que fraudulenta. Mas, enfim, como abordamos um problema desse tipo?

A primeira restrição é que não podemos utilizar acurácia como métrica de validação, uma vez que mais de 99% das ocorrências do dataset são transações genuínas. Isso quer dizer, em outras palavras, que se um modelo qualquer prever sempre `genuína`, para qualquer transação, teria uma acurácia altíssima e, ao mesmo tempo, seria um modelo pouco útil (a dummy model).

Por esse motivo, o objetivo desse notebook é útilizar abordagens para contornar esse problema e possuir uma métrica de performance que seja realmente válida para esse problema.

Nesse projeto, iremos utilizar diversos algoritmos de classificação da biblioteca `scikit-learn`, técnicas de ajustes de hiperparâmetros, métricas de performance não-sensíveis a dados desbalanceados, validação cruzada e técnicas de oversampling.


## **Dataset**
O dataset utilizado nesse projeto pode ser encontrado no seguinte endereço: https://tinyurl.com/yaffs7gx.

O código desse projeto pode ser encontrado nesse **[endereço](#)** e também no meu perfil no **[Kaggle](https://tinyurl.com/yagjwne9)**.

## **Habilidades aplicadas**
Classificação, Regressão Logística, Gradient Boosting Decision Tree, Random Forest, Cross-validation, SMOTE, Validação de Performance (AUC), Gridsearch
