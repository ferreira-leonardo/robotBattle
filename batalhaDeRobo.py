import random

class Part():
    
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption
        
    # Dicionário com os status das partes do robo
    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        
        return { 
             f"{formatted_name}_name": self.name.upper(),
             f"{formatted_name}_status": "Available" if self.is_available() else "Unavailable",
             f"{formatted_name}_attack": self.attack_level,
             f"{formatted_name}_defense": self.defense_level,
             f"{formatted_name}_energy_consump": self.energy_consumption,
        }
         
    # Verifica se a parte está disponível   
    def is_available(self):
        return self.defense_level > 0 
    
    # Reduz a defesa do robo
    def reduce_edefense(self, attack_level):
        self.defense_level = self.defense_level - attack_level
        if self.defense_level <= 0:
            self.defense_level = 0


class Robot:
    
    def __init__(self, name, color_code):
        
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [ 
            Part("Head", attack_level=7, defense_level=10, energy_consumption=15),
            Part("Weapon", attack_level=10, defense_level=8, energy_consumption=15), 
            Part("Left Arm", attack_level=5, defense_level=5, energy_consumption=10),
            Part("Right Arm", attack_level=6, defense_level=7, energy_consumption=10),
            Part("Left Leg", attack_level=4, defense_level=5, energy_consumption=10),
            Part("Right Leg", attack_level=5, defense_level=12, energy_consumption=10),
        ]
    
    # Printa o status do robo
    def print_status(self):
        
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["Branco"])
    
    # Printa o nome 
    def greet(self):
        print(f"Olá meu nome é {self.name}")
    
    # Printa a quantidade de energia
    def print_energy(self):
        print(f"Nós temos {self.energy}% de energia restante")
    
    # Dicionário com todas as partes do robô
    def get_part_status(self):
        
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status
      
    # Verifica se as partes estão disponíveis, no mínimo uma o jogo continua
    def is_there_available_part(self):
        
        for part in self.parts:
            if part.is_available():
                return True
        return False
     
    # Verifica se o robo está ligado 
    def is_on(self):
        return self.energy > 0 
    
    # Ataque 
    def attack(self, enemy_robot, part_to_use, part_to_attack):
               
       enemy_robot.parts[part_to_attack].reduce_edefense(self.parts[part_to_use].attack_level) 
       self.energy -= self.parts[part_to_use].energy_consumption
    
    # Auto attack para quando escolher a opção de 1 jogador, o robo 2 atacar sozinho
    def attack_auto(self, current_robot):
       
        # Escolhe aleatoriamnente entre um número 0-5 para ser a parte que vai usar para atacar
        part_to_use_index = random.randint(0, 5) 
        # Loop para avaliar se a parte do robo escolhida no código acima está disponível
        while not self.parts[part_to_use_index].is_available():
            part_to_use_index = random.randint(0, 5) 

        part_to_use = self.parts[part_to_use_index]

        print(f"O robô {self.name} utilizou a {part_to_use.name} para atacar")
           
        # Escolhe aleatoriamente entre um número 0-5 para ser a parte onde vai ser atacada
        part_to_attack_index = random.randint(0, 5) 
      
        # Loop para avaliar se a parte do robo escolhida no código acima pra ser atacada está disponível
        while not current_robot.parts[part_to_attack_index].is_available():
            part_to_attack_index = random.randint(0, 5)
            
        part_to_attack = self.parts[part_to_attack_index]
        print(f"O robô {self.name} atacou {part_to_attack.name} do seu robô")
        
        # Executar o attack
        current_robot.parts[part_to_attack_index].reduce_edefense(part_to_use.attack_level) 
        
        # Reduzir a energia
        self.energy -= self.parts[part_to_use_index].energy_consumption



class Builds:

    def build_robot(self):
        
        self.nome = [] 
        self.cor = [] 
        
        robot_name = input("Nome do robô: ")
        self.nome.append(robot_name)
        color_code = self.choose_color()
        self.cor.append(color_code)
        
        robot = Robot(robot_name, color_code)
        robot.print_status()
        return robot


    def build_robot_2(self): 
    
        robot_name = input("Nome do robô: ")
        while robot_name in self.nome:
           robot_name = input("O nome do robô já está em uso, escolha outro!")
        

        color_code = self.choose_color()
        while color_code in self.cor:
           color_code = input("A cor do robô já está em uso, escolha outro!")
       

        robot = Robot(robot_name, color_code)
        robot.print_status()
        return robot


    
    def build_robot_machine(self):

        names_random = ["Megatron", "OptimusPrime","Bumblebee","Scar","Atomo"] 
        robot_name = random.choice(names_random)
        
        
        while robot_name in self.nome: 
            robot_name = random.choice(names_random)
        

        color_code = random.choice(list(colors.values()))
        
        while color_code in self.cor: 
            color_code = random.choice(list(colors.values()))
        

        robot = Robot(robot_name, color_code)
        robot.print_status()
        return robot


    
    def choose_color(self):
        
        available_colors = colors
        print("Cores disponíveis:")
        for key, value in available_colors.items():
            print(value, key)
        print(colors["Branco"])
        
        
        valid_input = True
        while  valid_input:

            chosen_color = input("Escolha uma cor:").capitalize()
            if chosen_color not in available_colors:
                print("Por favor, escolha uma cor disponível.")
            else:
                valid_input = False
        
        color_code = available_colors[chosen_color]
        return color_code

   
robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| 'o  o' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
                                
