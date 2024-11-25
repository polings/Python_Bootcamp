from itertools import zip_longest


def fix_wiring(cables, sockets, plugs):
    """
    Creates wiring instructions for connecting cables to sockets, with or without plugs.
    """
    return (
        f"plug {cable} into {socket} using {plug}" if plug else f"weld {cable} to {socket} without plug"
        for cable, socket, plug in
        zip_longest(filter(lambda x: isinstance(x, str), cables), filter(lambda x: isinstance(x, str), sockets),
                    filter(lambda x: isinstance(x, str), plugs))
        if cable and socket
    )


def main():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    for wire in fix_wiring(cables, sockets, plugs):
        print(wire)


if __name__ == "__main__":
    main()
