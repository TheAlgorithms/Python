from typing import Any


def viterbi(
    observations_space: list,
    states_space: list,
    initial_probabilities: dict,
    transition_probabilities: dict,
    emission_probabilities: dict,
) -> list:
    """
        Viterbi Algorithm, to find the most likely path of
        states from the start and the expected output.
        https://en.wikipedia.org/wiki/Viterbi_algorithm
    sdafads
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

        >>> viterbi((), states, start_p, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: There's an empty parameter

        >>> viterbi(observations, (), start_p, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: There's an empty parameter

        >>> viterbi(observations, states, {}, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: There's an empty parameter

        >>> viterbi(observations, states, start_p, {}, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: There's an empty parameter

        >>> viterbi(observations, states, start_p, trans_p, {})
        Traceback (most recent call last):
            ...
        ValueError: There's an empty parameter

        >>> viterbi("invalid", states, start_p, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: observations_space must be a list

        >>> viterbi(["valid", 123], states, start_p, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: observations_space must be a list of strings

        >>> viterbi(observations, "invalid", start_p, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: states_space must be a list

        >>> viterbi(observations, ["valid", 123], start_p, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: states_space must be a list of strings

        >>> viterbi(observations, states, "invalid", trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: initial_probabilities must be a dict

        >>> viterbi(observations, states, {2:2}, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: initial_probabilities all keys must be strings

        >>> viterbi(observations, states, {"a":2}, trans_p, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: initial_probabilities all values must be float

        >>> viterbi(observations, states, start_p, "invalid", emit_p)
        Traceback (most recent call last):
            ...
        ValueError: transition_probabilities must be a dict

        >>> viterbi(observations, states, start_p, {"a":2}, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: transition_probabilities all values must be dict

        >>> viterbi(observations, states, start_p, {2:{2:2}}, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: transition_probabilities all keys must be strings

        >>> viterbi(observations, states, start_p, {"a":{2:2}}, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: transition_probabilities all keys must be strings

        >>> viterbi(observations, states, start_p, {"a":{"b":2}}, emit_p)
        Traceback (most recent call last):
            ...
        ValueError: transition_probabilities nested dictionary all values must be float

        >>> viterbi(observations, states, start_p, trans_p, "invalid")
        Traceback (most recent call last):
            ...
        ValueError: emission_probabilities must be a dict

        >>> viterbi(observations, states, start_p, trans_p, None)
        Traceback (most recent call last):
            ...
        ValueError: There's an empty parameter

    """
    _validation(
        observations_space,
        states_space,
        initial_probabilities,
        transition_probabilities,
        emission_probabilities,
    )
    # Creates data structures and fill initial step
    probabilities: dict = {}
    pointers: dict = {}
    for state in states_space:
        observation = observations_space[0]
        probabilities[(state, observation)] = (
            initial_probabilities[state] * emission_probabilities[state][observation]
        )
        pointers[(state, observation)] = None

    # Fills the data structure with the probabilities of
    # different transitions and pointers to previous states
    for o in range(1, len(observations_space)):
        observation = observations_space[o]
        prior_observation = observations_space[o - 1]
        for state in states_space:
            # Calculates the argmax for probability function
            arg_max = ""
            max_probability = -1
            for k_state in states_space:
                probability = (
                    probabilities[(k_state, prior_observation)]
                    * transition_probabilities[k_state][state]
                    * emission_probabilities[state][observation]
                )
                if probability > max_probability:
                    max_probability = probability
                    arg_max = k_state

            # Update probabilities and pointers dicts
            probabilities[(state, observation)] = (
                probabilities[(arg_max, prior_observation)]
                * transition_probabilities[arg_max][state]
                * emission_probabilities[state][observation]
            )

            pointers[(state, observation)] = arg_max

    # The final observation
    final_observation = observations_space[len(observations_space) - 1]

    # argmax for given final observation
    arg_max = ""
    max_probability = -1
    for k_state in states_space:
        probability = probabilities[(k_state, final_observation)]
        if probability > max_probability:
            max_probability = probability
            arg_max = k_state
    last_state = arg_max

    # Process pointers backwards
    previous = last_state
    result = []
    for o in range(len(observations_space) - 1, -1, -1):
        result.append(previous)
        previous = pointers[previous, observations_space[o]]
    result.reverse()

    return result


