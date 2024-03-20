import java.util.Scanner;
public class Colaborador {
 /**
 * @param args
 */
public static void main(String[] args) {
 // TODA LOGICA DO CODIGO ESTA AQUI

 Scanner ler = new Scanner(System.in);
 Gerente gerente = new Gerente();
 Administrativo adm = new Administrativo();

 System.out.println("Informe o seu nome: ");
 gerente.nome = ler.next();

 System.out.println("O nome do gerente informado é: "+ gerente.nome);

 gerente.trabalhar();

 System.out.print("################################################");

 System.out.println("Informe o nome do colaborador administrativo: ");
 adm.nome = ler.next();
 System.out.println("Informe o CPF do colaborador administrativo: ");
 adm.CPF = ler.nextLong();
 System.out.println("Informe a função: ");
 adm.funcao = ler.next();

 System.out.println("Dados para confirmação: ");
 System.out.println("Nome: "+ adm.nome);
 System.out.println("CPF: "+ adm.CPF);
 System.out.println("Nome: "+ adm.funcao);
 adm.comer(); 
ler.close();
}
}