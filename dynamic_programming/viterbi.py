from collections.abc import Callable
from typing import Any, Dict, List, Tuple


def viterbi(
    observations_space: list[str],
    states_space: list[str],
    initial_probabilities: dict[str, float],
    transition_probabilities: dict[str, dict[str, float]],
    emission_probabilities: dict[str, dict[str, float]],
) -> list[str]:
    """
    Viterbi Algorithm, to find the most likely path of
    states from the start and the expected output.
    https://en.wikipedia.org/wiki/Viterbi_algorithm

    Wikipedia example
    >>> observations = ["normal", "cold", "dizzy"]
    >>> states = ["Healthy", "Fever"]
    >>> start_p = {"Healthy": 0.6, "Fever": 0.4}
    >>> trans_p = {
    ...     "Healthy": {"Healthy": 0.7, "Fever": 0.3},
    ...     "Fever": {"Healthy": 0.4, "Fever": 0.6},
    ... }
    >>> emit_p = {
    ...     "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
    ...     "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
    ... }
    >>> viterbi(observations, states, start_p, trans_p, emit_p)
    ['Healthy', 'Healthy', 'Fever']

    # >>> viterbi((), states, start_p, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: There's an empty parameter
    #
    # >>> viterbi(observations, (), start_p, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: There's an empty parameter
    #
    # >>> viterbi(observations, states, {}, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: There's an empty parameter
    #
    # >>> viterbi(observations, states, start_p, {}, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: There's an empty parameter
    #
    # >>> viterbi(observations, states, start_p, trans_p, {})
    # Traceback (most recent call last):
    #     ...
    # ValueError: There's an empty parameter
    #
    # >>> viterbi("invalid", states, start_p, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: observations_space must be a list
    #
    # >>> viterbi(("valid", 123), states, start_p, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: observations_space must be a list of strings
    #
    # >>> viterbi(observations, "invalid", start_p, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: states_space must be a list
    #
    # >>> viterbi(observations, ("valid", 123), start_p, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: states_space must be a list of strings
    #
    # >>> viterbi(observations, states, "invalid", trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: initial_probabilities must be a dict
    #
    # >>> viterbi(observations, states, {2:2}, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: initial_probabilities all keys must be strings
    #
    # >>> viterbi(observations, states, {"a":2}, trans_p, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: initial_probabilities all values must be float
    #
    # >>> viterbi(observations, states, start_p, "invalid", emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: transition_probabilities must be a dict
    #
    # >>> viterbi(observations, states, start_p, {"a":2}, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: transition_probabilities all values must be dict
    #
    # >>> viterbi(observations, states, start_p, {2:{2:2}}, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: transition_probabilities all keys must be strings
    #
    # >>> viterbi(observations, states, start_p, {"a":{2:2}}, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: transition_probabilities all keys must be strings
    #
    # >>> viterbi(observations, states, start_p, {"a":{"b":2}}, emit_p)
    # Traceback (most recent call last):
    #     ...
    # ValueError: transition_probabilities nested dictionary all values must be float
    #
    # >>> viterbi(observations, states, start_p, trans_p, "invalid")
    # Traceback (most recent call last):
    #     ...
    # ValueError: emission_probabilities must be a dict
    #
    # >>> viterbi(observations, states, start_p, trans_p, None)
    # Traceback (most recent call last):
    #     ...
    # ValueError: There's an empty parameter

    """
    _validation(
        observations_space,
        states_space,
        initial_probabilities,
        transition_probabilities,
        emission_probabilities,
    )
    # Creates data structures and fill initial step
    pointers, probabilities = _initialise_probabilities_and_pointers(
        observations_space,
        states_space,
        initial_probabilities,
        emission_probabilities,
    )

    # Function for the process forward calculations
    def _prior_state(observation: str, prior_observation: str, state: str) -> Callable:
        def _func(k_state: str) -> float:
            return (
                probabilities[(k_state, prior_observation)]
                * transition_probabilities[k_state][state]
                * emission_probabilities[state][observation]
            )

        return _func

    # Fills the data structure with the probabilities of
    # different transitions and pointers to previous states
    _process_forward(
        observations_space, states_space, _prior_state, probabilities, pointers
    )

    # The final observation
    last_state = _extract_final_state(observations_space, states_space, probabilities)

    # Process pointers backwards
    return _extract_best_path(observations_space, last_state, pointers)


