// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

contract Contrato {
    uint128 public numero;
    function guardar(uint128 _numero) public {
        numero = _numero;
    }
}
