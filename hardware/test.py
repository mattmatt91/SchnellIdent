data = [1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7450506446842962, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571,
        1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.7434453857670396, 1.7501872265610552, 1.748573164572571, 1.7501872265610552, 1.748573164572571]


def transform_data(data: list, number_of_channels: int):
    new_data = [[] for _ in range(number_of_channels)]
    for i, value in enumerate(data):
        sensor_index = i % number_of_channels
        new_data[sensor_index].append(value)
    return new_data


print(transform_data(data,2))