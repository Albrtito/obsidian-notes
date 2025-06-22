# Differential Calculus - 3-Day Study Guide
*Based on UC3M DiffCalc Course Content and Notes*

## Overview
This guide covers essential differential calculus concepts organized for intensive 3-day study preparation, based on your UC3M DiffCalc course materials and personal notes.

**Course Reference**: UC3M Applied Differential Calculus OCW - http://ocw.uc3m.es/mod/page/view.php?id=3076

**Key Terminology**:
- **DE** → Differential equation
- **ODE** → Ordinary differential Equation  
- **PDE** → Partial differential equation
- **IVP** → Initial Value Problem
- **IC** → Initial Conditions

---

## Day 1: Foundations and Introduction to Differential Equations

### 1. What are Differential Equations?
- **Definition**: Relations between a function and its derivatives
- **Example**: $x'' + 8x' + 7x = 0$ (relates x(t) and its derivatives)
- **Goal**: Find the function that satisfies the equation
- **Key Insight**: Easy to check solutions by substitution

### 2. Family of Solutions
- **Important Concept**: DEs usually have infinite solutions (family of functions)
- **Reason**: Constants derive to 0, so any constant value works
- **Example**: For $x'' = 2t$, solution is $x(t) = \frac{t^3}{3} + c_1t + c_2$
- **Always check for**: Lost solutions in DEs

### 3. Classification of Differential Equations

#### A. ODEs vs PDEs
- **ODE**: Function depends on ONE independent variable → $f(x)$
  - Uses ordinary derivatives
- **PDE**: Function depends on MULTIPLE independent variables → $f(x_1,x_2,...,x_n)$
  - Uses partial derivatives

#### B. Properties of DEs
- **Order**: Highest order derivative in the equation
  - $f(x) + 3f'(x) + f''(x) = 3$ → Order 2
  - $f(x) + 3f'(x) = 3$ → Order 1

- **Linearity**: DE is linear when unknown and derivatives satisfy:
  1. Exponent equals 1
  2. No products or ratios between them  
  3. Not composed with other functions
  - Example: $-y + yy' = 3$ → Non-linear (product between solution and derivative)

### 4. Solving Methods Overview
- **Analytic methods**: For specific types (mostly linear DEs)
- **Numeric methods**: When analytic methods fail
- **UC3M Course Focus**: Analytic methods with brief mention of numeric

### Key Practice Problems Day 1:
- Classify DEs as ODE/PDE, determine order and linearity
- Verify solutions by substitution
- Understand the concept of family of solutions
- Identify different types of DEs from examples

---

## Day 2: Ordinary Differential Equations (ODEs) - Solution Methods

### 1. Separable ODEs
- **Form**: $M(x)dx + N(y)dy = 0$
  - M(x) is function of x only
  - N(y) is function of y only

- **Method**:
  1. Separate variables: $M(x)dx = -N(y)dy$
  2. Integrate both sides: $\int M(x)dx = \int -N(y)dy$
  3. Solve for y (implicit solution)

- **Example**: $\frac{dy}{dx} = x(y-1)$
  - Separate: $\frac{dy}{y-1} = xdx$
  - Integrate: $\ln|y-1| = \frac{x^2}{2} + C$
  - Solution: $y(t) = 1 + Ce^{x^2/2}$

### 2. First Order Linear ODEs
- **Standard Form**: $\frac{dy}{dx} + P(x)y = f(x)$

- **Quick Method**:
  1. Find integrating factor: $u = e^{\int P(x)dx}$
  2. Solution given by: $\frac{d[u \cdot y]}{dx} = f(x) \cdot u$
  3. Integrate both sides: $u \cdot y = \int f(x) \cdot u \, dx$

- **General Solution Process**:
  1. Solve homogeneous part: $u_h = C_1 e^{-\int \frac{a_0}{a_1}dx}$
  2. Find particular solution using integrating factor
  3. General solution: $u(x) = u_h + u_p$ (superposition principle)

### 3. Exact ODEs
- **Form**: $M(x,y)dx + N(x,y)dy = 0$
- **Condition for Exactness**: $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
- **Solution**: Find function F(x,y) such that $\frac{\partial F}{\partial x} = M$ and $\frac{\partial F}{\partial y} = N$

### 4. Homogeneous ODEs (Substitution Method)
- **Form**: Functions where $f(tx,ty) = t^n f(x,y)$
- **Method**: Use substitution $v = \frac{y}{x}$ to convert to separable form

### Key Practice Problems Day 2:
- Solve separable ODEs with various functions
- Apply integrating factor method to first-order linear ODEs
- Work through complete examples with initial conditions
- Practice identifying which method to use for different ODE types

---

