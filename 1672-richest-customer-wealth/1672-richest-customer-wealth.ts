function maximumWealth(accounts: number[][]): number {
    let totalCustomersWealth = 0;
    for(let i=0; i<accounts.length; i++) {
        let totalAmount = 0;
        for(let j=0; j < accounts[i].length; j++) {
            totalAmount += accounts[i][j]
        }
        if(totalCustomersWealth < totalAmount) {
            totalCustomersWealth = totalAmount
        }
    }
    return totalCustomersWealth;
};
