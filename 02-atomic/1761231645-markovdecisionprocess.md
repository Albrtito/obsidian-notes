---
aliases:
  - markov decision process
  - MDP
tags:
  - ms
---
# markov decision process
> [!info] Intro: 
> Describes states through which a decision-making agent transitions to achieve a goal. Uses variables in the enviroment and previous acctions of the agent and rewards to decide the next thing to do. 

In artificial intelligence it is used to model situations **wher results of actions are uncertain**. Usefull in enviroments where each action might lead to different outcomes. 

>[!example] Dictionary:
> - **FMDP|Finite markov decision process ->** Finite nuber of states or transitions. 
> - **actions ->** The actions are the **things an agent can do**
>   > Again talking about a grid, move in the grid would be an action
> - **states ->** A set of possible "places" an agent can be at given some properties it has
>   >in a grid, the state could be the position of the agent in the grid
> - **reward ->** A number given to the agent after it takes action. Positive, good; negative, bad.
> - **policy|$\Pi$ ->** The agents plan. "If you are in this state take this action". The goal is to find the best policy.


>[!important] Properties:
> - **markov property** -> The probability of each possible value for a state or reward depends **only on the immediately preceding state and action**, nothing earlier. 
> It only matters where we are and where we are going next. Which means that for probability computation we just need to work with the previous states.
> - **deterministic property ->** When given some state or action there are no probabilities involved in reaching some other state or performing some specific action we say that the MDP is deterministic in that matter. It will always do the same thing in that case.
> 

## formal definition:
We can formally define a MDP as:
$$
\begin{align} \\
&\text{States:} \space &S \\
&\text{Model:} \space &T(S,a,S`) \backsim P(S'|S,a) \\
&\text{Actions:} \space &A(S), A \\
&\text{Reward:} \space &R(S), R(S,a), R(S,a,S')
\over\\
&\text{Policy:} \space &\Pi(S) \rightarrow a \\
&&\Pi^\star
\end{align}
$$
**where:**
- **S ->** Set of states
- **T ->** Transition model mapping each state and action to a new state. In the given definition it is also represented as a probability distribution as it may not be that we land in one state with 100% probability but maybe there are different chances for different states. (That is why P is over there, what is the probability of some state S' given the agent its in state S performing action a)
- **R ->** Reward defined as, reward for some state S, rewards given an action and an state, rewards given an initial state S, final state S' and action a. 

  
***
### Up
- [[1762025473-reinforcementlearning|reinforcement learning]]
### Down
- [[1761237890-mdppolicy|policy selection]]
***
