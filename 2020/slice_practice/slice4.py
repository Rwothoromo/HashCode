import sys


def knapsack(items, capacity, item_count):
    selected_pizzas = []
    possible_count = 0
    return_list = []

    for index in range(item_count):
        item = items[index]

        if not selected_pizzas:
            possible_count += item
            selected_pizzas.append((index, item))

        elif item != selected_pizzas[-1]:
            possible_count += item
            selected_pizzas.append((index, item))

        if possible_count > capacity:
            next_index = index + 1
            if next_index < item_count:
                next_item = items[next_index]
                selected_pizzas.pop()
                possible_count -= item
                possible_count += next_item
                selected_pizzas.append((next_index, next_item))
            break

    if possible_count <= capacity:
        return_list = [i[0] for i in selected_pizzas]

    for pizza_index in range(len(selected_pizzas)):
        pizza = selected_pizzas[pizza_index]
        item = pizza[1]

        if possible_count - item <= capacity:
            selected_pizzas.pop(pizza_index)
            possible_count -= item
            return_list = [i[0] for i in selected_pizzas]
            break

    # determine what pizza to replace in the list
    last_index = return_list[-1]
    pending_capacity = capacity - possible_count
    if pending_capacity > 0:
        sought_value = min(items[:last_index],
                           key=lambda x: abs(x-pending_capacity))
        loop_index = items.index(sought_value)
        if loop_index > 0:
            for new_index in range(loop_index, -1, -1):
                new_item = items[new_index]
                if new_index not in return_list:
                    new_count = possible_count + new_item
                    if new_count <= capacity:
                        possible_count = new_count
                        selected_pizzas.append((new_item, new_index))
                        return_list.append(new_index)
                if possible_count > capacity:
                    break

    return return_list


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as file:
            input_data = file.read()
        lines = input_data.split('\n')
        _capacity = int(lines[0].split()[0])
        _item_count = int(lines[0].split()[1])
        _items = [int(item) for item in lines[1].split()]
        result = knapsack(_items, _capacity, _item_count)

        result_len = len(result)
        result_string = ' '.join(map(str, result))

        output_file = open(sys.argv[2], 'w')
        output_file.write("{}\n{}\n".format(result_len, result_string))
