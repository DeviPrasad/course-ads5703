
## Compound or Composite Objects and their Representation in Python

Our world is replete with objects - static and dynamic/active. Irrespective of their shape, form, or purpose, all objects have **states** and admit **operations**.

As an example, review a few UPI transactions that you have performed using your favorite mobile app.

List the important data elements that describe a typical UPI transaction.

How do we represent the transaction details as a Python object? How do we inspect and modify the state of an object?

Notice that the transaction details represent one composite or compound object.

## Tuples

Tuple is the simplest data type that can be used to group logically related data elements.

This is the documentation for tuples:
https://docs.python.org/3.9/tutorial/datastructures.html#tuples-and-sequences

A tuple object is
- immutable
- a heterogeneous sequence of elements

### Operations on Tuples
Tuples are simple objects. They admit only a few operations:
1. Creating a new instance.
2. Nested tuples.
3. Accessing the elements.
4. Unpacking or destructuring a tuple.
5. Slicing a tuple.

    ```python
    t = (18, ('DSF', 'BI', 'SP',), (12.50, 1.25, 0.05), 18)
    assert t[0] == 18
    assert t[1] == ('DSF', 'BI', 'SP')
    assert t[1] == (('DSF', 'BI', 'SP'))
    assert t[1] != (('DSF', 'BI', 'SP'),)
    assert not (t[1] == (('DSF', 'BI', 'SP'),))
    assert t[2] == (12.5, 1.0, 0.05)
    assert t[2:3] == ((12.5, 1.0, 0.05),)
    ```

6. `count` function.

    ```python
    # count the number of times an element is found
    assert t.count(18) == 2
    assert t.count(1.25) == 0
    assert t[2].count(1.25) == 1
    assert t[2].count(1.25) >= 1
    assert t[2].count(1.25) < 3
    assert t[2].count(1.2501) < 3
    assert t[2].count(1.2501) == 0
    ```

7. `__contains__` function
    ```
        assert 18 in t
        assert t.__contains__(18)
        assert 'DSF' in t[1]
        assert t[1].__contains__('DSF')
        assert 'DSf' not in t[1]
        assert not t[1].__contains__('DSf')
    ```



## Defining Functions in Python
Programming languages have figured out a simple, efficient, and immensely powerful method for bundling code in named logical units called **functions**.

It is useful to relate a Python function to a mathematical notion of function. It is a good starting point for developing intuitions about the behavior of Python functions.

The following code defines a simple function:

```python
def nop():
    pass

nop()
assert nop() is None

```


```python
def increment(x):
    return x+1

increment(100)

assert increment(-1) == 0
assert increment(100) == 101
assert increment(-100) == -99
```

```python
def say_hello():
    print("Hello!")

say_hello()

assert say_hello() is None
```

```python
def new_upi_tx(amount, sender_upi_id, receiver_upi_id):
    return (amount, sender_upi_id, receiver_upi_id)

```
