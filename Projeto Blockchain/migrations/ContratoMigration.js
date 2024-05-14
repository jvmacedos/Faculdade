const Contrato = artifacts.require("Contrato");


module.exports = function(deployer){
   deployer.deploy(ContratoExemplo, "Contrato");
};
