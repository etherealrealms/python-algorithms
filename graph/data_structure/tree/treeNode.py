class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return (
            f'Tree Node [Val: {self.value}]:\n\tLeft Child: ' +
               ('None' if self.left_child is None else str(self.left_child.value))+
                                                      '\n\tRight Child: ' +
                                                      ('None' if self.right_child is None else str(self.right_child.value))
            + '\n'
        )

