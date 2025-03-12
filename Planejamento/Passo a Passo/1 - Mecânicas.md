# Iniciando o Projeto:

- [x] Criar repositório
- [x] Criar pastas:
	- Texturas
	- Modelos
	- Scripts
	- Sons
- [x] Configurar Projeto.blend
- [x] Commit **Inicial**

---
# Sistemas de movimentação do player
Aqui iremos usar uma psicologia diferenciada para o movimento do personagem, para conseguir replicar a forma base de como funcionaria a gravidade do mundo. Primeiro que, quem se move não é o jogador, é o planeta que gira em seu próprio eixo, dando a impressão de movimento.
	%% As coisas acabaram mudando e eu preferi por um Empty que rotaciona o jogador ao invés do planeta, pois pensei que seria muito mais prático. %%

- [x] Criar o mundo, que gira no proprio eixo.
- [x] Câmera e configurar a vista.
- [x] Criar um cubo, como referência para o player.

![[Pasted image 20250309190103.png]]
- - - 
# Ataque do player (Mecânica principal):
O player irá usar um ataque do estilo projétil, uma arma a laser ou algo do tipo, para matar os inimigos pelo cenário. Ele irá atacar usando a tecla Z ou o botão esquerdo do Mouse e irá jogar o projetil para uma das direções apontadas usando WASD (W: frente, S: Trás, A: Esquerda, D: Direito) Tendo que se posicionar para conseguir acertar os inimigos.

## Como vai funcionar:
Para que a gravidade do planeta seja respeitada e o projétil não seja jogado no espaço, o objeto do projetil será parenteado em um Empty que ficará no centro do planeta que irá se rotacionar, dando a impressão de gravidade.

- [x] Criar o sistema de tiro.
- [x] Criar o empty que simula a gravidade.

![[Pasted image 20250309194716.png]]

O projétil só se destrói se colidir com algo, sendo assim:
	**Se colidir com o inimigo:** Destrói o inimigo
	**Se colidir com uma pedra ou outro projétil**: Destrói a si mesmo
	**Se colidir com o Jogador:** Tira vidas do jogador

Por isso além de ter que tomar cuidado com os inimigos, o jogador terá que ter cuidado com os próprios projeteis. Isso evita que os jogadores encham o mundo de projeteis e sejam mais estratégicos na hora de atacar. 

- [x] Sistema de vida do jogador (3 vidas)
- [x] Programar as colisões do projetil
- - -
# Inimigos:
Os inimigos terão uma inteligência artificial bem simples, eles irão aparecer e ficarão parados ou andando pelo mapa, se o jogador estiver no campo de visão deles, eles irão caça-lo.

### Movimentos padrões:
- [ ] Fazer o inimigo se mover apenas para frente (Y) 
- [ ] Girar 90 ou -90 no eixo Z aleatoriamente.
### Se avistar o jogador:
- [ ] Fazer o inimigo perseguir o jogador em uma velocidade maior que a padrão, mas não muito assustadora.
- [ ] O inimigo some e tira vida do jogador caso colida com ele.

	Além disso, não podemos esquecer que caso o inimigo colida com o projetil ele irá sumir...

- [ ] O inimigo some caso ele se colida com o projétil do player.

%% Acredito que aqui é o final da mecânica principal, mas vou deixar em aberto, caso no meio do desenvolvimento eu tenha que adicionar coisas a mais. %%

