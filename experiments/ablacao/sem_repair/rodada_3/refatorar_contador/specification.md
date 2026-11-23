# Specification

## Objective
The objective is to refactor the `contador.py` file which currently uses a global variable to manage a counter. The goal is to encapsulate this functionality within a class named `Contador`. This class should include methods for incrementing the counter (`incrementar`), retrieving the current value of the counter (`valor`), and resetting the counter (`zerar`). Additionally, the existing functions in the module must continue to work by delegating their operations to an instance of the `Contador` class.

## Parameters / Requirements
- **Entradas**: 
  - The `incrementar` method accepts an optional parameter `passo` with a default value of `1`.
- **Tipos**:
  - The `incrementar` method should accept an integer or float for the `passo` parameter.
  - The `valor` method returns an integer or float representing the current value of the counter.
  - The `zerar` method does not return any value.
- **Restrições**:
  - The `incrementar` method should be able to handle both positive and negative values for the `passo` parameter.
  - The `valor` method should always return the current state of the counter.
  - The `zerar` method should reset the counter to its initial state.
- **Regras de Negócio**:
  - The module-level functions should delegate their operations to an instance of the `Contador` class.
  - Multiple instances of the `Contador` class should operate independently of each other.

## Acceptance Criteria
- The `Contador` class should have three methods: `incrementar`, `valor`, and `zerar`.
- The `incrementar` method should accept an optional `passo` parameter with a default value of `1`.
- The `valor` method should return the current value of the counter.
- The `zerar` method should reset the counter to its initial state.
- The module-level functions should continue to function correctly by calling the corresponding methods on an instance of the `Contador` class.
- Creating multiple instances of the `Contador` class should result in counters that operate independently of one another.
- All functionalities should be tested using automated tests to ensure correctness and reliability.