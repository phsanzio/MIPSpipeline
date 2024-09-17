# Dicionário para classificar as instruções como 'read' ou 'write'(função "principal")
data_func = {
    'lb': ['read', 'write'], 'lh': ['read', 'write'], 'lwl': ['read', 'write'], 'lw': ['read', 'write'], 
    'lbu': ['read', 'write'], 'lhu': ['read', 'write'], 'lwr': ['read', 'write'],
    
    'sb': ['read', 'write'], 'sh': ['read', 'write'], 'swl': ['read', 'write'], 'sw': ['read', 'write'], 
    'swr': ['read', 'write'],

    'add': ['read', 'write'], 'addu': ['read', 'write'], 'sub': ['read', 'write'], 'subu': ['read', 'write'],
    'and': ['read', 'write'], 'or': ['read', 'write'], 'xor': ['read', 'write'], 'nor': ['read', 'write'],
    'slt': ['read', 'write'], 'sltu': ['read', 'write'],

    'addi': ['read', 'write'], 'addiu': ['read', 'write'], 'slti': ['read', 'write'], 'sltiu': ['read', 'write'],
    'andi': ['read', 'write'], 'ori': ['read', 'write'], 'xori': ['read', 'write'], 'lui': 'write',

    'sll': 'write', 'srl': 'write', 'sra': 'write', 'sllv': ['read', 'write'], 'srlv': ['read', 'write'], 
    'srav': ['read', 'write'],

    'mfhi': 'write', 'mthi': 'read', 'mflo': 'write', 'mtlo': 'read', 'mult': ['read', 'write'], 
    'multu': ['read', 'write'], 'div': ['read', 'write'], 'divu': ['read', 'write'],

    'jr': 'read', 'jalr': ['read', 'write'],

    'bltz': 'read', 'bgez': 'read', 'bltzal': ['read', 'write'], 'bgezal': ['read', 'write'], 
    'beq': 'read', 'bne': 'read', 'blez': 'read', 'bgtz': 'read',

    'j': 'read', 'jal': 'write'
}

#Indica a posição do(s) registrador(es) que é(são) lido(s) em cada instrução
where_is_read = {
    'lb': [1, 2], 'lh': [1, 2], 'lwl': [1, 2], 'lw': [2], 'lbu': [1, 2], 'lhu': [1, 2], 'lwr': [1, 2],
    'sb': [2], 'sh': [2], 'swl': [2], 'sw': [1, 2], 'swr': [2],

    'add': [2, 3], 'addu': [2, 3], 'sub': [2, 3], 'subu': [2, 3],
    'and': [2, 3], 'or': [2, 3], 'xor': [2, 3], 'nor': [2, 3],
    'slt': [2, 3], 'sltu': [2, 3],

    'addi': [2], 'addiu': [2], 'slti': [2], 'sltiu': [2],
    'andi': [2], 'ori': [2], 'xori': [2], 'lui': [],

    'sll': [2], 'srl': [2], 'sra': [2], 'sllv': [2], 'srlv': [2], 'srav': [2],

    'mfhi': [], 'mthi': [1], 'mflo': [], 'mtlo': [1], 'mult': [1, 2], 'multu': [1, 2],
    'div': [1, 2], 'divu': [1, 2],

    'jr': [1], 'jalr': [1],

    'bltz': [1], 'bgez': [1], 'bltzal': [1], 'bgezal': [1], 'beq': [1, 2], 'bne': [1, 2],
    'blez': [1], 'bgtz': [1],

    'j': [], 'jal': []
}

