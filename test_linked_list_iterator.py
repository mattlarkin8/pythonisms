import pytest

from linked_list_iterator import LinkedList

# @pytest.mark.skip("pending")
def test_for_in():

    foods = LinkedList(("apple","banana","cucumber"))

    foods_list = []

    for food in foods:
        foods_list.append(food)

    assert foods_list == ["apple","banana","cucumber"]

# @pytest.mark.skip("pending")
def test_list_comprehension():

    foods = LinkedList(("apple","banana","cucumber"))

    cap_foods = [food.upper() for food in foods]

    assert cap_foods == ["APPLE","BANANA","CUCUMBER"]

# @pytest.mark.skip("pending")
def test_list_cast():

    food_list = ["apple","banana","cucumber"]

    foods = LinkedList(food_list)

    assert list(foods) == food_list

# @pytest.mark.skip("pending")
def test_len():

    num_range = range(1,20+1)

    nums = LinkedList(num_range)

    assert len(nums) == 20

# @pytest.mark.skip("pending")
def test_len_append():
    nums = LinkedList([1])
    nums.append(2)
    nums.append(3)
    actual = nums.__len__()
    expected = 3
    assert actual == expected

# @pytest.mark.skip("pending")
def test_len_insert_before():
    nums = LinkedList([1,2,3])
    nums.insert_before(3,4)
    assert nums.__len__() == 4
    assert nums.__str__() == "{ 1 } -> { 2 } -> { 4 } -> { 3 } -> None"

# @pytest.mark.skip("pending")
def test_len_insert_after():
    nums = LinkedList([1,2,3])
    nums.insert_after(3,4)
    assert nums.__len__() == 4
    assert nums.__str__() == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> None"

# @pytest.mark.skip("pending")
def test_filter():

    nums = LinkedList(range(1,21))

    odds = [num for num in nums if num % 2]

    assert odds == [1,3,5,7,9,11,13,15,17,19]

# @pytest.mark.skip("pending")
def test_next():

    foods = LinkedList(["apple","banana","cucumber"])

    iterator = iter(foods)

    assert next(iterator) == "apple"
    assert next(iterator) == "banana"
    assert next(iterator) == "cucumber"

# @pytest.mark.skip("pending")
def test_stop_iteration():

    foods = LinkedList(["apple","banana","cucumber"])

    iterator = iter(foods)

    with pytest.raises(StopIteration):
        while True:
            food = next(iterator)

# @pytest.mark.skip("pending")
def test_str():
    linked_foods = LinkedList(["apple","banana","cucumber"])
    actual = str(linked_foods)
    expected = "{ apple } -> { banana } -> { cucumber } -> None"
    assert actual == expected

# dunder method tests
# @pytest.mark.skip("pending")
def test_equals():

    lla = LinkedList(["apple","banana","cucumber"])
    llb = LinkedList(["apple","banana","cucumber"])

    assert lla == llb

# @pytest.mark.skip("pending")
def test_get_item():

    foods = LinkedList(["apple","banana","cucumber"])

    assert foods[0] == "apple"

# @pytest.mark.skip("pending")
def test_get_item_out_of_range():

    foods = LinkedList(["apple","banana","cucumber"])

    with pytest.raises(IndexError):
        foods[100]