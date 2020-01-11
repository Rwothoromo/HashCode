import sys

def knapsack(items, capacity):
    selected_pizzas = []
    possible_count = 0

    for item in items:
        if item not in selected_pizzas:
            possible_count += item
            selected_pizzas.append(item)
            if possible_count > capacity:
                # print(possible_count, selected_pizzas)
                break

    len_selected = len(selected_pizzas)
    for index in range(len_selected):
        if index == 0:
            if possible_count - selected_pizzas[0] <= capacity:
                return [items.index(i) for i in selected_pizzas[1:]]
        elif index < len_selected-1:
            if possible_count - selected_pizzas[index] <= capacity:
                return [items.index(i) for i in ([selected_pizzas[index-1]] + selected_pizzas[index+1:])]
        # if at the last item
        else:
            return [items.index(i) for i in selected_pizzas[:len_selected-1]]



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
        print(result_len)
        print(result_string)

        output_file = open(sys.argv[2], 'w')
        output_file.write("{}\n{}\n".format(result_len, result_string))
