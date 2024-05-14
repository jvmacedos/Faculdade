using System;
using System.Collections.Generic;
using System.Linq;

namespace GerenciadorDeMateriais
{
    class Equipamento
    {
        public int Id { get; set; }
        public string Nome { get; set; }
    }

    class Insumo
    {
        public int Id { get; set; }
        public string NomeInsumo { get; set; }
        public string DataValidade { get; set; }
    }

    class Program
    {
        static List<Equipamento> refrigeradores = new List<Equipamento>();
        static List<Equipamento> mixers = new List<Equipamento>();
        static List<Insumo> insumos = new List<Insumo>();

        static void Main(string[] args)
        {
            bool continuar = true;
            while (continuar)
            {
                Console.WriteLine("--- Menu ---");
                Console.WriteLine("1. Cadastrar Equipamento");
                Console.WriteLine("2. Visualizar Insumos");
                Console.WriteLine("3. Realizar Checkin de Insumo");
                Console.WriteLine("4. Realizar Checkout de Insumo");
                Console.WriteLine("5. Sair");
                Console.Write("Escolha uma opção: ");
                string opcao = Console.ReadLine();

                switch (opcao)
                {
                    case "1":
                        CadastrarEquipamento();
                        break;
                    case "2":
                        VisualizarInsumos();
                        break;
                    case "3":
                        RealizarCheckin();
                        break;
                    case "4":
                        RealizarCheckout();
                        break;
                    case "5":
                        continuar = false;
                        break;
                    default:
                        Console.WriteLine("Opção inválida.");
                        break;
                }
            }
        }

        static void CadastrarEquipamento()
        {
            Console.Write("Digite o nome do equipamento: ");
            string nome = Console.ReadLine();

            Console.Write("Digite o tipo do equipamento (refrigerador ou mixer): ");
            string tipo = Console.ReadLine();

            Equipamento equipamento = new Equipamento
            {
                Id = tipo == "refrigerador" ? refrigeradores.Count + 1 : mixers.Count + 1,
                Nome = nome
            };

            if (tipo == "refrigerador")
                refrigeradores.Add(equipamento);
            else if (tipo == "mixer")
                mixers.Add(equipamento);

            Console.WriteLine("Equipamento cadastrado com sucesso.");
        }

        static void VisualizarInsumos()
        {
            Console.WriteLine("--- Insumos ---");
            foreach (var insumo in insumos)
            {
                Console.WriteLine($"ID: {insumo.Id}, Nome do Insumo: {insumo.NomeInsumo}, Data de Validade: {insumo.DataValidade}");
            }
        }

        static void RealizarCheckin()
        {
            Console.Write("Digite o tipo do equipamento (refrigerador ou mixer): ");
            string tipoEquipamento = Console.ReadLine();

            Console.Write("Digite o ID do equipamento: ");
            int idEquipamento = int.Parse(Console.ReadLine());

            Console.Write("Digite o nome do insumo: ");
            string nomeInsumo = Console.ReadLine();

            Console.Write("Digite a data de validade do insumo (dd/mm/aaaa): ");
            string dataValidade = Console.ReadLine();

            Insumo insumo = new Insumo
            {
                Id = insumos.Count + 1,
                NomeInsumo = nomeInsumo,
                DataValidade = dataValidade
            };

            Equipamento equipamento = null;
            if (tipoEquipamento == "refrigerador")
            {
                equipamento = refrigeradores.FirstOrDefault(e => e.Id == idEquipamento);
            }
            else if (tipoEquipamento == "mixer")
            {
                equipamento = mixers.FirstOrDefault(e => e.Id == idEquipamento);
            }

            if (equipamento != null)
            {
                insumos.Add(insumo);
                Console.WriteLine("Checkin realizado com sucesso.");
            }
            else
            {
                Console.WriteLine("Equipamento não encontrado.");
            }
        }

        static void RealizarCheckout()
        {
            Console.Write("Digite o ID do insumo: ");
            int idInsumo = int.Parse(Console.ReadLine());

            Insumo insumo = insumos.Find(i => i.Id == idInsumo);

            if (insumo != null)
            {
                insumos.Remove(insumo);
                Console.WriteLine("Checkout realizado com sucesso.");
            }
            else
            {
                Console.WriteLine("Insumo não encontrado.");
            }
        }
    }
}
