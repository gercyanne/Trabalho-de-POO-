medicos = [
    {"medicoNome": "Larissa", 
     "medicoCPF": "1515", 
     "medicoRG": "1010", 
     "medicoCRM": "2709",
     "medicoTelefone": "889212121",
     "medicoEndereco": "Varzea Alegre", 
     "medicoSexo": "F", 
     "senha": "1511"},

     {"medicoNome": "Ana Maria", 
     "medicoCPF": "202020", 
     "medicoRG": "0000", 
     "medicoCRM": "1212",
     "medicoTelefone": "889303030",
     "medicoEndereco": "Varzea Alegre", 
     "medicoSexo": "F", 
     "senha": "102810"},      
     
     ]   

pacientes = [
    {"pacienteNome": "Hiago", 
     "pacienteEndereco": "Varzea Alegre",
     "pacienteTelefone": "88 994649566", 
     "pacienteCPF": "606060", 
     "pacienteRG": "717171",
     "pacienteSexo": "M", 
     "convenio": "B" }
     ]

convenios = [ {"convenioNome": "B", 
               "convenioTelefone": "88910281028",
                "convenioEndereco": "Juazeiro do Norte ",
                "convenioCNPJ": "1234567", 
                "convenioPlanos": "1" }]


compromissos = [{
     "data": "14/06/2024",  
     "horaInicial": "13:00", 
     "horaFinal": "14:50", 
     "descricao": "consulta no psicologo"}]

consultas = [{
    "medicoNome": "Larissa",
    "pacienteNome": "Hiago", 
    "data": "20/06/2024",
    "horaInicial": "9:50",
    "horaFinal": "11:00",
    "descricao": "consulta no dentista",
    }]