def _validation(
    observations_space: Any,
    states_space: Any,
    initial_probabilities: Any,
    transition_probabilities: Any,
    emission_probabilities: Any,
) -> None:
    _validate_not_empty(
        observations_space,
        states_space,
        initial_probabilities,
        transition_probabilities,
        emission_probabilities,
    )
    _validate_lists(observations_space, states_space)
    _validate_dicts(
        initial_probabilities, transition_probabilities, emission_probabilities
    )


def _validate_not_empty(
    observations_space: Any,
    states_space: Any,
    initial_probabilities: Any,
    transition_probabilities: Any,
    emission_probabilities: Any,
) -> None:
    if not all(
        [
            observations_space,
            states_space,
            initial_probabilities,
            transition_probabilities,
            emission_probabilities,
        ]
    ):
        raise ValueError("There's an empty parameter")


def _validate_lists(observations_space: Any, states_space: Any) -> None:
    _validate_list(observations_space, "observations_space")
    _validate_list(states_space, "states_space")


def _validate_list(_object: Any, var_name: str) -> None:
    if not isinstance(_object, list):
        raise ValueError(f"{var_name} must be a list")
    else:
        for x in _object:
            if not isinstance(x, str):
                raise ValueError(f"{var_name} must be a list of strings")


def _validate_dicts(
    initial_probabilities: Any,
    transition_probabilities: Any,
    emission_probabilities: Any,
) -> None:
    _validate_dict(initial_probabilities, "initial_probabilities", float)
    _validate_nested_dict(transition_probabilities, "transition_probabilities")
    _validate_nested_dict(emission_probabilities, "emission_probabilities")


def _validate_nested_dict(_object: Any, var_name: str) -> None:
    _validate_dict(_object, var_name, dict)
    for x in _object.values():
        _validate_dict(x, var_name, float, True)


def _validate_dict(_object: Any, var_name: str, value_type: type, nested: bool = False):
    if not isinstance(_object, dict):
        raise ValueError(f"{var_name} must be a dict")
    if not all(isinstance(x, str) for x in _object):
        raise ValueError(f"{var_name} all keys must be strings")
    if not all(isinstance(x, value_type) for x in _object.values()):
        nested_text = "nested dictionary " if nested else ""
        raise ValueError(
            f"{var_name} {nested_text}all values must be {value_type.__name__}"
        )


def _initialise_probabilities_and_pointers(
    observations_space: list[str],
    states_space: list[str],
    initial_probabilities: dict[str, float],
    emission_probabilities: dict[str, dict[str, float]],
) -> tuple[dict, dict]:
    probabilities = {}
    pointers = {}
    for state in states_space:
        observation = observations_space[0]
        probabilities[(state, observation)] = (
            initial_probabilities[state] * emission_probabilities[state][observation]
        )
        pointers[(state, observation)] = None
    return pointers, probabilities


def _process_forward(
    observations_space: list[str],
    states_space: list[str],
    _prior_state: Callable,
    probabilities: dict,
    pointers: dict,
) -> None:
    for o in range(1, len(observations_space)):
        observation = observations_space[o]
        prior_observation = observations_space[o - 1]
        for state in states_space:
            arg_max = _arg_max(
                _prior_state(observation, prior_observation, state), states_space
            )

            probabilities[(state, observation)] = _prior_state(
                observation, prior_observation, state
            )(arg_max)
            pointers[(state, observation)] = arg_max


def _extract_final_state(observations_space, states_space, probabilities):
    final_observation = observations_space[len(observations_space) - 1]

    def _best_final_state(k_state: str) -> float:
        return probabilities[(k_state, final_observation)]

    last_state = _arg_max(_best_final_state, states_space)
    return last_state


def _extract_best_path(
    observations_space: list[str],
    last_observation: str,
    pointers: dict,
) -> list[str]:
    previous = last_observation
    result = []
    for o in range(len(observations_space) - 1, -1, -1):
        result.append(previous)
        previous = pointers[previous, observations_space[o]]
    result.reverse()
    return result


def _arg_max(prior_state: Callable, states_space: list[str]) -> str:
    arg_max = ""
    max_probability = -1
    for k_state in states_space:
        probability = prior_state(k_state)
        if probability > max_probability:
            max_probability = probability
            arg_max = k_state
    return arg_max


if __name__ == "__main__":
    from doctest import testmod

    testmod()
