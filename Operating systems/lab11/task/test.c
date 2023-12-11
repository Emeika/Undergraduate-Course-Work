#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Define a structure to represent a student
struct Student
{
    char name[50];
    int age;
    float gpa;
};

int main()
{
    int num_students = 0; // Initialize to 0 initially

    // Dynamically allocate memory for an initial array of structures
    struct Student *student_array = (struct Student *)malloc(sizeof(struct Student));

    if (student_array == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Input student data
    char response;
    do
    {
        // Prompt the user if they want to enter another student
        printf("Do you want to enter another student? (y/n): ");
        scanf(" %c", &response);

        if (response == 'y' || response == 'Y')
        {
            printf("Enter details for student %d:\n", num_students + 1);
            printf("Name: ");
            scanf("%s", student_array[num_students].name);

            char ageInput[10];
            while (1)
            {
                printf("Age: ");
                if (scanf("%s", ageInput) != 1 || !isdigit(ageInput[0]))
                {
                    printf("Invalid input for age. Please enter a valid integer.\n");
                }
                else
                {
                    student_array[num_students].age = atoi(ageInput);
                    break; // Exit the loop if a valid input is provided
                }
            }

            printf("GPA: ");
            scanf("%f", &student_array[num_students].gpa);

            num_students++; // Increment the count of entered students

            // Resize the array for the next student
            student_array = realloc(student_array, (num_students + 1) * sizeof(struct Student));

            if (student_array == NULL)
            {
                printf("Memory allocation failed\n");
                return 1;
            }
        }

    } while (response == 'y' || response == 'Y');

    // Display student data
    printf("\nStudent details:\n");
    for (int i = 0; i < num_students; ++i)
    {
        printf("Student %d:\n", i + 1);
        printf("Name: %s\n", student_array[i].name);
        printf("Age: %d\n", student_array[i].age);
        printf("GPA: %.2f\n", student_array[i].gpa);
        printf("\n");
    }

    // Free the allocated memory
    free(student_array);

    return 0;
}
