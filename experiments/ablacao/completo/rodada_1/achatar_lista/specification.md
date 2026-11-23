# Specification

## Objective
The primary objective is to create a Python script named `achatar.py` that includes a function `achatar(items)` capable of flattening nested lists and tuples of any depth into a single-level list while preserving the order of elements. The function should not flatten strings, treating them as single elements.

## Parameters / Requirements
- **Input**: The function `achatar(items)` accepts a single parameter `items`, which can be a nested structure containing lists, tuples, and strings.
- **Output**: Returns a flat list containing all elements from the input structure in the same order they appeared, with strings treated as individual elements.
- **Types**:
  - `items`: Can be a list or tuple containing other lists, tuples, and strings.
  - Output type: List.
- **Constraints**:
  - The function must handle arbitrarily deep nesting.
  - Strings within the input structure should not be split; they should remain as single elements in the output list.
  
## Acceptance Criteria
- The function correctly flattens nested structures into a single-level list.
- Strings within the nested structure are not flattened but remain as single elements in the output list.
- The order of elements in the output list matches their order in the input structure.
- Test cases should include:
  - A nested list containing integers, strings, and further nested lists/tuples.
  - Edge cases such as empty lists, single-element lists, and lists containing only strings.
- The function passes automated tests verifying the above criteria.

Arquivos do projeto:
(vazio)