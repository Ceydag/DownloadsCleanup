import os

images = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'ico']
documents = ['pdf', 'txt','doc', 'docx', 'odt', 'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'odp', 'csv', 'rtf', 'tex', 'html']
compressed = ['zip', 'rar', '7z', 'tar', 'gz', 'z', 'rpm', 'deb']
installers = ['exe', 'msi', 'dmg', 'iso']	
music = ['mp3', 'wav', 'raw', 'm4a', 'aac', 'ogg', 'wma', 'aiff']
code = ['py', 'html', 'css', 'js', 'php', 'cpp', 'c', 'java', 'rb', 'pl', 'sh', 'bat', 'cmd', 'ps1', 'vbs', 'swift', 'kt', 'go', 'ts', 'lua', 'r', 'cs', 'vb', 'scala', 'groovy', 'perl', 'rust', 'dart', 'ts', 'asm', 'sql', 'json', 'xml', 'yml', 'yaml', 'toml', 'ini', 'cfg', 'conf', 'md', 'markdown', 'rst']

path = os.path.expanduser('~/Downloads')
destinations = ['Music', 'Images', 'Documents', 'Compressed', 'Installers', "Code", 'Others']

# Checks if the directories exist, if not, creates them
for destination in destinations:
    if (os.path.exists(os.path.join(path, destination)) == False):
        os.mkdir(os.path.join(path, destination))


# Moves the files to their respective directories
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        extension = file.split('.')[-1]
        if extension in images:
            os.rename(os.path.join(path, file), os.path.join(path, 'Images', file))
        elif extension in documents:
            os.rename(os.path.join(path, file), os.path.join(path, 'Documents', file))
        elif extension in compressed:
            os.rename(os.path.join(path, file), os.path.join(path, 'Compressed', file))
        elif extension in installers:
            os.rename(os.path.join(path, file), os.path.join(path, 'Installers', file))
        elif extension in music:
            os.rename(os.path.join(path, file), os.path.join(path, 'Music', file))
        elif extension in code:
            os.rename(os.path.join(path, file), os.path.join(path, 'Code', file))
        else:
            os.rename(os.path.join(path, file), os.path.join(path, 'Others', file))