relatorios = []
a = True
while a:
 lang = input("1 - Cadastrar Médicos\n"
              "2 - Cadastrar Pacientes\n"
              "3 - Cadastrar Convênios\n"
              "4 - Buscar Médicos\n"
              "5 - Buscar Pacientes\n"
              "6 - Buscar Convênios\n"
              "7 - Alterar Medicos\n"
              "8 - Alterar Pacientes\n"
              "9 - Marcar Compromisso\n"
              "10 - Marcar consulta\n"
              "11 - Emitir Relatorio\n"
              "12 - Encerrar Programa\n"
              "O que você deseja fazer? ")
 
 def cadastrarMedicos():
     medicoNome = input("Digite o nome do médico: ")
     medicoCPF = input("Digite o CPF do médico: ")
     medicoCRM = input("Digite o CRM do médico: ")
     medicoRG = input("Digite o RG do médico: ")
     medicoTelefone = input("Digite o telefone do médico: ")
     medicoEndereco = input("Digite o endereço do médico: ")
     medicoSexo = input("Digite o sexo do médico (M/F): ")
     senha = input("Digite a senha do médico: ")
     
 
     medicos.append({
         "medicoNome": medicoNome,
         "medicoCPF": medicoCPF,
         "medicoCRM": medicoCRM,
         "medicoRG" : medicoRG, 
         "medicoTelefone": medicoTelefone,
         "medicoEndereco": medicoEndereco,
         "medicoSexo": medicoSexo,
         "senha": senha
         })
 
     print("Médico cadastrado com sucesso!")
 
      
 def buscarMedicos():
     print("Informe o nome ou CRM do médico que deseja buscar:")
     busm = input("")
     print("Medico encontrado!")
     resultados = [medico for medico in medicos if busm.lower() == medico.get('medicoNome', '').lower() or busm == medico.get('medicoCRM', '')]
     if resultados:
        for resultado in resultados:
            print(f"medicoNome: {resultado['medicoNome']}, medicoTelefone: {resultado['medicoTelefone']}, medicoCRM: {resultado['medicoCRM']}")
     else:
        print("Nenhum médico encontrado.")
 
 
 def alterarMedicos():
     medicoNome = input("Digite o nome do médico: ")
     for medico in medicos:
         if medico["medicoNome"] == medicoNome:
            medico["medicoCPF"] = input("Digite o novo cpf do médico: ")
            medico["medicoCRM"] = input("Digite o novo CRM do médico: ")
            medico["medicoRG"] = input("Digite o novo RG do médico: ")
            medico["medicoTelefone"] = input("Digite o novo telefone do médico: ")
            medico["medicoEndereco"] = input("Digite o novo endereço do médico: ")
            print("Médico alterado com sucesso!")
            return
     print("Médico não encontrado!")
 
 def cadastrarPacientes():
     
     pacienteNome = input("Digite o nome do paciente: ")
     pacienteCPF = input("Digite o CPF do paciente: ")
     pacienteRG = input("Digite o RG do paciente: ")
     pacienteTelefone = input("Digite o telefone do paciente: ")
     pacienteEndereco = input("Digite o endereço do paciente: ")
     pacienteSexo = input("Digite o sexo do paciente (M/F): ")
     convenio = input("Digite o convenio que o paciente está associado: ")
 
     
     pacientes.append({
        "pacienteNome": pacienteNome, 
        "pacienteCPF": pacienteCPF,
        "pacienteRG": pacienteRG,
        "pacienteTelefone": pacienteTelefone,
        "pacienteEndereco": pacienteEndereco,
        "pacienteSexo": pacienteSexo,
        "convenio": convenio, })

     print("Paciente cadastrado com sucesso!")

 
 def buscarPacientes():
     pacienteNome = input("Digite o nome do paciente: ")
     for paciente in pacientes:
         if paciente["pacienteNome"] == pacienteNome:
             print("Paciente encontrado!")
             print("pacienteCPF:", paciente["pacienteCPF"])
             print("pacienteTelefone:", paciente["pacienteTelefone"])
             return paciente
     print("Paciente não encontrado!")
 
 
 
 def alterarPacientes():
     pacienteNome = input("Digite o nome do paciente: ")
     for paciente in pacientes:
         if  paciente["pacienteNome"] == pacienteNome:
             paciente["pacienteCPF"] = input("Digite o novo cpf do paciente: ")
             paciente["pacienteRG"] = input("Digite o novo RG do paciente: ")
             paciente["pacienteTelefone"] = input("Digite o novo telefone do paciente: ")
             paciente["pacienteEndereco"] = input("Digite o novo endereço do paciente: ")
             paciente["convenio"] = input("Digite o novo convenio que o paciente está relacionado: ")
             print("Paciente alterado com sucesso!")
             return
     print("Paciente não encontrado!")
 
 def cadastrarConvenios():
     convenioNome = input("Digite o nome do convênio: ")
     convenioTelefone = input("Digite o telefone para contato: ")
     convenioCNPJ = input("Digite seu CNPJ: ")
     convenioPlanos = input("Digite os planos fornecidos pelo convenio: ")
 
     
     convenios.append({
        "convenioNome": convenioNome,
        "convenioTelefone": convenioTelefone,
        "convenioCNPJ": convenioCNPJ,
        "convenioPlanos": convenioPlanos,})

     print("Convênio cadastrado com sucesso!")
 
 def buscarConvenios():
     convenioCNPJ = input("Digite o CNPJ: ")
     for convenio in convenios:
         if convenio["convenioCNPJ"] == convenioCNPJ:
             print("Convenio encontrado!")
             print("convenioNome:", convenio["convenioNome"])
             print("convenioTelefone:", convenio["convenioTelefone"])
             print("convenioCNPJ:", convenio["convenioCNPJ"])
             return
     print("Convenio não encontrado!")
 
 def marcarConsulta():
        medicoNome = input("Insira o nome do médico: ")
        medicoencontrado = next((medico for medico in medicos if medico['medicoNome'] == medicoNome), None)
        if medicoencontrado:
            pacienteNome = input("Informe o nome do paciente: ")
            pacienteencontrado = next((paciente for paciente in pacientes if paciente['pacienteNome'] == pacienteNome), None)
            if pacienteencontrado:
                data = input("Insira a data da consulta: ")
                horaInicial = input("Insira a hora inicial da consulta: ")
                horaFinal = input("Insira a hora final da consulta: ")
                descricao = input("Descreva a consulta: ")
                
            
                print("Consulta marcada com sucesso!")
                consultas.append({
                    "data": data,
                    "horaInicial": horaInicial,
                    "horaFinal": horaFinal,
                    "medicoNome": medicoNome,
                    "pacienteNome": pacienteNome,
                    "descricao": descricao
                })

                
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")
     
        
                

 def marcarCompromisso():
        medicoNome = input("Insira o nome do médico: ")
        medicoencontrado = next((medico for medico in medicos if medico['medicoNome'] == medicoNome), None)
        if medicoencontrado:
           data= input("Informe a data do compromisso: ")
           horaInicial = input("Informe a hora inicial do compromisso: ")
           horaFinal = input("Informe a hora final do compromisso: ")
           descricao = input("Informe a descrição do compromisso: ")
           print("Compromisso marcado com sucesso!")
     
           compromissos.append({
                  "data": data,
                  "horaInicial": horaInicial,
                  "horaFinal": horaFinal,
                  "descricao": descricao,
              })
                
        else:
                print("Medico não encontrado.")
        
       
 def emitirRelatorio (): 
   
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome do médico: {medico['medicoNome']}, CPF do médico: {medico['medicoCPF']}, CRM do médico: {medico['medicoCRM']}, Telefone do médico: {medico['medicoTelefone']}")
            
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"Nome do paciente: {paciente['pacienteNome']}, CPF do paciente: {paciente['pacienteCPF']}, Telefone do paciente: {paciente['pacienteTelefone']}")
            
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome do convênio: {convenio['convenioNome']}, CNPJ do convênio: {convenio['convenioCNPJ']}, Telefone do convênio: {convenio['convenioTelefone']}")
            
    elif escolha == "4":
        print("Consultas:")
        for consulta in consultas:
            print(f"Nome do paciente: {consulta['pacienteNome']}, Nome do médico: {consulta['medicoNome']}, Data da consulta: {consulta['data']},  Hora inicial da consulta: {consulta['horaInicial']},  Hora final da consulta: {consulta['horaFinal']},  Descrição da consulta: {consulta['descricao']}")
            

 match lang:
     case "1":
         cadastrarMedicos()
       
 
     case "2":
         cadastrarPacientes()
        
 
     case "3":
         cadastrarConvenios()
        
     
     case "4":
         buscarMedicos()
         
 
     case "5":
         buscarPacientes()
        
         
     case "6":
         buscarConvenios()
        
 
     case "7":
         alterarMedicos()
         
        
     case "8":
         alterarPacientes()
         
     case "9":
         marcarCompromisso()
         
 
     case "10":
         marcarConsulta()
        
     
 
     case "11":
         emitirRelatorio()
        
     case "12":
         a = False
 
     case _:
         print("Escolha uma opção válida")
        
 