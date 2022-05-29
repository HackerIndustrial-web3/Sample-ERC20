// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/* Sample of a simple erc20 contract
Dean Dunbar, HackerIndustrial 2022  */


import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC20/ERC20.sol";


contract HackerIndustrialToken is ERC20 {
    // wei value for the inital supply so supply = supply * 10**decimals
    constructor(uint256 initialSupply) ERC20("HackerIndustrial Tokan", "HIT") {
        _mint(msg.sender, initialSupply);
    }
}
