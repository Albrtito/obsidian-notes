---
aliases:
- Function Approximation in Reinforcement Learning
tags:
- reinforcementlearning
- artificial
---
# Function Approximation in Reinforcement Learning
> [!info] Intro: 
> Function approximation is a method in reinforcement learning to estimate value functions for large or continuous state spaces by using parametric models, such as neural networks, instead of tabular representations. This enables generalization to unseen states and reduces memory requirements.

>[!example]- Dictionary:
> - **function approximation ->** Using a parametric model (e.g., neural network) to approximate the value function Q(s,a) or V(s) instead of storing a table for every state-action pair
> - **bootstrapping ->** Updating value estimates based on other estimates, as in temporal difference learning
> - **off-policy learning ->** Learning from a policy different from the one being followed (e.g., Q-Learning)
> - **on-policy learning ->** Learning from the same policy being executed (e.g., SARSA)
> - **experience replay ->** Storing past experiences in a buffer and sampling them randomly for training to break correlations
> - **target network ->** A separate neural network used to compute target Q-values in Deep Q-Learning to stabilize training

>[!important] Properties:
> - **Handles large state spaces:** Avoids storing Q-tables for every possible state-action pair by generalizing with a model
> - **Generalization:** Can estimate values for unseen states based on learned parameters
> - **Efficiency:** Fewer parameters than tabular methods, enabling scalability
> - **Challenges:** Can lead to instability (deadly triad: bootstrapping + off-policy + function approximation)
> - **Deep Q-Learning:** Combines Q-Learning with deep neural networks, using techniques like experience replay and target networks to address instability

## Why Function Approximation?
In reinforcement learning, tabular methods like Q-Learning store Q-values for every state-action pair. For large or continuous state spaces (e.g., Atari games with pixel inputs), this becomes infeasible due to memory and computation constraints. Function approximation approximates Q(s,a) using a parametric model, such as a neural network, with fewer parameters than the number of states.

## From Tabular to Approximate Q-Learning
Q-Learning updates Q-values using:
Q(s,a) ← Q(s,a) + α \[r + γ max_a' Q(s',a') - Q(s,a)]

With function approximation, Q(s,a) ≈ Q(s,a; θ), where θ are the parameters. The update becomes a gradient descent step to minimize the loss between predicted and target Q-values.

## Deep Q-Learning
Deep Q-Learning uses a deep neural network (DQN) to approximate Q-values. Key innovations:
- **Experience Replay:** Store transitions (s,a,r,s') in a buffer and sample mini-batches randomly to reduce correlation and improve stability.
- **Target Network:** Use a separate network for computing targets, updated periodically, to prevent moving targets during training.

This allows learning from high-dimensional inputs like images, achieving human-level performance in games like Atari.

## Deadly Triad
Combining bootstrapping (updating based on estimates), off-policy learning (Q-Learning), and function approximation can cause divergence. Mitigations include experience replay and target networks.

***
### Up
- [[1762025473-reinforcementlearning|reinforcement learning]]
- [[1762205273-temporaldifferencelearning|temporal difference learning]]
### Down
- [[1762271227-qlearning|Q-Learning]]
- [[1762270792-sarsa|SARSA]]
***