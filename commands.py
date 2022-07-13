def command_nodeJs(path):
    commands = [
        'cd', 
        path,  
        '&&',
        'npm',
        'init',
        '-y',
        '&&',
        'cls',
        '&&',
        'npm',
        'init',
        '-ws',
        path,
        '-y',
        '&&',
        'cls',
        '&&',
        'npm',
        'i',
        'express',
        'cors',
        'mongoose',
        'jsonwebtoken',
        'bcryptjs',
        'dotenv',
        '&&',
        'cls',
        '&&',
        'npm',
        'i',
        'morgan',
        'nodemon',
        '-D',
        '&&',
        'cls',
        '&&',
        'npm',
        'list'
    ]
    return commands

def command_vite(path):
    comands = [
        'cd',
        path,
        '.',
        '&&',
        'npm',
        'create',
        'vite@latest',
        '.',
        '--',
        '--template',
        'react',
        '-y',
        '&&',
        'cls',
        '&&',
        'npm',
        'i',
        '&&',
        'cls',
        '&&',
        'npm',
        'list'
    ]
    return comands