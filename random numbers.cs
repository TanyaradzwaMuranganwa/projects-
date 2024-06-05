using System;

namespace NumberGuessingGame
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a Random object to generate a random number
            Random random = new Random();
            // Generate a random number between 1 and 100
            int numberToGuess = random.Next(1, 101);
            int numberOfTries = 0;
            int guess = 0;
            bool win = false;

            // Welcome message
            Console.WriteLine("Welcome to the Number Guessing Game!");
            Console.WriteLine("I have randomly chosen a number between 1 and 100.");
            Console.WriteLine("Try to guess it.");

            while (!win)
            {
                Console.Write("Enter your guess: ");
                // Read user input and parse it to an integer
                string input = Console.ReadLine();
                if (int.TryParse(input, out guess))
                {
                    numberOfTries++;
                    if (guess < 1 || guess > 100)
                    {
                        Console.WriteLine("Invalid input! Please enter a number between 1 and 100.");
                    }
                    else if (guess < numberToGuess)
                    {
                        Console.WriteLine("Too low! Try again.");
                    }
                    else if (guess > numberToGuess)
                    {
                        Console.WriteLine("Too high! Try again.");
                    }
                    else
                    {
                        win = true;
                        Console.WriteLine($"Congratulations! You've guessed the number in {numberOfTries} tries.");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid input! Please enter a valid number.");
                }
            }

            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }
    }
}