#Indica a posição do(s) registrador(es) que é(são) escrito(s) em cada instrução
where_is_write = {
    'lb': [1], 'lh': [1], 'lwl': [1], 'lw': [1], 'lbu': [1], 'lhu': [1], 'lwr': [1],
    'sb': [], 'sh': [], 'swl': [], 'sw': [], 'swr': [],

    'add': [1], 'addu': [1], 'sub': [1], 'subu': [1],
    'and': [1], 'or': [1], 'xor': [1], 'nor': [1],
    'slt': [1], 'sltu': [1],

    'addi': [1], 'addiu': [1], 'slti': [1], 'sltiu': [1],
    'andi': [1], 'ori': [1], 'xori': [1], 'lui': [1], 

    'sll': [1], 'srl': [1], 'sra': [1], 'sllv': [1], 'srlv': [1], 'srav': [1],

    'mfhi': [1], 'mthi': [], 'mflo': [1], 'mtlo': [], 'mult': [], 'multu': [],
    'div': [], 'divu': [],

    'jr': [], 'jalr': [1],

    'bltz': [], 'bgez': [], 'bltzal': [], 'bgezal': [], 'beq': [], 'bne': [],
    'blez': [], 'bgtz': [],

    'j': [], 'jal': [31]
}

#Estágio onde cada instrução tem seu "resultado"
stage_result = {
    'lb': 'MEM',  #termina em estágio de memória
    'lh': 'MEM',
    'lwl': 'MEM',
    'lw': 'MEM',
    'lbu': 'MEM',
    'lhu': 'MEM',
    'lwr': 'MEM',
    
    'sb': 'EX', #termina em estágio de execução
    'sh': 'EX',
    'swl': 'EX',
    'sw': 'EX',
    'swr': 'EX',

    'add': 'EX',
    'addu': 'EX',
    'sub': 'EX',
    'subu': 'EX',
    'and': 'EX',
    'or': 'EX',
    'xor': 'EX',
    'nor': 'EX',
    'slt': 'EX',
    'sltu': 'EX',

    'addi': 'EX',
    'addiu': 'EX',
    'slti': 'EX',
    'sltiu': 'EX',
    'andi': 'EX',
    'ori': 'EX',
    'xori': 'EX',
    'lui': 'EX',

    'sll': 'EX',
    'srl': 'EX',
    'sra': 'EX',
    'sllv': 'EX',
    'srlv': 'EX',
    'srav': 'EX',

    'mfhi': 'EX',
    'mthi': 'EX',
    'mflo': 'EX',
    'mtlo': 'EX',
    'mult': 'EX',
    'multu': 'EX',
    'div': 'EX',
    'divu': 'EX',

    'jr': 'EX',
    'jalr': 'EX',

    'bltz': 'EX',
    'bgez': 'EX',
    'bltzal': 'EX',
    'bgezal': 'EX',
    'beq': 'EX',
    'bne': 'EX',
    'blez': 'EX',
    'bgtz': 'EX',

    'j': 'EX',
    'jal': 'EX'
}


# Verifica se a instrução é válida para verificação de conflito
def is_instruction_valid(instruction):
    return instruction[0] in data_func

#Retirar NOPs do array
def remove_NOPs(array_list):
    i = 0
    while i < len(array_list):
        if array_list[i] == ['NOP']:
            array_list.pop(i)
            i -= 1
        i += 1

#Priorizar funções Jump e Branch
def priorizeJandB(array_list):
    i = 0
    jump_instructions = ['j', 'jalr', 'jr', 'jal']
    branch_instructions = ['bltz', 'bgez', 'bltzal', 'bgezal', 'beq', 'bne', 'blez', 'bgtz']
    while i < len(array_list):
        array_line1 = array_list[i]
        if array_line1[0] in branch_instructions:
            array_list.pop(array_list.index(array_line1))
            array_list.insert(0, array_line1)
        i += 1
    i = 0
    while i < len(array_list):
        array_line1 = array_list[i]
        if array_line1[0] in jump_instructions:
            array_list.pop(array_list.index(array_line1))
            array_list.insert(0, array_line1)
        i += 1

