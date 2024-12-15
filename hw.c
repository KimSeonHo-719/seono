#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void tustinTransform(double *num, double *den, double *numZ, double *denZ, double T) {
    double alpha = 2.0 / T;

    numZ[0] = num[0] * alpha + num[1];
    numZ[1] = -num[0] * alpha + num[1];
    denZ[0] = den[0] * alpha + den[1];
    denZ[1] = -den[0] * alpha + den[1];

    double normFactor = denZ[0];
    for (int i = 0; i < 2; i++) {
        numZ[i] /= normFactor;
        denZ[i] /= normFactor;
    }
}
void zohTransform(double *num, double *den, double *numZ, double *denZ, double T) {
    double alpha = exp(-den[1] * T);

    numZ[0] = num[0];
    numZ[1] = num[1] - num[0] * alpha;
    denZ[0] = 1.0;
    denZ[1] = -alpha;

    double normFactor = denZ[0];
    for (int i = 0; i < 2; i++) {
        numZ[i] /= normFactor;
        denZ[i] /= normFactor;
    }
}
void matchedPoleZeroTransform(double *num, double *den, double *numZ, double *denZ, double T) {
    double alpha = exp(-den[1] * T);

    numZ[0] = num[0];
    numZ[1] = num[1] - num[0] * alpha;
    denZ[0] = 1.0;
    denZ[1] = -alpha;

    double normFactor = denZ[0];
    for (int i = 0; i < 2; i++) {
        numZ[i] /= normFactor;
        denZ[i] /= normFactor;
    }
}

// 전달 함수 출력
void printPolynomial(const char *label, double *num, double *den) {
    printf("%s:\n", label);
    printf("Numerator: %.5fz^-0 + %.5fz^-1\n", num[0], num[1]);
    printf("Denominator: 1.00000z^-0 + %.5fz^-1\n", den[1]);
}

int main(void) {
    double T; 
    double num[2], den[2]; 
    double numTustin[2] = {0}, denTustin[2] = {0};
    double numZOH[2] = {0}, denZOH[2] = {0};
    double numMPZ[2] = {0}, denMPZ[2] = {0};

    // 입력
    printf("Enter numerator coefficients (b0 b1): ");
    scanf("%lf %lf", &num[0], &num[1]);
    printf("Enter denominator coefficients (a0 a1): ");
    scanf("%lf %lf", &den[0], &den[1]);
    printf("Enter sampling time T: ");
    scanf("%lf", &T);

    tustinTransform(num, den, numTustin, denTustin, T);
    zohTransform(num, den, numZOH, denZOH, T);
    matchedPoleZeroTransform(num, den, numMPZ, denMPZ, T);

    printPolynomial("Tustin Transform", numTustin, denTustin);
    printf("\n");
    printPolynomial("ZOH Transform", numZOH, denZOH);
    printf("\n");
    printPolynomial("Matched Pole-Zero Transform", numMPZ, denMPZ);
    printf("\n");
    return 0;
}
