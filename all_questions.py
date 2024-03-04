# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since agglomerative hierarchical clustering combines data points according to similarity rather than cluster centroids, it is more robust against outliers than k-means."
    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Different clusterings can be produced by k-means and agglomerative hierarchical clustering, depending on the initial conditions and algorithm parameters. A few variables that influence the clustering result are the number of clusters, initial centroids, distance measure, and linking technique."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "For certain data settings, K-means clustering may not be the most efficient clustering technique, while using less memory and being faster than agglomerative hierarchical clustering. Other clustering algorithms might work better in certain circumstances."

    # type: bool (True/False) #check whether there is true or false is there
    answers["(d)"] = -1

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Depending on the new centroid, splitting a cluster can either raise or lower the clustering's SSE. Since reducing the SSE is the aim, splitting a cluster should be decided depending on how much the clustering quality might improve."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Due to the data points being closer to the cluster centers, lower SSE in k-means clustering results in higher cluster cohesiveness."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "Since there is a greater distance between the clusters in k-means clustering, higher SSB results in better cluster separation."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In k-means clustering, cohesion and separation are independent. It is not necessary to increase SSB (separation) in order to decrease SSE (cohesion), and vice versa."

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "When making adjustments to the clusters or adding or removing data points, SSE and BSS in k-means clustering might also vary."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "In k-means clustering, there are two distinct metrics: separation and cohesiveness. Separation quantifies how different a cluster is from its neighbors, whereas cohesion gauges how closely associated the data points within a cluster are. Depending on the dataset and algorithm, they may alter separately."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "When the k-means algorithm completes, each shaded circle will have one cluster centroid at its center."
    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "When the k-means algorithm completes, some of the two final clusters will have points from both shaded regions."
    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "When the k-means algorithm completes, the final clustering for k-means contains an empty cluster."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = 4/R^2

    # type: a string that evaluates to a float
    answers["(b) SSE"] = squrt(a^2+b^2)

    # type: a string that evaluates to a float
    answers["(c) SSE"] = 5*R^2

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 0

    # type: int
    answers["(a) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: int
    answers["(b) Circle (a)"] = 0

    # type: int
    answers["(b) Circle (b)"] = 0

    # type: int
    answers["(b) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set(Group A , Group B)

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The distance between the top left point in Group A and the top right point in Group B is the shortest path that separates them. "

    # type: set
    answers["(b)"] = set(Group A , Group C)

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The distance between the bottom left point in Group C and the bottom right point in Group A is the longest between them."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set(A,B,C,D,E,F,G,H,I,J)

    # type: set
    answers["(a) boundary"] = set(L,M)

    # type: set
    answers["(a) noise"] = set()

    # type: set
    answers["(b) cluster 1"] = set()

    # type: set
    answers["(b) cluster 2"] = set()

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set()

    # type: set
    answers["(c)-a boundary"] = set()

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set()

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = ""

    # type: string
    answers["(b) Row 2"] = ""

    # type: string
    answers["(b) Row 3"] = ""

    # type: string
    answers["(b) Row 4"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierachial','fuzzy','partial']

    # type: list
    answers["(b)"] = ['hierarchical','overlapping','partial']

    # type: list
    answers["(c)"] = ['partitional', 'non-exclusive', 'partial']

    # type: list
    answers["(d)"] = ['','overlapping','fuzzy']

    # type: list
    answers["(e)"] = ['partitional', 'exclusive','complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = ""

    # type: string
    answers["(a) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b) Figure (a)"] = ""

    # type: string
    answers["(b) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: string
    answers["(c)"] = ""

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
