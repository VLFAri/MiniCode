# Specification

## Objective
The objective is to refactor the `contador.py` file which currently uses a global variable to manage a counter. The goal is to encapsulate this functionality within a class named `Contador`. This class should include methods for incrementing the counter (`incrementar`), retrieving the current value of the counter (`valor`), and resetting the counter (`zerar`). Additionally, the existing functions in the module must continue to work by delegating their operations to an instance of the `Contador` class.

## Parameters / Requirements
- **Entradas**: 
  - The `incrementar` method takes an optional parameter `passo` with a default value of 1.
- **Tipos**:
  - The `incrementar` method should accept an integer or float for the `passo` parameter.
  - The `valor` method returns an integer or float representing the current value of the counter.
  - The `zerar` method does not return any value but resets the counter to zero.
- **Restrições**:
  - The `incrementar` method should be able to handle both positive and negative values for the `passo` parameter.
  - The `valor` method should always return the current state of the counter.
  - The `zerar` method should reset the counter to zero regardless of its current state.
- **Regras de Negócio**:
  - The module-level functions should delegate their operations to an instance of the `Contador` class.
  - Multiple instances of the `Contador` class should operate independently of each other.

## Acceptance Criteria
- The `incrementar` method should correctly update the counter based on the `passo` parameter.
- The `valor` method should accurately reflect the current value of the counter.
- The `zerar` method should successfully reset the counter to zero.
- Module-level functions should function as expected when called, effectively using an instance of the `Contador` class.
- Different instances of the `Contador` class should maintain their own independent states without interfering with each other.
- All functionalities should be tested through automated tests to ensure correctness and reliability.