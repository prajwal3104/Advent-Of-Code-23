#include <iostream>
#include <iomanip>
#include <vector>

class Stock {
protected:
    double cp;
    int noOfShares;

public:
    void setStock(double price, int shares) {
        cp = price;
        noOfShares = shares;
    }
};

class PfVal : public Stock {
public:
    double calculatePfVal() {
        return cp * noOfShares;
    }
};

class Profit : public Stock {
private:
    double bp;

public:
    void setbp(double price) {
        bp = price;
    }

    double calProf() {
        return (cp - bp) * noOfShares;
    }
};

std::vector<double> calPtfAndPf(double cp, double bp, int noOfShares) {
    PfVal portfolio;
    Profit profit;

    // Set values
    portfolio.setStock(cp, noOfShares);
    profit.setStock(cp, noOfShares);
    profit.setbp(bp);

    // Calculate values
    double PfVal = portfolio.calculatePfVal();
    double profitValue = profit.calProf();

    return {PfVal, profitValue};
}

void readHiddenTestInput(double &cp, double &bp, int &noOfShares) {
    std::cin >> cp >> bp >> noOfShares;
}

int main() {
    // Input
    double cp, bp;
    int noOfShares;

    // Read input from the hidden test case
    readHiddenTestInput(cp, bp, noOfShares);

    // Run test case
    std::vector<double> result = calPtfAndPf(cp, bp, noOfShares);

    // Output
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Portfolio Value: " << result[0] << std::endl;
    std::cout << "Profit: " << result[1] << std::endl;

    return 0;
}
