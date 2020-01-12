import sys


def knapsack(items, capacity):
    selected_pizzas = []
    possible_count = 0

    for (index, item) in enumerate(items):
        if not selected_pizzas:
            possible_count += item
            selected_pizzas.append((index, item))

        elif item != selected_pizzas[-1]:
            possible_count += item
            selected_pizzas.append((index, item))

        if possible_count > capacity:
            break

    len_selected = len(selected_pizzas)
    for pizza in selected_pizzas:
        index = pizza[0]
        item = pizza[1]
        if index == 0:
            if possible_count - item <= capacity:
                return [i[0] for i in selected_pizzas[index+1:]]
        elif index < len_selected-1:
            if possible_count - item <= capacity:
                return [i[0] for i in (selected_pizzas[:index] + selected_pizzas[index+1:])]
        # if at the last item
        else:
            return [i[0] for i in selected_pizzas[:len_selected-1]]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as file:
            input_data = file.read()
        lines = input_data.split('\n')
        _capacity = int(lines[0].split()[0])
        _items = [int(item) for item in lines[1].split()]
        result = knapsack(_items, _capacity)

        result_len = len(result)
        result_string = ' '.join(map(str, result))

        output_file = open(sys.argv[2], 'w')
        output_file.write("{}\n{}\n".format(result_len, result_string))
