def ratio(coordinate_1, coordinate_2):
    if coordinate_1 is None:
        return None
    delta_x = coordinate_2[0] - coordinate_1[0]
    delta_y = coordinate_2[1] - coordinate_1[1]
    if delta_x == 0:
        return float('inf')
    return delta_y / delta_x


class Solution(object):
    def outerTrees(self, trees):
        trees.sort()
        finish_tree_index = len(trees) - 1

        def stop_for_tree(
                trees: List[List[int]], previous_tree: Optional[List[int]], current_tree_index: int,
                next_tree_index: Optional[int], trees_reversed: bool, ans: set
        ):
            current_tree = trees[current_tree_index]
            if current_tree_index == finish_tree_index:
                ans.add(tuple(current_tree))
                return current_tree_index, current_tree
            if next_tree_index is not None:
                next_tree = trees[next_tree_index]
            else:
                next_tree_index, next_tree = self.get_next_tree(trees, current_tree_index, current_tree, trees_reversed)
            ratio_1 = ratio(previous_tree, current_tree)
            ratio_2 = ratio(current_tree, next_tree)
            if ratio_1 is not None and (ratio_2 < ratio_1):
                print('Invalid ratio')
                return next_tree_index, next_tree
            cycle_counter = 0
            while True:
                cycle_counter += 1
                next_tree_index, next_tree = stop_for_tree(trees, current_tree, next_tree_index,
                                                           None, trees_reversed, ans)
                ratio_1 = ratio(previous_tree, current_tree)
                ratio_2 = ratio(current_tree, next_tree)
                if (ratio_1 is not None and ratio_2 < ratio_1):
                    return next_tree_index, next_tree
                if (ratio_1 is None or (ratio_2 >= ratio_1)) and next_tree_index == finish_tree_index:
                    ans.add(tuple(current_tree))
                    return next_tree_index, next_tree

        answer = set()
        stop_for_tree(trees, None, 0, None, False, answer)
        trees_reversed = list(reversed(trees))
        stop_for_tree(trees_reversed, None, 0, None, True, answer)
        return answer

    def get_next_tree(self, trees, current_tree_index, current_tree, trees_reversed):
        for index, tree in enumerate(trees[current_tree_index + 1:], start=current_tree_index + 1):
            if (tree[0] > current_tree[0] and not trees_reversed) or (
                    tree[0] < current_tree[0] and trees_reversed):
                return index, tree
        return current_tree_index + 1, trees[current_tree_index + 1]