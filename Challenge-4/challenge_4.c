#include <stdio.h>

#define MAX(a,b) ((a > b) ? a : b )
#define MIN(a,b) ((a < b) ? a : b )

// Find the volume of the lake
int trap (int height[], int size)
{
    // Initialize two arrays that keep track of max height from left and right
    int left_max[size], right_max[size];
    // Total valume of the lake
    int total = 0;

    // If there's no terrain, the valume of the lake is zero
    if (size == 0)
    		return total;
    // Left to right
    left_max[0] = height[0];
    for (int i=1; i<size; i++)
        left_max[i] = MAX (height[i], left_max[i - 1]);
    // Right to left
    right_max[size-1] = height[size-1];
    for (int i=size-2; i>=0; i--)
        right_max[i] = MAX (height[i], right_max[i + 1]);
    // Calculate the actual volume of the lake
    for (int i=1; i<size-1; i++)
        total += MIN (left_max[i], right_max[i]) - height[i];

    return total;
}

int main ()
{
    // The given array
    int height[] = {1,3,2,4,1,3,1,4,5,2,2,1,4,2,2};
    // Size of the given array
    int size = sizeof(height) / sizeof(int);

    int max = 0;
    for (int i=0; i<size; i++) {
        max = MAX(height[i], max);
    }

    printf("Correct Result: 15\n");
    printf("Result from trap() function: %d\n", trap(height, size));
}