## Day 3: Advanced Topics - Systems, Laplace Transform, and PDEs

### 1. Systems of First-Order ODEs
- **General Form**: 
  $$\frac{du_1}{dt} = f_1(u_1,...,u_n,t)$$
  $$\frac{du_2}{dt} = f_2(u_1,...,u_n,t)$$
  $$...$$
  $$\frac{du_n}{dt} = f_n(u_1,...,u_n,t)$$

- **Linear Systems**: $\frac{du}{dt} = A(t)u + F(t)$
  - u is vector of functions
  - A is coefficient matrix
  - F(t) is vector of independent terms

- **Autonomous vs Non-autonomous**:
  - **Autonomous**: Functions $f_i$ don't depend on t
  - **Non-autonomous**: Functions $f_i$ depend on t
  - Any non-autonomous system of order n = autonomous system of order (n+1)

- **Solution for Constant Coefficients**:
  - Look for solutions of form: $u(t) = Ue^{\lambda t}$
  - Leads to eigenvalue problem: $AU = \lambda U$
  - General solution: $u(t) = \sum_{j=1}^n c_j e^{\lambda_j t}\Phi_j$

### 2. Laplace Transform
- **Definition**: $\mathcal{L}\{f(t)\} = \int_0^{\infty} e^{-st} f(t) dt = F(s)$

- **Key Properties**:
  - **Linearity**: $\mathcal{L}\{c_1f_1(t) + c_2f_2(t)\} = c_1\mathcal{L}\{f_1(t)\} + c_2\mathcal{L}\{f_2(t)\}$
  - **Transform of derivatives**: 
    - $\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0)$
    - $\mathcal{L}\{f''(t)\} = s^2\mathcal{L}\{f(t)\} - sf(0) - f'(0)$

- **Common Transforms**:
  - $\mathcal{L}\{1\} = \frac{1}{s}$ (s > 0)
  - $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$ (s > a)
  - $\mathcal{L}\{\sin(at)\} = \frac{a}{s^2+a^2}$ (s > 0)

- **Application**: Transform IVP ODE to algebraic equation, solve, then inverse transform

### 3. Partial Differential Equations (PDEs)
- **Definition**: Involve functions depending on 2+ independent variables
- **Example**: $u(x,t)$ with partial derivatives

- **Course Focus**: Three main models
  - **Heat Equation**: Models heat conduction
  - **Wave Equation**: Models wave propagation  
  - **Laplace Equation**: Models potential fields

- **Solution Method**: Separation of variables
  - Assume solution form: $u(x,t) = X(x)T(t)$
  - Substitute and separate variables
  - Solve resulting ODEs

- **Key Point**: PDEs are usually very difficult to solve analytically
  - Most real applications use numerical methods
  - Course covers only basic analytical approach

### Key Practice Problems Day 3:
- Solve 2×2 systems using eigenvalue method
- Apply Laplace transform to solve IVPs
- Practice separation of variables for simple PDEs
- Work with heat and wave equation examples

---

## Quick Reference Formulas

### ODE Solution Methods
| Type | Form | Method |
|------|------|--------|
| Separable | $M(x)dx + N(y)dy = 0$ | Separate and integrate |
| First-order Linear | $y' + P(x)y = f(x)$ | Integrating factor $e^{\int P(x)dx}$ |
| Exact | $M dx + N dy = 0$ | Check $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ |
| Homogeneous | $y' = f(\frac{y}{x})$ | Substitution $v = \frac{y}{x}$ |

### Laplace Transform Pairs
| Function | Transform |
|----------|-----------|
| $1$ | $\frac{1}{s}$ |
| $e^{at}$ | $\frac{1}{s-a}$ |
| $\sin(at)$ | $\frac{a}{s^2+a^2}$ |
| $\cos(at)$ | $\frac{s}{s^2+a^2}$ |
| $f'(t)$ | $sF(s) - f(0)$ |
| $f''(t)$ | $s^2F(s) - sf(0) - f'(0)$ |

---

## Study Tips
- **Day 1**: Focus on understanding concepts and classification
- **Day 2**: Practice solving different types of ODEs systematically
- **Day 3**: Work on more complex problems and applications
- **Throughout**: Always verify solutions by substitution
- **Key Resource**: UC3M OCW materials and provided PDF references
- **Exam Prep**: Practice with previous exam problems from your collection

## Links to Your Notes
- [[20240208 - 000000 - Definition - Differential Equations]]
- [[20240307 - 000000 - ODEs]]
- [[20240528 - 121302 - First order linear ODE]]
- [[20240528 - 110528 - Separable ODEs]]
- [[Systems of First-Order ODEs]]
- [[The Laplace transform]]
- [[20240418 - 193416 - Partial Differential Equations (PDEs)]]
