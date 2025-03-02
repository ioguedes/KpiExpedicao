import os
import sys
import webbrowser
from django.core.management import execute_from_command_line

def main():
    try:
        # Define o caminho absoluto do projeto
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        # Adiciona o caminho do projeto ao sys.path
        sys.path.append(BASE_DIR)

        # Configura o módulo de settings do Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KpiExpedicao.settings') 

        # Simula os argumentos de linha de comando para o Django
        sys.argv = ['manage.py', 'runserver', '--noreload']

        # Inicia o servidor Django
        print("Iniciando servidor Django...")
        execute_from_command_line(sys.argv)

        # Abre o navegador
        print("Abrindo navegador...")
        webbrowser.open('http://localhost:8000/expedicao/')
    except Exception as e:
        print(f"Erro: {e}")
        input("Pressione Enter para sair...")

if __name__ == '__main__':
    main()