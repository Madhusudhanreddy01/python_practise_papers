# 13. Let’s assume there is function defined which expects only list as an argument, However there is chance that sometimes function will be called with different type of data, Now Fix this scenario to handle the other types without breaking the code
# • Scenario 1: If the argument provided is a list then, Print inside the function as“valid argument “
# • Scenario 2: if the argument provided is a different data type, then Print a message saying “ invalid argument, You have provided data type (str/int) .

def scenario_(list1):
        if type(list1) == list:
            print("valid argument")
        else:
            print("invalid argument, you have provided data type", type(list1).__name__)


scenario_([1, 2, 3])        # valid argument
scenario_("hello")          # invalid argument, you have provided data type str
scenario_(123)              # invalid argument, you have provided data type str
