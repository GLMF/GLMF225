from typing import Callable
import timeit

def readFile(name : str, processFct : Callable[[str], None], characters : int = 8) -> int:
    try:
        with open(name, 'r') as fic:
            chain = fic.read(characters)
            while chain:
                processFct(chain)
                chain = fic.read(characters)
            return 0
    except Exception as e:
        print(f'Erreur : {e}')
        return 1


def display(chain : str) -> None:
    print(f'(display) => {chain}')


def display_timeit(chain : str) -> None:
    if len(chain) == 5:
        var = True


if __name__ == '__main__':
    print(timeit.timeit(lambda fic='test.txt', fct=display_timeit : readFile(fic, fct), number=100000))
