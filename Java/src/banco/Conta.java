package banco;

public class Conta {
    private Cliente cliente;
    private double saldo;

    public Conta(Cliente cliente, double saldoInicial) {
        this.cliente = cliente;
        this.saldo = saldoInicial;
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public boolean sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
            return true; // Saque bem-sucedido
        } else {
            return false; // Saldo insuficiente
        }
    }

    public double consultarSaldo() {
        return saldo;
    }

    public Cliente getCliente() {
        return cliente;
    }
}
