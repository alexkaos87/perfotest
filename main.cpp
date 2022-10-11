#include <iostream>
#include <memory>
#include <vector>

int main()
{
    constexpr auto maxIterations{100000000};
    auto iterations = maxIterations;
    int percentage = 10, newPercentage = 10;
    std::cout << "[" << std::flush;

    std::vector<std::unique_ptr<int>> list;
    while (--iterations)
    {
        auto pInt = std::make_unique<int>(iterations);

        newPercentage = ((double)iterations / (double)maxIterations) * 10;  
        if (percentage != newPercentage)
        {
            list.emplace_back(std::move(pInt));
            pInt = nullptr;
            percentage = newPercentage;
            std::cout << "#" << std::flush;
        } 
    }
    std::cout << "] 100%\n";

    return 0;    
}