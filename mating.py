def average_parents(partners, ratio=0.5):
    children = []
    for parent1, parent2 in zip(partners[::2], partners[1::2]):
        for i in range(len(parent1)):
            parent1[i] *= ratio
            parent1[i] += (1-ratio) * parent2[i]
        children.append(parent1)
    return children

