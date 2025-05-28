<h1> Lema do bombeamento </h1>

<h2>O Lema do Bombeamento é uma ferramenta usada na área de Linguagens Formais para ajudar a descobrir se uma linguagem não é regular.
De forma simples, ele diz o seguinte:
Se uma linguagem é regular, ela pode ser reconhecida por um autômato finito, que é uma máquina com memória bem limitada.</h2>

Isso significa que, se a cadeia for muito grande, a máquina vai acabar repetindo algum pedaço da cadeia, porque ela não consegue "lembrar" de tudo.

<h2> Conclusão Fundamentada </h2>
Através da aplicação do lema do bombeamento sobre a linguagem L={anbn∣n≥0}L = \{a^n b^n \mid n \geq 0\}L={anbn∣n≥0}, foi possível verificar, de forma prática, que essa linguagem não é regular.
Durante os testes, o programa realizou todas as divisões possíveis da cadeia w=′aaabbb′w = 'aaabbb'w=′aaabbb′ em x,y,zx, y, zx,y,z, respeitando as condições do lema: ∣xy∣≤p|xy| \leq p∣xy∣≤p e ∣y∣>0|y| > 0∣y∣>0. A cada divisão, foi feita a repetição do segmento yyy para os valores de i=0,1,2,3i = 0, 1, 2, 3i=0,1,2,3. Os resultados mostraram que, ao remover (i=0i=0i=0) ou repetir (i=2,3i=2, 3i=2,3) o trecho yyy, as cadeias resultantes não permaneceram na linguagem, pois perderam a condição essencial de possuir o mesmo número de 'a's seguidos do mesmo número de 'b's.
Essa quebra do lema evidencia que não existe um autômato finito capaz de reconhecer essa linguagem, pois ela exige memória para contar a quantidade de símbolos 'a' e garantir que seja igual à quantidade de 'b', característica que não é possível em autômatos finitos, mas sim em autômatos com pilha (linguagem livre de contexto).
Portanto, a execução do código, fundamentada na aplicação formal do lema do bombeamento, confirma o que é conhecido na teoria de linguagens formais: a linguagem L={anbn∣n≥0}L = \{a^n b^n \mid n \geq 0\}L={anbn∣n≥0} não é regular.
