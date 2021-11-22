#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start_amount = 0;
    int end_amount = 0;
    int years = 0;
    // TODO: Prompt for start size
    while (start_amount < 9)
    {
        start_amount = get_int("How many llamas to start? \n");
    }

    // TODO: Prompt for end size
    while (end_amount < start_amount)
    {
        end_amount = get_int("How many llames to end? \n");
    }

    // TODO: Calculate number of years until we reach threshold
    while (start_amount < end_amount)
    {
        start_amount += (start_amount / 3) - (start_amount / 4);
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
