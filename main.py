from subprocess import run
import argparse
import os
from commands import command_nodeJs
from examples import example_node_js

path_folder = os.path.expanduser(os.path.abspath('C:\\Users\\alexa\\workspace'))
count_create_folder = 0

parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', required=True)
parser.add_argument('--lang', '-l', required=True)
args = list(vars(parser.parse_args()).values())

def html(name):
    print('Html')

def react(name):
    print('React')

def vite(name):
   print('Vite')

def node(name, path):
    create_folder(os.path.join(name, 'src'))
    write_files(os.path.join(path, 'src', 'index.js'), example_node_js)
    create_folder(os.path.join(name, 'src', 'libs'))
    create_folder(os.path.join(name, 'src', 'models'))
    create_folder(os.path.join(name, 'src', 'routers'))
    run(command_nodeJs(path), shell=True)
    

langs = {
    'html': html,
    'react': react,
    'vite': vite,
    'node': node,
}

def write_files(path, data):
    with open(path, 'w') as file:
        file.write(data)

def controller(name, lang):
    if not lang in langs.keys():
        raise OSError('The lang is invalid, the valid [html, react, vite, node]')
    langs[lang](name, os.path.join(path_folder, name))
    return 
    

def create_folder(name):
    if not os.path.isdir(path_folder):
        os.mkdir(path_folder)
        count_create_folder = count_create_folder + 1
        if count_create_folder < 5:
            create_folder(name)
        else: return False
    else:
        count_create_folder = 0
        os.mkdir(os.path.join(path_folder, name))
        return True


def main():
    name, lang = args
    folder = create_folder(name)
    if folder:
        controller(name, lang)


if __name__ == '__main__':
    main()