var AtmExchangeContract = artifacts.require("./AtmExchangeContract.sol");

contract('AtmExchange', accounts => {
    const srcToken = "0xd0A1E359811322d97991E03f863a0C30C2cF029C";
    const destToken = "0xC4375B7De8af5a38a93548eb8453a498222C4fF2";
    const atmAddress = "0xd11f1077efdf72c196c82b243786f88b5e63e3a3";
    const srcQty = "10000000000000000";
    const maxDestAmount = "1500000000000000000";

    owner = accounts[0];
    it("Get  Exchange rates", async() => {
        atmExchangeContract = await AtmExchangeContract.at(atmAddress);

        console.log(accounts.length);
        atmExchangeContract = await AtmExchangeContract.at(atmAddress);
        let rate = await atmExchangeContract.getConversionRates.call(srcToken, 1, destToken, { from: owner });
        console.log('Rate(min,max) =' + rate[0] + ' ' + rate[1]);
    });

    it("Execute Swap. Exchange WETH to DAI", async() => {


        atmExchangeContract = await AtmExchangeContract.at(atmAddress);
        // ERC20 srcToken,
        // uint srcQty,
        // ERC20 destToken,
        // address destAddress,
        // uint maxDestAmount
        let txObject = await atmExchangeContract.executeSwap(srcToken, srcQty, destToken, owner, maxDestAmount, { from: owner });
        console.log(txObject);
    });


});