def _validation(
    observations_space: Any,
    states_space: Any,
    initial_probabilities: Any,
    transition_probabilities: Any,
    emission_probabilities: Any,
) -> None:
    """
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
    >>> _validation(observations, states, start_p, trans_p, emit_p)

    >>> _validation([], states, start_p, trans_p, emit_p)
    Traceback (most recent call last):
            ...
    ValueError: There's an empty parameter
    """
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
    """
    >>> _validate_not_empty(["a"], ["b"], {"c":0.5},
    ... {"d": {"e": 0.6}}, {"f": {"g": 0.7}})

    >>> _validate_not_empty(["a"], ["b"], {"c":0.5}, {}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: There's an empty parameter
    >>> _validate_not_empty(["a"], ["b"], None, {"d": {"e": 0.6}}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: There's an empty parameter
    """
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
    """
    >>> _validate_lists(["a"], ["b"])

    >>> _validate_lists(1234, ["b"])
    Traceback (most recent call last):
            ...
    ValueError: observations_space must be a list

    >>> _validate_lists(["a"], [3])
    Traceback (most recent call last):
            ...
    ValueError: states_space must be a list of strings
    """
    _validate_list(observations_space, "observations_space")
    _validate_list(states_space, "states_space")


def _validate_list(_object: Any, var_name: str) -> None:
    """
    >>> _validate_list(["a"], "mock_name")

    >>> _validate_list("a", "mock_name")
    Traceback (most recent call last):
            ...
    ValueError: mock_name must be a list
    >>> _validate_list([0.5], "mock_name")
    Traceback (most recent call last):
            ...
    ValueError: mock_name must be a list of strings

    """
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
    """
    >>> _validate_dicts({"c":0.5}, {"d": {"e": 0.6}}, {"f": {"g": 0.7}})

    >>> _validate_dicts("invalid", {"d": {"e": 0.6}}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: initial_probabilities must be a dict
    >>> _validate_dicts({"c":0.5}, {2: {"e": 0.6}}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: transition_probabilities all keys must be strings
    >>> _validate_dicts({"c":0.5}, {"d": {"e": 0.6}}, {"f": {2: 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: emission_probabilities all keys must be strings
    >>> _validate_dicts({"c":0.5}, {"d": {"e": 0.6}}, {"f": {"g": "h"}})
    Traceback (most recent call last):
            ...
    ValueError: emission_probabilities nested dictionary all values must be float
    """
    _validate_dict(initial_probabilities, "initial_probabilities", float)
    _validate_nested_dict(transition_probabilities, "transition_probabilities")
    _validate_nested_dict(emission_probabilities, "emission_probabilities")


def _validate_nested_dict(_object: Any, var_name: str) -> None:
    """
    >>> _validate_nested_dict({"a":{"b": 0.5}}, "mock_name")

    >>> _validate_nested_dict("invalid", "mock_name")
    Traceback (most recent call last):
            ...
    ValueError: mock_name must be a dict
    >>> _validate_nested_dict({"a": 8}, "mock_name")
    Traceback (most recent call last):
            ...
    ValueError: mock_name all values must be dict
    >>> _validate_nested_dict({"a":{2: 0.5}}, "mock_name")
    Traceback (most recent call last):
            ...
    ValueError: mock_name all keys must be strings
    >>> _validate_nested_dict({"a":{"b": 4}}, "mock_name")
    Traceback (most recent call last):
            ...
    ValueError: mock_name nested dictionary all values must be float
    """
    _validate_dict(_object, var_name, dict)
    for x in _object.values():
        _validate_dict(x, var_name, float, True)


def _validate_dict(
    _object: Any, var_name: str, value_type: type, nested: bool = False
) -> None:
    """
    >>> _validate_dict({"b": 0.5}, "mock_name", float)

    >>> _validate_dict("invalid", "mock_name", float)
    Traceback (most recent call last):
            ...
    ValueError: mock_name must be a dict
    >>> _validate_dict({"a": 8}, "mock_name", dict)
    Traceback (most recent call last):
            ...
    ValueError: mock_name all values must be dict
    >>> _validate_dict({2: 0.5}, "mock_name",float, True)
    Traceback (most recent call last):
            ...
    ValueError: mock_name all keys must be strings
    >>> _validate_dict({"b": 4}, "mock_name", float,True)
    Traceback (most recent call last):
            ...
    ValueError: mock_name nested dictionary all values must be float
    """
    if not isinstance(_object, dict):
        raise ValueError(f"{var_name} must be a dict")
    if not all(isinstance(x, str) for x in _object):
        raise ValueError(f"{var_name} all keys must be strings")
    if not all(isinstance(x, value_type) for x in _object.values()):
        nested_text = "nested dictionary " if nested else ""
        raise ValueError(
            f"{var_name} {nested_text}all values must be {value_type.__name__}"
        )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
