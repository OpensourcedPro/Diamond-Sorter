from random import randint as rint


def windows() -> str:
    etc = ['WOW64', 'Win64; x64']
    ver = ['10.0', '6.' + str(rint(0, 3))]
    main = 'Windows NT '

    version = ver[rint(0, 1)]

    if version == '10.0' or bool(rint(0, 1)):
        version += '; ' + etc[rint(0, 1)]

    return main + version


def macos() -> str:
    main = 'Macintosh; Intel Mac OS X 10_'
    sub = str(rint(10, 14))
    sub += '_' + str(rint(1, (6 if sub != '14' else 2)))

    return main + sub


def linux() -> str:
    ver = ['x86_64', 'i686', 'i686 on x86_64']
    main = 'X11; Linux '

    return main + ver[rint(0, 2)]


def random_os() -> str:
    os = [windows, macos, linux]
    return os[rint(0, 2)]()
