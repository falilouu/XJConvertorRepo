import json
import sys
import svgwrite

from urllib.request import urlopen


def is_json(file):
    try:
        json.load(file)
    except ValueError:
        return False
    return True


def func1(toParse):
    for key, value in toParse.items():
        print(str(key) + '->' + str(value))
        if type(value) == type(dict()):
            func1(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    func1(val)


def main():
    if sys.argv[1] == '-i' and sys.argv[2] == 'json':
        if sys.argv[3] == '-t':
            if sys.argv[4] == '-h':
                url = urlopen(sys.argv[5])
                if is_json(url):
                    print("JSON valide.")
                    print()
                else:
                    print("JSON invalide")
                    return 0
                json_obj = json.load(url)
                func1(json_obj)
            elif sys.argv[4] == '-f':
                name = sys.argv[5]
                if is_json(open(name, 'r')):
                    print("JSON valide.")
                    print()
                else:
                    print("JSON invalide")
                    return 0
                with open(name, 'r') as fp:
                    json_obj = json.load(fp)
                func1(json_obj)
            if sys.argv[6] == '-o':
                nomFichier=sys.argv[7]
        else:
            if sys.argv[3] == '-h':
                url = urlopen(sys.argv[4])
                if is_json(url):
                    print("JSON valide.")
                    print()
                else:
                    print("JSON invalide")
                    return 0
                json_obj = json.load(url)
            if sys.argv[3] == '-f':
                name = sys.argv[4]
                if is_json(open(name, 'r')):
                    print("JSON valide.")
                    print()
                else:
                    print("JSON invalide")
                    return 0
                with open(name, 'r') as fp:
                    json_obj = json.load(fp)
            if sys.argv[5] == '-o':
                nomFichier=sys.argv[6]
    elif sys.argv[1] == '-i' and sys.argv[2] == 'xml':
        if sys.argv[3] == '-t':
            if sys.argv[4] == '-h':
                url = urlopen(sys.argv[5])

            elif sys.argv[4] == '-f':
                name = sys.argv[5]
            if sys.argv[6] == '-o':
                nomFichier=sys.argv[7]

        else:
            if sys.argv[3] == '-h':
                url = urlopen(sys.argv[4])

            if sys.argv[3] == '-f':
                name = sys.argv[4]
            if sys.argv[5] == '-o':
                nomFichier=sys.argv[6]
        print("Nothing ftm")


if __name__ == '__main__': main()


# json_obj = str(json_obj)
# for e in i:
# j, rhs = json_obj.split(":", 1)

# for key, value in json_obj.items():
# print("Entité : {} | Valeur : {}".format(key, value))
