Identify subtrees():
 
    subtrees[]

    findSubtree:
        if node is null return null
       
        else
        findSubtree on children node

        subtree= root+ children

        Append subtree to subtrees
    
    findSubtree()

    return subtrees


for trees in subtrees
    calculate fitness
    if trees.fitness>=hostTree.fitness
        stop mutation from applying on any node in that subtree
    else
        apply mutation

#PUT INTO REPORT