#Metódo de bubble
def bubble(array_list):
    i = 0
    remove_NOPs(array_list)
    #Mais que duas instruções
    if len(array_list) > 2:
        while i < len(array_list) - 2:
            # Avalia de 3 em 3 linhas
            array_line1 = array_list[i]
            array_line2 = array_list[i + 1]
            array_line3 = array_list[i + 2]

            if is_instruction_valid(array_line1) and is_instruction_valid(array_line2):
                # Verifica se há conflito entre a 1ª e 2ª instrução
                if 'write' in data_func[array_line1[0]] and 'read' in data_func[array_line2[0]]:
                    if len(where_is_read[array_line2[0]]) == 2 and len(where_is_write[array_line1[0]]) > 0:
                        wh_write = array_line1[where_is_write[array_line1[0]][0]]
                        wh_read1 = array_line2[where_is_read[array_line2[0]][0]]
                        wh_read2 = array_line2[where_is_read[array_line2[0]][1]]
                        if wh_write == wh_read1 or wh_write == wh_read2:
                            # Conflito detectado, insere 2 NOPs após array_line1
                            array_list.insert(i + 1, ['NOP'])
                            array_list.insert(i + 2, ['NOP'])
                            i += 2  
                            # Avança o índice para não criar conflito com os NOPs recém-inseridos
                    elif len(where_is_read[array_line2[0]]) == 1 and len(where_is_write[array_line1[0]]) > 0:
                        wh_write = array_line1[where_is_write[array_line1[0]][0]]
                        wh_read1 = array_line2[where_is_read[array_line2[0]][0]]
                        if wh_write == wh_read1:
                            # Conflito detectado, insere 2 NOPs após array_line1
                            array_list.insert(i + 1, ['NOP'])
                            array_list.insert(i + 2, ['NOP'])
                            i += 2  
                            # Avança o índice para não criar conflito com os NOPs recém-inseridos
                
            # Verifica se há conflito entre a 1ª e 3ª instrução
            if is_instruction_valid(array_line1) and is_instruction_valid(array_line3):
                if 'write' in data_func[array_line1[0]] and 'read' in data_func[array_line3[0]]:
                    if len(where_is_read[array_line3[0]]) == 2 and len(where_is_write[array_line1[0]]) > 0:
                        wh_write = array_line1[where_is_write[array_line1[0]][0]]
                        wh_read1 = array_line3[where_is_read[array_line3[0]][0]]
                        wh_read2 = array_line3[where_is_read[array_line3[0]][1]]
                        if wh_write == wh_read1 or wh_write == wh_read2:
                            if array_list[i - 1] != ['NOP'] and array_list[i] != ['NOP']:
                            # Conflito detectado, insere 2 NOPs após array_line1
                                array_list.insert(i + 1, ['NOP'])
                                array_list.insert(i + 2, ['NOP'])
                                i += 2  
                                # Avança o índice para não criar conflito com os NOPs recém-inseridos
                    elif len(where_is_read[array_line3[0]]) == 1 and len(where_is_write[array_line1[0]]) > 0:
                        wh_write = array_line1[where_is_write[array_line1[0]][0]]
                        wh_read1 = array_line3[where_is_read[array_line3[0]][0]]
                        if wh_write == wh_read1:
                            if array_list[i - 1] != ['NOP'] and array_list[i] != ['NOP']:
                                # Conflito detectado, insere 2 NOPs após array_line1
                                array_list.insert(i + 1, ['NOP'])
                                array_list.insert(i + 2, ['NOP'])
                                i += 2  
                                # Avança o índice para não criar conflito com os NOPs recém-inseridos

            # Verifica se a instrução é válida para verificação de conflito
            if is_instruction_valid(array_line2) and is_instruction_valid(array_line3):
                # Verifica se há conflito entre a 2ª e 3ª instrução
                if 'write' in data_func[array_line2[0]] and 'read' in data_func[array_line3[0]]:
                        if len(where_is_read[array_line3[0]]) == 2 and len(where_is_write[array_line2[0]]) > 0:
                            wh_write = array_line2[where_is_write[array_line2[0]][0]]
                            wh_read1 = array_line3[where_is_read[array_line3[0]][0]]
                            wh_read2 = array_line3[where_is_read[array_line3[0]][1]]
                            if wh_write == wh_read1 or wh_write == wh_read2:
                                # Conflito detectado, insere 2 NOPs após array_line2
                                array_list.insert(i + 2, ['NOP'])
                                array_list.insert(i + 3, ['NOP'])
                                i += 2  
                                # Avança o índice para não criar conflito com os NOPs recém-inseridos
                        elif len(where_is_read[array_line3[0]]) == 1 and len(where_is_write[array_line2[0]]) > 0:
                            wh_write = array_line2[where_is_write[array_line2[0]][0]]
                            wh_read1 = array_line3[where_is_read[array_line3[0]][0]]
                            if wh_write == wh_read1:
                                # Conflito detectado, insere 2 NOPs após array_line2
                                array_list.insert(i + 2, ['NOP'])
                                array_list.insert(i + 3, ['NOP'])
                                i += 2  
                                # Avança o índice para não criar conflito com os NOPs recém-inserido

            i += 1  # Avança para a próxima instrução
    
    #2 instruções somente
    elif len(array_list) == 2:
        array_line1 = array_list[i]
        array_line2 = array_list[i + 1]

        if is_instruction_valid(array_line1) and is_instruction_valid(array_line2):
            # Verifica se há conflito entre a 1ª e 2ª instrução
            if 'write' in data_func[array_line1[0]] and 'read' in data_func[array_line2[0]]:
                if len(where_is_read[array_line2[0]]) == 2 and len(where_is_write[array_line1[0]]) > 0:
                    wh_write = array_line1[where_is_write[array_line1[0]][0]]
                    wh_read1 = array_line2[where_is_read[array_line2[0]][0]]
                    wh_read2 = array_line2[where_is_read[array_line2[0]][1]]
                    if wh_write == wh_read1 or wh_write == wh_read2:
                        # Conflito detectado, insere 2 NOPs após array_line1
                        array_list.insert(i + 1, ['NOP'])
                        array_list.insert(i + 2, ['NOP'])
                        i += 2  
                        # Avança o índice para não criar conflito com os NOPs recém-inseridos
                elif len(where_is_read[array_line2[0]]) == 1 and len(where_is_write[array_line1[0]]) > 0:
                    wh_write = array_line1[where_is_write[array_line1[0]][0]]
                    wh_read1 = array_line2[where_is_read[array_line2[0]][0]]
                    if wh_write == wh_read1:
                        # Conflito detectado, insere 2 NOPs após array_line1
                        array_list.insert(i + 1, ['NOP'])
                        array_list.insert(i + 2, ['NOP'])
                        i += 2  
                        # Avança o índice para não criar conflito com os NOPs recém-inseridos
    

