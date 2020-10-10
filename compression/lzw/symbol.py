import bitarray
import bitarray.util


class Symbol:
    def __init__(self, init_value=""):
        self._internal_repr = bitarray.frozenbitarray(init_value)

    def __eq__(self, other):
        """
        Compare two symbols.
        Two instances of Symbol are equal if they hold the same bits.
        If any of the bits at the same position is not the same the result is False.
        If the number of bits differs the result is False (e.g. '000' != '0').
        If the other operand is not a Symbol the result is False.
        :param other: Symbol object to compare with this
        :return: True if the two symbols have the same internal bits.
                 False if they are different or the other operand is not a Symbol
        """
        return isinstance(other, Symbol) and self._internal_repr == other._internal_repr

    def __len__(self):
        """
        :return: the number of bits used to represent this Symbol
        """
        return len(self._internal_repr)

    def __add__(self, other):
        """
        Return a new Symbol holding the bits of the left symbol (self) and the other
        symbol.
        After this the internal representation of this symbol will remain the same.
        :param other: Symbol representing the bits we want to have at the end
        :return: a new Symbol which concatenates the bits from left and right operand
        """
        if not isinstance(other, Symbol):
            raise TypeError("unsupporetd += with type %s" % type(other).__name__)
        ret = Symbol()
        ret._internal_repr = self._internal_repr + other._internal_repr
        return ret

    def __iadd__(self, other):
        """
        Append the bits of the other Symbol at the end of those of this Symbol.
        After this the internal representation will change
        :param other: Symbol whose bits we want to append to this one
        :return: self
        """
        if not isinstance(other, Symbol):
            raise TypeError("unsupporetd += with type %s" % type(other).__name__)
        self._internal_repr = bitarray.frozenbitarray(
            self._internal_repr + other._internal_repr
        )
        return self

    def __repr__(self):
        return repr(self._internal_repr)

    def __getitem__(self, item):
        """
        Return a new Symbol holding the bits requested by means of the subscription
        operator
        :param item: index or range of bits in this Symbol to return as new Symbol
        :return: new Symbol holding only the requested bits
        """
        ret = Symbol()
        ret._internal_repr = self._internal_repr.__getitem__(item)
        return ret

    def __int__(self):
        """
        :return: the bit representation of this Symbol converted to int
        """
        return bitarray.util.ba2int(self._internal_repr)

    def pad_to_len(self, desired_length):
        """
        Add 0s to the internal representation of this Symbol, so that the number of bits
        used matches desired_length
        :param desired_length: the number of bits we want this Symbol to be
                               represented on
        :return: self
        """
        mutable_repr = bitarray.bitarray(self._internal_repr)
        while len(mutable_repr) < desired_length:
            mutable_repr.insert(0, 0)
        self._internal_repr = bitarray.frozenbitarray(mutable_repr)
        return self

    @staticmethod
    def from_dict(mapping, input_string):
        """
        Return a new instance of Symbol holding the representation of input_string
        converted using the provided mapping.
        Input_string is expected to be iterable (not necessarily of type str).
        Mapping is expected to be a dict defining the association
        <type_of_input_elements>->Symbol used to convert each element in the
        input_string iterable.
        :param mapping: mapping between the possible values in input_string to their
                        corresponding Symbol
        :param input_string: iterable
        :return: a new Symbol representing the concatenation of the values in
                 input_string, converted using the mapping
        """
        mapping = {key: val._internal_repr for key, val in mapping.items()}
        val = bitarray.bitarray()
        val.encode(mapping, input_string)
        ret = Symbol()
        ret._internal_repr = bitarray.frozenbitarray(val)
        return ret

    @staticmethod
    def from_int(int_val, bits):
        """
        Return a new instance of Symbol holding the representation of the provided int
        value using the provided amount of bits.
        If bits is not enough to represent the provided int value, OverflowError is
        raised.
        :param int_val: integer to represent as Symbol
        :param bits: number of bits to use to represent the symbol
        :return: a new Symbol representing the provided int value
        :raises: OverflowError if bits is not enough to represent int_val
        """
        ret = Symbol()
        ret._internal_repr = bitarray.util.int2ba(int_val, length=bits)
        return ret
