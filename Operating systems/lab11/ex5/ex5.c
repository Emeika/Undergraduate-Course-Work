#include <stdio.h>
#include <stdlib.h>

// Define a structure to represent a student
struct Student
{
    char name[50];
    int age;
    float gpa;
};

int main()
{
    int num_students;

    // Prompt the user for the number of students
    printf("Enter the number of students: ");
    scanf("%d", &num_students);

    // Dynamically allocate memory for an array of structures
    struct Student *student_array = (struct Student *)malloc(num_students * sizeof(struct Student));

    if (student_array == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Input student data
    for (int i = 0; i < num_students; ++i)
    {
        printf("Enter details for student %d:\n", i + 1);
        printf("Name: ");
        scanf("%s", student_array[i].name);
        printf("Age: ");
        scanf("%d", &student_array[i].age);
        printf("GPA: ");
        scanf("%f", &student_array[i].gpa);
    }

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