def advance_with_bubble(array_list):
    i = 0
    remove_NOPs(array_list)
    while i < len(array_list) - 1:
        array_line1 = array_list[i]
        array_line2 = array_list[i + 1]
        if is_instruction_valid(array_line1) and is_instruction_valid(array_line2):
            # Verifica se há conflito entre a 1ª e 2ª instrução
            if 'write' in data_func[array_line1[0]] and 'read' in data_func[array_line2[0]]:
                if len(where_is_read[array_line2[0]]) == 2 and len(where_is_write[array_line1[0]]) > 0:
                    wh_write = array_line1[where_is_write[array_line1[0]][0]]
                    wh_read1 = array_line2[where_is_read[array_line2[0]][0]]
                    wh_read2 = array_line2[where_is_read[array_line2[0]][1]]
                    if wh_write == wh_read1 or wh_write == wh_read2:
                        if stage_result[array_line1[0]] == 'MEM':
                            # Conflito detectado, insere 1 NOP após array_line1
                            array_list.insert(i + 1, ['NOP'])
                            i += 1  
                            # Avança o índice para não criar conflito com os NOPs recém-inseridos
                elif len(where_is_read[array_line2[0]]) == 1 and len(where_is_write[array_line1[0]]) > 0:
                    wh_write = array_line1[where_is_write[array_line1[0]][0]]
                    wh_read1 = array_line2[where_is_read[array_line2[0]][0]]
                    if wh_write == wh_read1:
                        if stage_result[array_line1[0]] == 'MEM':
                        # Conflito detectado, insere 1 NOP após array_line1
                            array_list.insert(i + 1, ['NOP'])
                            i += 1  
                            # Avança o índice para não criar conflito com os NOPs recém-inseridos
        i += 1

def reordering_with_bubble(array_list):
    reordering(array_list)
    bubble(array_list)

