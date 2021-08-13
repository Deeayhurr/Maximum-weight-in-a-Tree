from graph import Graph
def userguide():
    """ This is a function that has enclosed the userguide of this program """

    print(" -----User Guide----" + "\n" +
          "* Problem Description:" + "\n" +
          "The project is about finding a group of shareholders in a joint-stock company" +
          "with the biggest sum of shares in which none of the shareholders spy each other." + "\n"
                                                                                               "In this company each shareholder except one spy on exactly one other shareholder." + "\n"                                                                                                                                                                      "Result = sum of the biggest shareholder group. /n" +
          "Find out what is the maximum total \n" +
          "Input Format: The  first line contains an integer " +
          "— the number of shareholders in the joint-stock company. \n" +
          "The next line contains 3 part. In this order: the weight of shareholder, the name of shareholder, " +
          "the spy of shareholder. \n" +
          "Each of the next lines describes the shareholders structure. \n" +
          "if shareholder does not spy anybody then put space or do not enter anything. " +
          "Everyone except one spy on exactly one other shareholder. " +
          "Each of the lines contains shareholders information. \n" +
          "Constraints. 1<=N<=26; \n" +
          "ShareHolder name must be character. \n" +
          "Spy name must be character or space \n" +
          "Weight must be integer \n" +
          "Output Format: Output the maximum possible total sum of the shareholder group" +
          "(the biggest sum of shares of all shareholders in a joint-stock company)." +
          ""
          "\n Example: \n 40,A,B")


def getshareholderinfo() -> tuple:
    """ This function gets the input from the user, saves the input and returns it as a tuple. """

    while True:
        try:
            num_of_shareholders = int(input("Input number of shareholders [Range: 1-26]: "))
            if num_of_shareholders < 1 or num_of_shareholders > 26:
                raise IndexError("Shareholder's number is not in the expected range [1-26]")
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except IndexError as err:
            print(err.args)

    print("Please use shareholders format: Name(Type: string), Weight(Type: int), Spy(Type: string)")

    Shareholders = []
    Weights = []
    Spies = []

    for shareholder_index in range(num_of_shareholders):
        count = shareholder_index + 1
        while True:
            try:
                shareholder, weight, spy = [x for x in
                                            input(f'Input in this order: the name of shareholder {count}, '
                                                  'the name of shareholder\'s weight and the shareholder he spies: '
                                                  ).split(',')]

                shareholder_type = isinstance(shareholder, str)
                weight_type = isinstance(int(weight), str)
                spy_type = isinstance(spy, str)
                if ((shareholder_type == True and spy_type == True) and ("-" in shareholder or "-" in spy)) or (
                        shareholder_type == False or spy_type == False) or (weight_type == True):
                    raise ValueError("Please shareholder and the shareholder spied has to be Character while Weight "
                                     "should be a number!")
                else:
                    Shareholders.append(shareholder)
                    Spies.append(spy)
                    Weights.append(weight)
                break
            except ValueError as err:
                print(err.args)
                print("Please shareholder and the shareholder spied has to be Character while Weight should be a "
                      "number!")
    shareholder_full_info = zip(Shareholders, Weights, Spies)
    shareholder_full_info = tuple(shareholder_full_info)
    # Another way to get the  shareholder_full_info without having to zip the values is by using the
    # shareholderindex+count as the name of the variable and using a for loop to get the values.
    return shareholder_full_info

# The main program
if __name__ == '__main__':
    userguide()
    shareholder_info = getshareholderinfo()
    graph1 = Graph(shareholder_info)
    print(graph1.get_graph())
    cycle = graph1.is_cyclic()
    print(cycle)
    max_solution = graph1.solve_cyclic_graph()
    print(max_solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
