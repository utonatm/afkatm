var AtmExchangeContract = artifacts.require("./AtmExchangeContract.sol");

contract('AtmExchange', accounts => {



    it("should put 10000 MetaCoin in the first account", async() => {
        console.log(accounts_num = accounts.length);
        await AtmExchangeContract.at("0x6f552f400bca3e1a3b772501da5e8fce6e2bb6d1");
    });


});