import subprocess
import typer
from colorama import Fore, Style

def print_colored_message(message, color):
    typer.echo(f"{color}{message}{Style.RESET_ALL}")

def choice_0():
    list_rule = ["sudo", "iptables", "-L", "-n", "-v"]    
    try:
        print_colored_message(" [*] Rules list of iptables : ", Fore.BLUE)
        process = subprocess.Popen(list_rule, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if stdout:
            typer.echo(stdout)
        else:
            print_colored_message(" [*] The command does not send any exit !", Fore.YELLOW)
        if stderr:
            print_colored_message(" [*] Error running the command : ", stderr, Fore.RED)
    except Exception as e:
        print_colored_message(" [*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def choice_1():
    list_rule = ["sudo", "iptables", "-P"]
    print_colored_message(" [*] Change general rules : ", Fore.BLUE)
    in_out = str(input("Enter 'INPUT' or 'OUTPUT' or 'FORWARD': "))
    list_rule.append(in_out)
    list_rule.append(in_out.upper())
    decision = str(input("Enter 'DROP' (if we cute the transmission) or 'ACCEPT' (if we accept the transmission) : "))
    list_rule.append(decision)
    
    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Change general rules with succes !", Fore.YELLOW)
    except Exception as e:
        print_colored_message("Error when adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def choice_2():
    list_rule = ["sudo", "iptables", "-A"]
    print_colored_message(" [*] Add rule with interface and decision: ", Fore.BLUE)
    in_out = str(input("Enter 'INPUT' or 'OUTPUT' or 'FORWARD': "))
    list_rule.append(in_out)
    list_rule.append(in_out.upper())
    option_in_out = str(input("Enter '-i' (if the interface is specialized for input ) or '-o' (if the interface is specialized for output) : "))
    list_rule.append(option_in_out)
    interface_name = str(input("Enter the interface [lo, eth0, ...]: "))
    list_rule.append(interface_name)
    list_rule.append("-j")
    decision = str(input("Enter 'DROP' (if we cute the transmission) or 'ACCEPT' (if we accept the transmission): "))
    list_rule.append(decision)
    
    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Adding rule with successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def choice_3():
    list_rule = ["sudo", "iptables", "-A"]
    print_colored_message(" [*] Add rule with protocole , port and decision: ", Fore.BLUE)
    in_out = str(input("Enter 'INPUT' or 'OUTPUT' or 'FORWARD': "))
    list_rule.append(in_out)
    list_rule.append(in_out.upper())
    list_rule.append("-p")
    protocole_name = str(input("Enter name of protocol: "))
    list_rule.append(protocole_name)
    list_rule.append("--dport")
    port_number = str(input("Enter port number: "))
    list_rule.append(port_number)
    list_rule.append("-j")
    decision = str(input("Enter 'DROP' (if we cute the transmission) or 'ACCEPT' (if we accept the transmission): "))
    list_rule.append(decision)
    
    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Adding rule with successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def choice_4():
    list_rule = ["sudo", "iptables", "-A"]
    print_colored_message(" [*] Add rule with protocole , source or destination ip address  and decision: ", Fore.BLUE)
    in_out = str(input("Enter 'INPUT' or 'OUTPUT' or 'FORWARD': "))
    list_rule.append(in_out)
    list_rule.append(in_out.upper())
    list_rule.append("-p")
    protocole_name = str(input("Enter name of protocol : "))
    list_rule.append(protocole_name)
    option_src_dest = str(input("Enter '-s' (to specify ip address source) or '-d' (to specify ip address destination): "))
    list_rule.append(option_src_dest)
    ip_src_dest = str(input("Enter source or destination ip address (x.x.x.x/24): "))
    list_rule.append(ip_src_dest)
    list_rule.append("-j")
    decision = str(input("Enter 'DROP' (if we cute the transmission) or 'ACCEPT' (if we accept the transmission): "))
    list_rule.append(decision)

    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Adding rule with successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def choice_5():
    list_rule = ["sudo", "iptables", "-A"]
    print_colored_message(" [*] Add rule with protocole, port, source or destination ip address  and decision: ", Fore.BLUE)
    in_out = str(input("Enter 'INPUT' or 'OUTPUT' or 'FORWARD': "))
    list_rule.append(in_out)
    list_rule.append(in_out.upper())
    list_rule.append("-p")
    protocole_name = str(input("Enter name of protocol: "))
    list_rule.append(protocole_name)
    list_rule.append("--dport")
    port_number = str(input("Enter port number: "))
    list_rule.append(port_number)
    option_src_dest = str(input("Enter '-s' (to specify ip address source) or '-d' (to specify ip address destination): "))
    list_rule.append(option_src_dest)
    ip_src_dest = str(input("Enter source or destination ip address (x.x.x.x/24): "))
    list_rule.append(ip_src_dest)
    list_rule.append("-j")
    decision = str(input("Enter 'DROP' (if we cute the transmission) or 'ACCEPT' (if we accept the transmission): "))
    list_rule.append(decision)
    
    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Adding rule with successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def choice_6():
    list_rule = ["sudo", "iptables", "-A"]
    print_colored_message(" [*] Add rule with interface , protocole, port and decision: ", Fore.BLUE)
    in_out = str(input("Enter 'INPUT' or 'OUTPUT' or 'FORWARD': "))
    list_rule.append(in_out)
    list_rule.append(in_out.upper())
    option_in_out = str(input("Enter '-i' (if the interface is specialized for input ) or '-o' (if the interface is specialized for output): "))
    list_rule.append(option_in_out)
    interface_name = str(input("Enter the interface [lo, eth0, ...]: "))
    list_rule.append(interface_name)
    list_rule.append("-p")
    protocole_name = str(input("Enter name of protocol: "))
    list_rule.append(protocole_name)
    list_rule.append("--dport")
    port_number = str(input("Enter port number: "))
    list_rule.append(port_number)
    list_rule.append("-j")
    decision = str(input("Enter 'DROP' (if we cute the transmission) or 'ACCEPT' (if we accept the transmission): "))
    list_rule.append(decision)
    
    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Adding rule with successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def choice_7():
    list_rule = ["sudo", "iptables", "-A"]
    print_colored_message(" [*] Add rule with interface , protocole, port, ip address of the source or destination and decision: ", Fore.BLUE)
    in_out = str(input("Enter 'INPUT' or 'OUTPUT' or 'FORWARD': "))
    list_rule.append(in_out)
    list_rule.append(in_out.upper())
    option_in_out = str(input("Enter '-i' (if the interface is specialized for input ) or '-o' (if the interface is specialized for output) : "))
    list_rule.append(option_in_out)
    interface_name = str(input("Enter the interface [lo, eth0, ...]: "))
    list_rule.append(interface_name)
    list_rule.append("-p")
    protocole_name = str(input("Enter name of protocol: "))
    list_rule.append(protocole_name)
    list_rule.append("--dport")
    port_number = str(input("Enter port number: "))
    list_rule.append(port_number)
    option_src_dest = str(input("Enter '-s' (to specify ip address source) or '-d' (to specify ip address destination): "))
    list_rule.append(option_src_dest)
    ip_src_dest = str(input("Enter source or destination ip address (x.x.x.x/24): "))
    list_rule.append(ip_src_dest)
    list_rule.append("-j")
    decision = str(input("Enter 'DROP' (if we cute the transmission) or 'ACCEPT' (if we accept the transmission): "))
    list_rule.append(decision)
    
    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Adding rule with successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def delete_rules():
    list_rule = ["sudo", "iptables", "-F"]
    print_colored_message(" [*] Delete all rules !", Fore.BLUE)

    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Delete all rules withe successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)
#------------------------------------------------------------------------------------------------------------------------------

def delete_one_rule(rule_number):
    list_rule = ["sudo", "iptables", "-D", str(rule_number)]
    print_colored_message(" [*] Delete one rule !", Fore.BLUE)

    try:
        subprocess.run(list_rule)
        print_colored_message("[*] Delete one rules withe successfully !", Fore.GREEN)
    except Exception as e:
        print_colored_message("[*] Error adding the rule ", e, Fore.RED)

def main():
    if typer.confirm("Want to add or delete rules on your firewall ? "):
        choice = 0
        while choice != 10:
            print("""
                > Enter 0 to view list  of irewall rules
                > Enter 1 to change the general rule of the firewall
                > Enter 2 to add a rule and specify the interface and the decision
                > Enter 3 to add a rule and specify the protocol , port and the decision
                > Enter 4 to add a rule and specify the protocol , ip address of the source or destination and the decision
                > Enter 5 to add a rule and specify the protocol , port , ip address of the source or destination and the decision
                > Enter 6 to add a rule and specify the interface , protocol , port and the decision
                > Enter 7 to add a rule and specify the interface , protocol , port , ip address of the source or destination and the decision
                > Enter 8 to delete all rules of the firewall
                > Enter 9 to delete one rule of the firewall
                > Enter 10 to exit
            """)
            try:
                choice = int(input("Enter your choice : "))
                if choice == 0:
                    choice_0()
                elif choice == 1:
                    choice_1()
                elif choice == 2:
                    choice_2()
                elif choice == 3:
                    choice_3()
                elif choice == 4:
                    choice_4()
                elif choice == 5:
                    choice_5()
                elif choice == 6:
                    choice_6()
                elif choice == 7:
                    choice_7()
                elif choice == 8:
                    delete_rules()
                elif choice == 9:
                    rule_number = str(input("Enter number of the line where the rule is located: "))
                    delete_one_rule(rule_number)
                elif choice == 10:
                    print("Ending of script execution ...")
                else:
                    print_colored_message("Your choice is invalid !", Fore.RED)
            except ValueError:
                print_colored_message("Make sure number does not other character !", Fore.RED)
    else:
        print_colored_message("Ending of script execution ...", Fore.GREEN)

if __name__ == "__main__":
    typer.run(main)

"""
    > stdout=subprocess.PIPE: Cela redirige la sortie standard (stdout) du processus exécuté vers un objet de type PIPE. 
    Cela signifie que la sortie de la commande sera capturée et stockée dans l'objet stdout pour être utilisée ultérieurement.
    > stderr=subprocess.PIPE: Cela redirige la sortie d'erreur (stderr) du processus exécuté vers un objet de type PIPE. 
    Cela permet de capturer les éventuelles erreurs générées par la commande.
    > stdout, stderr = process.communicate(): Cette ligne exécute réellement la commande et capture à la fois la sortie standard (stdout) et la sortie d'erreur (stderr) dans les variables stdout et stderr.
    communicate() attend que le processus se termine et collecte ses sorties.
"""