import paramiko
import sys  

#Verifica se o usuário passou mais de 3 parâmetros (usuário, senha e host)
def input_verify(i):

    if(i<=3):
        print("Usage: python this_archive.py user password host")
        return 0
    return 1

#Executa a função de ssh se o usuário tiver passado mais de 3 parâmetros
def exec_ssh(args):
    user = args[1]
    passw = args[2]
    host = args[3]
    try:
        client_ssh = paramiko.SSHClient() #Cria uma variável contendo atributos de um cliente SSH
        client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy) #Adiciona política de chave do PARAMIKO
        client_ssh.connect(host, username=user, password=passw) #Tenta conexão SSH com os parâmetros passados (Usuário, Senha e Host)
        while True:
            command = input("Command: ") #Recebe comando do usuário para ser executado na máquina conectada via SSH
            stdin, stdout, stderr = client_ssh.exec_command(command) #Recebe os dados da conexão como dados de entrada/saída/erros
            print (stdout.readlines()) #Mostra o resultado da execução do comando
            print (stderr.readlines()) #Mostra os erros da execução do comando
    except Exception as e:
        print(e)

#Recebe a entrada do usuário e coloca na lista args
def main():
    args = []
    i = 0
    for line in sys.argv:
        args.append(line) #Adiciona os argumentos do usuário na lista args
        i = i+1
    if(input_verify(i)): #Verificação do input
        exec_ssh(args)   #Execução da função ssh em python usando lib paramiko

main()