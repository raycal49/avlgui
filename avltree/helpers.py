def step1(avl_tree, num, root, ordinal):
    print("-" * 20)
    print (f"Insertion number {ordinal}\n")
    print("Inserting", num, end="\n\n")
    root = avl_tree.insert_node(root, num)

    if root != None:
        root.display()

    print("\n")
    return root

def step2(avl_tree, num, root):
    print("Deleting", num)
    root = avl_tree.delete_node(root, num)
    if root != None:
        root.display()
    print("\n")
    return root