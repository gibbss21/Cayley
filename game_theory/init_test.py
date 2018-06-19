import Cayley as cy
import Cayley.game_theory as cg
from Cayley.change_me import timesteps
import csv

def main():
    print("Enter 'Linear', 'Limited', or 'Complete' for model type.")
    model = input('Model: ').lower()
    const = 1
    if model == 'limited':
        radius = 0.07
    else: radius = 0
    network = cg.Senate(model, const, radius)

    issue = float(input("What is the issue rating? "))
    polarity = issue-0.5
    const = 300
    senate = cy.MonteCarlo(network, 1/(const*(abs(polarity)+0.01)), 0, 1/(const*(abs(polarity)+0.01)))

    print("\n" + "Enter Excel file name \n"
          + "Example: monteCarloData")
    filename = str(input("Filename: "))
    full_filename = filename + ".xlsx"
    for i in range(timesteps):
        senate.senateDictionary(issue)
##    for i in range(timesteps):
##        senate.simulateVote()
    senate.sendExcel(full_filename)

if __name__ == '__main__':
    main()