def reordering(array_list):
    i = 0
    remove_NOPs(array_list)  # Remove NOPs desnecessários
    
    while i < len(array_list) - 1:
        array_line1 = array_list[i]
        array_line2 = array_list[i + 1]
        
        if is_instruction_valid(array_line1) and is_instruction_valid(array_line2):
            # Verifica se há dependência de dados entre a 1ª e a 2ª instrução
            if 'write' in data_func[array_line1[0]] and 'read' in data_func[array_line2[0]]:
                # Confere quais registradores estão sendo lidos e escritos
                if len(where_is_write[array_line1[0]]) > 0 and len(where_is_read[array_line2[0]]) > 0:
                    wh_write = array_line1[where_is_write[array_line1[0]][0]]
                    wh_read = array_line2[where_is_read[array_line2[0]][0]]
                    
                    # Se o registrador escrito na 1ª instrução é o mesmo que é lido na 2ª, não podemos reordenar
                    if wh_write == wh_read:
                        # Insere NOP para evitar conflito de dependência
                        array_list.insert(i + 1, ['NOP'])
                        i += 1  # Avança o índice para não criar mais conflitos com NOPs inseridos
                    else:
                        # Se não há dependência, podemos trocar as instruções
                        array_list[i], array_list[i + 1] = array_line2, array_line1
                        i += 1  # Move o índice para não trocar novamente as instruções que acabamos de ordenar
            else:
                # Se nenhuma dependência de leitura/escrita for detectada, reordena as instruções
                array_list[i], array_list[i + 1] = array_line2, array_line1
                i += 1
    
        i += 1  # Avança para a próxima instrução
    
    priorizeJandB(array_list)
    remove_NOPs(array_list)


def text_generator(read_file, write_file):
    with open(read_file, 'r') as read_file, open(write_file, 'w') as write_file:
        write_file.write('Nome: ' + username + '\n')
        write_file.write('Convertido de: ' + str(read_file.name).replace(caminho_arquivo, '') + '\n')
        write_file.write('Resultado: ' + '\n' + '\n')
        #Colocar instruções no array_list
        array_list = []
        for line in read_file:
            array_temp = []
            line = line.strip().replace(',', '').replace('(',' ').replace(')',' ')
            if line != '':
                for element in line.split():
                    array_temp.append(element)
                array_list.append(array_temp)
        
        #Seleção dos metódos
        verify_name = str(read_file.name).replace('TESTE-', '').replace('.txt', '').replace(caminho_arquivo, '')
        if verify_name in ['01', '02']:
            bubble(array_list)
        elif verify_name in ['03', '04']:
            advance_with_bubble(array_list)
        elif verify_name in ['05', '06', '07']:
            reordering_with_bubble(array_list)
        elif verify_name in ['08', '09', '10']:
            bubble(array_list)
            reordering(array_list)
            advance_with_bubble(array_list)
        else:
            print('Nome de arquivo incorreto!!')
            
        #Colocar instruções no txt de resultado
        for line in array_list:
            if len(line) == 4 and line[2].isdigit():
                line_printable = (f"{line[0]} {line[1]}, {line[2]}({line[3]})")
            elif len(line) == 4:
                line_printable = (f"{line[0]} {line[1]}, {line[2]}, {line[3]}")
            elif len(line) == 3:
                line_printable = (f"{line[0]} {line[1]}, {line[2]}")
            else:
                line_printable = " ".join(line)
            write_file.write(line_printable + '\n')


#Mude a quantidade de arquivos
n_arquivos = 10
#Coloque o caminho exato do arquivo, ex: pc/documentos/testes/
caminho_arquivo = "caminho"
for i in range(0, n_arquivos):
    username = 'Pedro Sanzio e Joao Pedro'
    if i + 1 < 10:
        read_file = f'{caminho_arquivo}TESTE-0{i+1}.txt'
    else:
        read_file = f'{caminho_arquivo}TESTE-{i+1}.txt'
    filename = read_file.replace('.txt','-RESULTADO')
    write_file = str(filename) + '.txt'
    text_generator(read_file, write_file)
