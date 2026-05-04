#------------------------------------------------------
#Script de python para probar Git
# Autor: Ariel Santamaria <asantamariaa1@est.ups.edu.ec>
# Fecha: 4/05/2026
#------------------------------------------------------

#Codigo que pregunta nombre y edad e imprima eso mismo pero con algo chevere

def main():
    nombre = input("Hermanuelo como te llamas :v? ")
    edad = input("Y cuantas primaveras tienes? ")
    
    print("Hola", nombre, "no puedo creer que tengas", edad, "primaveras :0")
    print("Mira", nombre, "salio un vamo a calmarno a continuacion:")
    
    print('''
                _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        \
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       \
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`."""""'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     \
\_ .          |   `""""'    `.           . \     \
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"""`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              \
               \/    `""\"""""""`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'mh

''')

if __name__ == "__main__":
    main()