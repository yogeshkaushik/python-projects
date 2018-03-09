'''''

1. The try statement works as follows.

-First, the try clause (the statement(s) between the try and except keywords) is executed.
-If no exception occurs, the except clause is skipped and execution of
    the try statement is finished.
-If an exception occurs during execution of the try clause, the rest of the clause is skipped.
    Then if its type matches the exception named after the except keyword, the except clause is
    executed, and then execution continues after the try statement.
-If an exception occurs which does not match the exception named in the except clause,
    it is passed on to outer try statements; if no handler is found, it is an unhandled
    exception and execution stops with a message as shown above.

2. An except clause may name multiple exceptions as a parenthesized tuple, for example:
... except (RuntimeError, TypeError, NameError):
...     pass


3. Example :
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

4. The try … except statement has an optional else clause, which, when present,
    must follow all except clauses. It is useful for code that must be executed if
    the try clause does not raise an exception. For example:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else: //similar to finally of java.
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

5. The raise statement allows the programmer to force a specified exception to occur. For example:
... raise NameError('HiThere')

6. The try statement has another optional clause which is intended to define clean-up actions
    that must be executed under all circumstances. For example:

...
... try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>

A finally clause is always executed before leaving the try statement, whether an exception
    has occurred or not. When an exception has occurred in the try clause and has not been
    handled by an except clause (or it has occurred in an except or else clause), it is
    re-raised after the finally clause has been executed. The finally clause is also executed
    “on the way out” when any other clause of the try statement is left via a break, continue
    or return statement. A more complicated example:
    
'''

'''
1. Instantiation of a class :==> obj = Main()
 
2. Construtor :==>
    def __init__(self):
          self.data = []
          
class Main:
     This is the doc statement of the class, will be returned on __doc__ call.
    a = 5
'''
from skimage import data
import matplotlib.pyplot as plt

def test():
    print("Hello")
    camera = data.coins()
    plt.imshow(camera, cmap="gray")
    plt.show()

if __name__=="__main__":
    test()



