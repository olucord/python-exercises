import json
import os

pessoas = [{
    "nome":'Lucas',
    "idade":25,
    "Curso":'Engenharia'
},
{
    "nome":'Ayanne',
    "idade":30,
    "Curso":'Odontologia'
}
]

# Para pegar o endereço desta pasta, sem o nome do arquivo incluso (__file__ inclui o nome)
directory_of_this_script = os.path.dirname(__file__) 
# Juntando de modo correto o caminho dos arquivos
new_file_on_this_folder = os.path.join(directory_of_this_script, 'json_file_of_python_file.json')

# Criando um novo arquivo, abrindo, escrevendo e fechando ele
with open(new_file_on_this_folder, 'w', encoding='utf8') as file:
    json.dump(pessoas, file, indent=2)
    
# Se quiser exibir no formato json diretamente 
# no terminal do python, sem criar um arquivo json
print(json.dumps(pessoas, indent=2), end='\n\n*********\n\n')

# Se quiser importa de um arquivo json para o Python
other_file_on_this_folder = os.path.join(directory_of_this_script, 'json_file_for_export_to_python.json')

with open(other_file_on_this_folder, 'r') as file:
    new_dict_imported = json.load(file)

print(new_dict_imported, end='\n\n*********\n\n')

# Se quisermos exibir um string de um arquivo json 
# no terminal do python diretamente
string_json = '''
[{"Linguagem": "Python", "idade": 33, "Uso": "Aplicações Científicas"}, {"Linguagem": "JavaScript", "idade": 28, "Uso": "Web, usuários e servidores"}]
'''
string_json_python_format = json.loads(string_json)

print(string_json_python_format)



