from IPython.display import clear_output


def in_ipynb():
    """Tells if a scripts is running under IPython or not"""
    try:
        cfg = get_ipython().config
        if cfg['IPKernelApp']['parent_appname'] == 'ipython-notebook':
            return True
        else:
            return False
    except NameError:
        return False


def cmdProgressBar(progress, size=30):
    a = round(progress * size)

    # Under jupyter, the clear of the console is different.
    if in_ipynb():
        clear_output(wait=True)

    print(
        "[{0}>{1}] {2:.0f}%".format(a * '=', (size - a) * ' ', progress * 100),
        end='\r', flush=True)
