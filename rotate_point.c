#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265

void rotate(double*, double*, double*);

int main(void) {
	double x_coordinate;
	double y_coordinate;
	double angle_of_rotation;
	
	printf("Please enter an x coordinate: ");
	scanf("%lf", &x_coordinate);
	printf("Please enter a y coordinate: ");
	scanf("%lf", &y_coordinate);
	printf("Please enter an angle of rotation: ");
	scanf("%lf", &angle_of_rotation);

	rotate(&x_coordinate, &y_coordinate, &angle_of_rotation);
	printf("The result is (%lf, %lf)\n", x_coordinate, y_coordinate);

	return 0;
}

void rotate(double *x_coordinate, double *y_coordinate, double *angle) {
	*angle = (PI / 180) * *angle;
	*x_coordinate = (*x_coordinate * cos(*angle)) - (*y_coordinate * sin(*angle));
	*y_coordinate = (*x_coordinate * sin(*angle)) + (*y_coordinate * cos(*angle));

}

