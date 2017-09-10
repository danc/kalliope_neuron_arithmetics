# Arithmetics

## Synopsis 

Kalliope neuron which asks some random basic integer arithmetics like n1 operator n2 where n1, n2 are integers and operator is "+", "-", "\*" or "/" such that result of n1 operator n2 is less than a given number maxresult.

## Installation

```
kalliope install --git-url https://github.com/1account/kalliope_neuron_arithmetics.git
```

## Options

| parameter | required | default | choices                     | comment                                         |
|-----------|----------|---------|-----------------------------|-------------------------------------------------|
| maxresult | YES      | None    |                             | n1 operator n2 < maxresult                      |
| operator  | NO       | Random  |                             | "+", "-", "\*" or "/"                           |

## Return Values

| Name                        | Description                                | Type   | sample                 |
|-----------------------------|--------------------------------------------|--------|------------------------|
| result                      | n1 operator n2                             | String | 7 + 5 -> 12            |
| operator                    | Operator                                   | String | "+", "-", "\*" or "/"  |                   

## Synapses example


```
  - name: "arithmetics"
    signals:
      - order: "Ask me some math"
    neurons:
     - arithmetics:
          maxresult: "100"
          operator: "+"
          file_template: templates/arithmetics_en_template.j2
          kalliope_memory:
            result: "{{result}}"
     - neurotransmitter:
          from_answer_link:
            - synapse: "synapse-correct"
              answers:
                - "I guess {{ kalliope_memory['result'] }}"
          default: "synapse-not-correct"

  - name: "synapse-correct"
    signals:
      - order: "synapse-correct"
    neurons:
      - say:
          message:
              - "Superb!"
              - "Perfect!"
              - "Correct!"

  - name: "synapse-not-correct"
    signals:
      - order: "synapse-not-correct"
    neurons:
      - say:
          message:
              - "That is wrong, {{ kalliope_memory['result'] }} is the correct answer"
```

## Template

```
{% set operator_spoken = {
    "+": "plus",
    "-": "minus",
    "*": "times",
    "/": "divided by"
    }[operator] | default("") -%}

What is {{n_1}} {{operator_spoken}} {{n_2}}?
```


## Notes
