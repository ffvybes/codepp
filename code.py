print#update demo file when "team correction in 21"
#read file

def update_demo_txt( demo_txt, key, value) :

    with open( demo_txt, "r" ) as file:
        lines = file.readlines()
    
    with open ( demo_txt, "w" ) as file:
        for line in lines:
            if line.strip().startwith(key + "=") or line.strip().startswith(key + "="):
                file.write(f"{key} = {value} \n")
        else:
            file.write(line)
update_demo_txt("demo.txt", "TEAM", "020")