"""


colors = {
        "Preto": '\x1b[90m',
        "Azul": '\x1b[94m',
        "Ciano": '\x1b[96m',
        "Verde": '\x1b[92m',
        "Rosa": '\x1b[95m',
        "Vermelho": '\x1b[91m',
        "Branco": '\x1b[97m',
        "Amarelo":'\x1b[93m',
    }


def play():
    builds = Builds() # Instânciado a classe Builds para conseguir usar os métodos de builds em robot_one e robot_two
   
    playing = True

    partes = "\n0 - Cabeça\n1 - Arma\n2 - Braço Esquerdo\n3 - Braço Direito\n4 - Perna Esquerda\n5 - Perna Direita "

    print("Desenvolvimento:  Beatriz Machado, Luiz Felix e Leonardo Ferreira. \nBem-vindo ao jogo Mech Showdown 🤖")
   
    # Loop para verificar se o input abaixo está dentro da lista, caso não esteja repete até escolher uma opção válida
    verification = True
    while verification:
        try:
            jogadores = int(input("\nOlá, quantos jogadores vão ser 1️⃣ ou 2️⃣?: "))
        
            if jogadores not in [1, 2]:
                print("Escolha um número entre 1 e 2")
                continue  
            verification = False
        except ValueError:
            print("Entrada inválida. Apenas números inteiros")
    
    # Condição para opção de 1 jogador
    if jogadores == 1:
       print("Dados do jogador 1:")
       robot_one = builds.build_robot()
       print("Dados da máquina:")
       robot_two = builds.build_robot_machine()
        
       while playing:
          current_robot = robot_one
          enemy_robot = robot_two
          current_robot.print_status()
        
          
          # Loop pra que a parte escolhida para utilizar no ataque esteja disponível e seja um número entre 0-5
          repeat = True
          while repeat:
              try:
                print(partes)
                part_to_use = int(input("Escolha a parte do robo que você vai usar para atacar: "))
       
                if part_to_use not in range(6):
                      print("Entrada invalida, escolha uma opção entre 0-5") 
                      continue
                  
                if not current_robot.parts[part_to_use].is_available():
                    print("Esta parte já está desabilitada. Escolha outra parte para atacar.")
                    continue

                repeat = False    
                  
              except ValueError:
                print("Opção inválida, escolha uma opção entre 0-5")
            
          enemy_robot.print_status() 
        
          #  Loop pra que a parte escolhida para atacar esteja disponível e seja um número entre 0-5
          repeat1 = True
          while repeat1:
              try:
                  print(partes)
                  part_to_attack = int(input("Escolha a parte do inimigo para atacar: "))
                  
                  if part_to_attack not in range(6):
                      print("Número não está entre 0-5, tente novamente!") 
                      continue
                  
                  if not enemy_robot.parts[part_to_attack].is_available():
                      print("Esta parte já está desabilitada. Escolha outra que você deseja atacar entre 0-5.")
                      continue
                  
                  current_robot.attack(enemy_robot, part_to_use, part_to_attack)
                  
                  
                  if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
                      playing = False
                      print(f"Parabéns {current_robot.name} você venceu")
                 
                  else:
                      enemy_robot.attack_auto(current_robot)   
                  
                      if not current_robot.is_on() or current_robot.is_there_available_part() == False:
                          current_robot.print_status()
                          playing = False
                          print(f"Parabéns {enemy_robot.name} você venceu")
                  
                 
                  repeat1 = False    
                  
              except ValueError:
                  print("Opção inválida, escolha uma opção entre 0-5")
          
    # Condição pra quando a opção de 2 jogadores for válida 
    elif jogadores == 2:
    
        print("Dados do jogador 1:")
        robot_one = builds.build_robot()
      
        robot_two = builds.build_robot_2() 
        
        current_robot = robot_one
        enemy_robot = robot_two
        rount = 0
      
        
        while playing:
            if rount % 2 == 0:
                current_robot = robot_one
                enemy_robot = robot_two
            else:
                current_robot = robot_two
                enemy_robot = robot_one
            
            current_robot.print_status()
                  
            
            repeat_part_to_use = True
            while repeat_part_to_use:
                try:
                    print(partes) 
                    part_to_use = int(input("Escolha a parte do robo que você vai usar para atacar: "))
                
                    if part_to_use not in range(6):
                        print("Entrada invalida, escolha uma opção entre 0-5") 
                        continue
                  
                    if not current_robot.parts[part_to_use].is_available():
                        print("Esta parte já está desabilitada. Escolha outra parte para atacar.")
                        continue

                    repeat_part_to_use = False    
                  
                except ValueError:
                    print("Entrada inválida!")

            
            enemy_robot.print_status()

          
            repeat_part_to_attack = True
            while repeat_part_to_attack:
                try:
                    print(partes) 
                    part_to_attack = int(input("Escolha a parte do inimigo para atacar: "))
                
                    if part_to_attack not in range(6):
                        print("Entrada invalida, escolha uma opção entre 0-5") 
                        continue
                  
                    if not enemy_robot.parts[part_to_attack].is_available():
                        print("Esta parte já está desabilitada. Escolha outra que você deseja atacar entre 0-5.")
                        continue
                  
                    current_robot.attack(enemy_robot, part_to_use, part_to_attack)
                    rount += 1
                    repeat_part_to_attack = False    
                  
                except ValueError:
                    print("Entrada inválida!")
              
            if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
                playing = False
                print(f"Parabéns {current_robot.name} você venceu")

            elif not current_robot.is_on() or current_robot.is_there_available_part() == False:
                playing = False
                print(f"Parabéns {enemy_robot.name} você venceu")
              

play()